from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Aseem! Happy Makar Sankranti"

if __name__ == "__main__":
    app.run()