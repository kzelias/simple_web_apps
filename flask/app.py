from flask import Flask

app = Flask(__name__)

@app.route("/")
def health():
    return {'status': 'ok'}, 200