# Copilot Instructions for Travel AI Website

## Project Overview
Flask-based travel AI application that integrates OpenAI and third-party travel APIs (Booking.com, TripAdvisor, Google Maps) to help users plan trips via a chat interface.

## Architecture

### Application Structure
- **Entry point**: `run.py` - Flask app factory with Debug/Production config switching
- **App factory**: `apps/__init__.py` - Uses `create_app()` pattern with blueprint registration
- **Blueprints** (registered in order): `authentication`, `home`, `tool`, `payment`, `chat`

### Key Modules
| Module | Purpose |
|--------|---------|
| `apps/chat/` | AI chat system - routes handle message storage, `api/` contains OpenAI and travel API integrations |
| `apps/chat/api/openAI.py` | Core AI orchestration with class hierarchy: `AI_handle_data` → `AI_required` → `AI_response` → `AI_main` |
| `apps/chat/api/config.py` | API configuration with RapidAPI headers for external services |
| `apps/authentication/` | Flask-Login based auth with SQLAlchemy `Users` model |
| `apps/tool/` | Content generation tools defined in `writingTool.py` as `dataJson` dict |

## Business Logic - AI Chat System

### Core Flow (`apps/chat/api/openAI.py`)
1. **User sends message** → `AI_main.run(data)` is called
2. **Main conversation** → `AI_required.main_required()` calls GPT-3.5-turbo-16k
3. **Response handling** → `AI_response.finish_reason()` handles incomplete responses (loops until `finish_reason == "stop"`)
4. **API extraction** → `suport_system()` parses AI response for travel API calls
5. **External API calls** → `select_function()` → `print_json_structure()` extracts structured API params

### Class Hierarchy
```
AI_handle_data          # JSON state management (user_promt, AI_promt, read/write)
    ↓
AI_required             # OpenAI API calls (main_required, sub_required)
    ↓
AI_response             # Response completion handling (finish_reason, suport_system)
    ↓
AI_main                 # Entry point - run(data) orchestrates full flow
```

### Dual Conversation State
- **Main conversation** (`chat.json` via `Handle` class) - Primary user/AI dialogue
- **Sub-process** (`procces.json` via `proccesHandle` class) - API parameter extraction subprocess

### Travel API Mapping (`apps/chat/api/Map.py`)
The `API_DATA` class routes AI-extracted params to correct external APIs:
- `google_map_business` → Location search, area search
- `google_Map_Geocoding` → Address to coordinates
- `google_map_routes` → Driving route calculation

### Data Persistence (JSON Files)
| File | Handler Class | Purpose |
|------|---------------|---------|
| `main.json` | `apps/chat/data/Handle.py` | User/AI message history for UI display |
| `chat.json` | `apps/chat/api/jsonHandle.py` | OpenAI conversation state (role-based messages) |
| `procces.json` | `apps/chat/api/proccesHandle.py` | Subprocess for API param extraction |

### Adding New Travel API Integration
1. Add API config method in `apps/chat/api/config.py`:
   ```python
   def new_api(self, dmain, sub):
       self._key("new_api_key", dmain, sub)
   ```
2. Create query builder class in new file (follow `booking.py` pattern with `set_value` for constants)
3. Add mapping in `apps/chat/api/Map.py` `Datahandel.handel` dict
4. Add handler in `queryhandle.queryhandlerun()` method

## Development Commands
```bash
# Run development server
python run.py                    # Uses DEBUG env var (default: False)
DEBUG=True python run.py         # Explicit debug mode

# Docker deployment
docker-compose up --build        # Runs on port 5085 via nginx

# Production (gunicorn)
gunicorn --config gunicorn-cfg.py run:app
```

## Configuration
- Environment: Copy `env.sample` to `.env`
- Debug mode: Set `DEBUG=True` in `.env`
- Database: SQLite in debug (`apps/db.sqlite3`), MySQL/PostgreSQL in production
- Static assets: `apps/static/assets/` (SCSS in `scss/`, compiled CSS in `css/`)

## Code Patterns

### Adding New Routes
1. Create blueprint in `apps/<module>/__init__.py`:
   ```python
   from flask import Blueprint
   blueprint = Blueprint('<name>_blueprint', __name__, url_prefix='/<prefix>')
   ```
2. Add routes in `apps/<module>/routes.py`
3. Register in `apps/__init__.py` `register_blueprints()` function

### Protected Routes
All routes except login/register require `@login_required` decorator:
```python
from flask_login import login_required

@blueprint.route('/endpoint')
@login_required
def endpoint():
    ...
```

### Chat Route Pattern (`apps/chat/routes.py`)
- `POST /send_user_message` - Appends user message to `main.json`
- `POST /send_ai_message` - Appends AI response to `main.json`
- `GET /get_messages` - Returns interleaved user/AI messages for display
- `GET /chat` - Renders chat UI with message history

### Template Structure
- Base layouts: `apps/templates/layouts/base.html`, `base-fullscreen.html`
- Jinja2 blocks: `{% block title %}`, `{% block stylesheets %}`, `{% block content %}`
- Chat UI: `apps/templates/home/index.html` iterates `user_chat_data` and `ai_chat_data`

## External Dependencies
- **OpenAI**: GPT-3.5-turbo-16k model, key in `apps/chat/api/config.py` (`OpenAi.OPENAI_API_KEY`)
- **RapidAPI**: Single key for multiple providers in `API_Data.header`
  - Booking.com, TripAdvisor, Sky-Scrapper, Google Maps APIs
- **Stripe**: Payment processing in `apps/payment/routes.py`

## Important Notes
- JSON files (`main.json`, `chat.json`, `procces.json`) store runtime state - not committed
- The `@app.before_first_request` decorator in `apps/__init__.py` auto-creates DB tables
- AI uses `max_tokens=256` - responses may be truncated and require continuation loops
- Error handling: `main_error_data()` appends error message when API timeouts occur
