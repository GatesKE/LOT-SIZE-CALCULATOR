from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "This is the home page"


if __name__ == '_main_':
    app.run(debug=True, port=8000)