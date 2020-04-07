from flask import Flask, render_template
from api import mark
from api import get
from controller import errorHandler
import os

frontEndDir = os.path.join("frontend", "flask-mark-12306-captcha-frontend", "build")

app = Flask(__name__, static_url_path='', static_folder=frontEndDir)
app.register_blueprint(errorHandler)
app.register_blueprint(mark)
app.register_blueprint(get)


@app.route('/')
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
