from flask import Flask
application = Flask(__name__)

@application.route('/')
def index():
    return application.send_static_file("index.html")