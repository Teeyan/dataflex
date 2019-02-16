from flask import Flask, render_template
#from flask_cors import CORS 		# if we need cross-domain

app = Flask(__name__)
#CORS(app)

@app.route("/")
def home():
	# home page
	return render_template("home.html")

@app.route("/scoob")
def scoob():
	# like SCOOB!
	pass

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=2000)