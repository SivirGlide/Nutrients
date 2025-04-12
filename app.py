from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<p>Welcome to my page!<p>"