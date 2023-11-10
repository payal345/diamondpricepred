from flask import Flask
app = Flask(__name__)

@app.route("/")
def data():
    return "welcome to GeekForGeeks"

@app.route("/GFK")
def index():
     return "'Welcome to GeeksforGeeks Python world.!!'"
  


if __name__ == "__main__":
    app.run()