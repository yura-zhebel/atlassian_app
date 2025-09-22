from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/atlassian-connect.json')
def descriptor():
    return send_from_directory('.', 'atlassian-connect.json')

@app.route('/index.html')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
