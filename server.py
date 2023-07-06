from flask import Flask, render_template, url_for

APP = Flask(__name__)

@APP.route('/')
def index():
	return render_template("index.html")


@APP.route('/about')
def about():
	return render_template("about.html")


# Using data from URL sample

@APP.route('/user/<string:name>/<int:ID>')
def user(name, ID):
	return f"User profile<br><br>Name: {name}, id: {str(ID)}"




if __name__ == '__main__':
	APP.run(debug=True)