from flask import Flask, send_from_directory, make_response

app = Flask(__name__)

def send_file_with_headers(filename, mimetype=None):
    resp = make_response(send_from_directory('.', filename, mimetype=mimetype))
    # Разрешаем встраивание в iframe (обязательно для Jira Cloud)
    resp.headers['X-Frame-Options'] = 'ALLOWALL'
    resp.headers['Content-Security-Policy'] = "frame-ancestors *"
    return resp

@app.route('/atlassian-connect.json')
def descriptor():
    return send_file_with_headers('atlassian-connect.json', mimetype='application/json')

@app.route('/index.html')
def index():
    return send_file_with_headers('index.html', mimetype='text/html')

@app.route('/')
def root():
    # Перенаправляем корень на index.html (удобно для проверки)
    return send_file_with_headers('index.html', mimetype='text/html')

@app.route('/status')
def status():
    return "OK"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # Railway передаёт PORT
    app.run(host="0.0.0.0", port=port)
