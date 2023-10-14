from flask import render_template, request, jsonify
from apps.chat import blueprint
from apps.chat.data.Handle import append_data, load_data
from flask_login import login_required


@blueprint.route('/send_user_message', methods=['GET','POST'])
@login_required
def send_user_message():
    if request.method == 'POST':
        chat_data = request.form.get('message')
        append_data("user", chat_data)
        chat_data = load_data()
        user_messages = chat_data.get("user", {})
        ai_messages = chat_data.get("ai", {})
        return jsonify({'status': 'success', 'user_messages': user_messages, 'ai_messages': ai_messages})

@blueprint.route('/get_messages',  methods=['GET','POST'])
@login_required
def get_messages():
    chat_data = load_data()
    user_messages = chat_data.get("user", {})
    ai_messages = chat_data.get("ai", {})
    messages = []
    for i in range(max(len(user_messages), len(ai_messages))):
        user_message = user_messages.get(str(i), '')
        ai_message = ai_messages.get(str(i), '')
        messages.append(("User", user_message))
        messages.append(("AI", ai_message))
    return jsonify({'messages': messages})

@blueprint.route('/chat', methods=['GET','POST'])
@login_required
def chat():
    chat_data = load_data()
    user_messages = chat_data.get("user", {})
    ai_messages = chat_data.get("ai", {})
    return render_template("home/index.html", user_chat_data=user_messages, ai_chat_data=ai_messages)

@blueprint.route('/send_ai_message',  methods=['GET','POST'])
@login_required
def send_ai_message():
    if request.method == 'POST':
        chat_data = request.form.get('message')
        append_data("ai", chat_data)
        chat_data = load_data()
        user_messages = chat_data.get("user", {})
        ai_messages = chat_data.get("ai", {})
        return jsonify({'status': 'success', 'user_messages': user_messages, 'ai_messages': ai_messages})
