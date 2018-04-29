from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello my World! for the second time"

if __name__ == '__main__':
    app.run(debug=True)
