from flask import Flask, send_from_directory

app = Flask(__name__)

# Отдаём App descriptor
@app.route('/atlassian-connect.json')
def descriptor():
    return send_from_directory('.', 'atlassian-connect.json')

# Отдаём страницу с кнопкой
@app.route('/index.html')
def index():
    return send_from_directory('.', 'index.html')

# Проверка, что сервер работает
@app.route('/status')
def status():
    return "OK"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
resp.headers['X-Frame-Options'] = 'ALLOWALL'
resp.headers['Content-Security-Policy'] = "frame-ancestors *"
