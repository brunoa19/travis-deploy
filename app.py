from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "CI integration"

if __name__ == "__main__":
    app.run()
