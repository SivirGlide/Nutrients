from flask import Flask

app = Flask(__name__)
@app.route("/")
def landingPage():
    return "<p>Welcome to my page!<p>"

@app.route("/signup")
def signup():
    pass

@app.route("/signin")
def signin():
    pass

@app.route("/dashboard")
def dashboard():
    pass

if __name__ == "__main__":
    app.run(debug=False)