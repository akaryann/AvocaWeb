from flask import Flask


application = Flask(__name__, static_url_path='', static_folder="/home/avocatalk-web/website/")


@application.route("/")
def homepage():
    return application.send_static_file("HomePage.html")

