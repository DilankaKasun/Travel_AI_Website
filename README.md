    # Travel AI Website

    ## Annexure C2-5 (Private Project 3)

    | Field | Details |
    |-------|---------|
    | **Project Title** | Travel AI Website |
    | **Client** | Chaminda Lakmal (Internal Project) |
    | **Client Address/Contact** | - |
    | **Year** | 2025 |
    | **Project Value** | - |

    ### Short Description
    A Flask-based travel AI application that integrates OpenAI and third-party travel APIs to help users plan trips efficiently through an intelligent chat interface. The system provides conversational trip planning, real-time travel data from multiple providers, user authentication, content generation tools, and payment processing capabilities.

    ### Technologies Used
    | Category | Technology |
    |----------|------------|
    | Backend | Flask 2.0.2, SQLAlchemy 1.4.29, Flask-Login 0.5.0 |
    | AI/ML | OpenAI GPT-3.5-turbo-16k |
    | External APIs | RapidAPI (Booking.com, TripAdvisor, Google Maps) |
    | Database | SQLite (Development), MySQL/PostgreSQL (Production) |
    | Frontend | Jinja2 3.0.2, Bootstrap 5, SCSS |
    | Payment Gateway | Stripe |
    | Deployment | Docker, Nginx, Gunicorn 20.1.0 |
    | Other | Flask-Migrate, Flask-WTF, Flask-Minify |

    ### Outcome/Deliverable
    - Fully functional AI-powered travel planning chatbot
    - Integration with multiple travel data providers (hotels, restaurants, locations)
    - User authentication and account management system
    - Content generation tools (Article Generator, Blog Writer, Email Generator, CV Builder)
    - Stripe payment integration for premium features
    - Docker containerized deployment with Nginx reverse proxy
    - Responsive web interface with Bootstrap 5

    ### Contact Person for Verification
    - **Author**: Dilanka Kasun
    - **Repository**: [github.com/DilankaKasun/Travel_AI_Website](https://github.com/DilankaKasun/Travel_AI_Website)

    ---

    ## Attached Proofs

    ### Screenshots
    *(Screenshots of the application interface can be added here)*

    - Login/Registration Page
    - AI Chat Interface
    - Content Generation Tools
    - Payment Page

    ---

    ## Technical Documentation

    ## Features

    - **AI-Powered Chat Interface** - Conversational trip planning using GPT-3.5-turbo-16k
    - **Travel API Integration** - Real-time data from Booking.com, TripAdvisor, Google Maps
    - **User Authentication** - Secure login/registration with Flask-Login
    - **Content Generation Tools** - Article generator, blog writer, email generator, and more
    - **Payment Integration** - Stripe checkout for premium features
    - **Responsive Design** - Bootstrap 5 with custom SCSS styling

    ## Tech Stack

    | Category | Technology |
    |----------|------------|
    | Backend | Flask, SQLAlchemy, Flask-Login |
    | AI/ML | OpenAI GPT-3.5-turbo-16k |
    | APIs | RapidAPI (Booking.com, TripAdvisor, Google Maps) |
    | Database | SQLite (dev), MySQL/PostgreSQL (prod) |
    | Frontend | Jinja2, Bootstrap 5, SCSS |
    | Payments | Stripe |
    | Deployment | Docker, Nginx, Gunicorn |

    ## Installation

    ### Prerequisites
    - Python 3.9+
    - pip

    ### Setup

    1. **Clone the repository:**
        ```bash
        git clone https://github.com/DilankaKasun/Travel_AI_Website.git
        cd Travel_AI_Website
        ```

    2. **Create virtual environment:**
        ```bash
        python -m venv venv
        source venv/bin/activate  # Linux/Mac
        venv\Scripts\activate     # Windows
        ```

    3. **Install dependencies:**
        ```bash
        pip install -r requirements.txt
        ```

    4. **Configure environment:**
        ```bash
        cp env.sample .env
        ```
        Edit `.env` and set your API keys:
        ```
        DEBUG=True
        SECRET_KEY=your-secret-key
        ```

    5. **Run the application:**
        ```bash
        python run.py
        ```

    6. **Access the website:**
        Open your browser and go to `http://localhost:5000`

    ## Docker Deployment

    ```bash
    # Build and run with Docker Compose
    docker-compose up --build

    # Access at http://localhost:5085
    ```

    ## Project Structure

    ```
    Travel_AI_Website/
    ├── run.py                 # Application entry point
    ├── apps/
    │   ├── __init__.py        # App factory (create_app)
    │   ├── config.py          # Configuration classes
    │   ├── authentication/    # User auth (login, register)
    │   ├── chat/              # AI chat system
    │   │   ├── routes.py      # Chat endpoints
    │   │   ├── api/           # OpenAI & travel API integrations
    │   │   │   ├── openAI.py  # Core AI orchestration
    │   │   │   ├── config.py  # API keys & headers
    │   │   │   ├── Map.py     # Google Maps integration
    │   │   │   ├── booking.py # Booking.com queries
    │   │   │   └── tripadvisor.py
    │   │   └── data/          # JSON data handlers
    │   ├── home/              # Main pages
    │   ├── tool/              # Content generation tools
    │   ├── payment/           # Stripe integration
    │   ├── static/assets/     # CSS, JS, images
    │   └── templates/         # Jinja2 templates
    ├── docker-compose.yml
    ├── Dockerfile
    └── requirements.txt
    ```

    ## API Configuration

    ### Required API Keys

    1. **OpenAI API Key** - For GPT chat functionality
    2. **RapidAPI Key** - For travel data APIs:
    - Booking.com
    - TripAdvisor
    - Google Maps (Local Business Data, Geocoding, Routes)
    3. **Stripe API Key** - For payment processing

    Configure keys in `apps/chat/api/config.py` or use environment variables.

    ## Usage

    ### Chat Interface
    1. Register/Login to your account
    2. Navigate to the chat page
    3. Ask travel-related questions:
    - "Find hotels in Paris for next weekend"
    - "What are the best restaurants near the Eiffel Tower?"
    - "Plan a 3-day trip to Tokyo"

    ### Content Tools
    Access various AI writing tools at `/tool?name=<tool-name>`:
    - Article Generator
    - Blog Post Writer
    - Email Generator
    - Report Generator
    - CV Builder

    ## Development

    ### Running in Debug Mode
    ```bash
    DEBUG=True python run.py
    ```

    ### Production with Gunicorn
    ```bash
    gunicorn --config gunicorn-cfg.py run:app
    ```

    ### Database
    - Debug mode uses SQLite (`apps/db.sqlite3`)
    - Production uses MySQL/PostgreSQL (configure in `.env`)

    ## Contributing

    1. Fork the repository
    2. Create a feature branch (`git checkout -b feature/amazing-feature`)
    3. Commit your changes (`git commit -m 'Add amazing feature'`)
    4. Push to the branch (`git push origin feature/amazing-feature`)
    5. Open a Pull Request

    ## License

    This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

    ## Contact

    - **Author**: Dilanka Kasun
    - **Repository**: [github.com/DilankaKasun/Travel_AI_Website](https://github.com/DilankaKasun/Travel_AI_Website)
