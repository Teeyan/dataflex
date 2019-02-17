from flask import Flask, render_template, jsonify, request, json, session, send_file
from flask_cors import CORS
from datamanagement import DataManagement
from pathlib import Path
import pandas as pd
import os

app = Flask(__name__)
CORS(app)


@app.route('/init', methods=['GET'])
def initiate():
	"""
	Initial Instantiation of our Application. Creat the DM state and return json of attr.
	"""
	file_name = request.args['upload']
	header_file = request.args['header']
	dm = DataManagement.from_file(filename=file_name,header_file=header_file)
	Path('./dm.pkl').touch()
	dm.data.to_pickle("./dm.pkl")
	return dm.get_labels()


@app.route('/meta', methods=['GET'])
def metadata():
	"""
	Return metadata w.r.t the specified attribute
	"""
	attr = request.args["attr"]
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	return dm.retrieve_metadata(attr)


@app.route('/view', methods=['GET'])
def view_values():
	"""
	Return the actual values of the attributes in a key/value dict
	"""
	attr_list = request.args.getlist("attr")
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	return dm.view_values(attr_list)


@app.route('/normalize', methods=['GET'])
def normalize():
	"""
	Normalize the column attribute specified
	"""
	attr = request.args["attr"]
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	dm.normalize(attr)
	os.remove("./dm.pkl")
	dm.data.to_pickle("./dm.pkl")
	return ('', 204)


@app.route('/fill', methods=['GET'])
def fill_null():
	"""
	Fill in null values based on method and default if applicable
	"""
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	attr = request.args["attr"]
	method = request.args.get("method")
	default = "0"
	if method == "default":
		request.args.get("default")
	dm.fill_in_missing(attr, method, default)
	os.remove("./dm.pkl")
	dm.data.to_pickle("./dm.pkl")
	return ('', 204)


@app.route('/correlate', methods=['GET'])
def correlate():
	"""
	Return correlation matrix with json of dict of attr to list of its values in 
	attr_list order.
	"""
	attr_list = request.args.getlist("attr")
	method = request.args.get("method")
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	return dm.correlation_matrix(attr_list, method)


@app.route('/drop', methods=['GET'])
def drop():
	"""
	Drop the specified attribute from the dataframe
	"""
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	attr = request.args["attr"]
	dm.drop_attr(attr)
	os.remove("./dm.pkl")
	print(dm.data)
	dm.data.to_pickle("./dm.pkl")
	return ('', 204)


@app.route("/save", methods=['GET'])
def save():
	"""
	Save dataframe as a csv to the filename
	"""
	dm = DataManagement.from_pkl(pd.read_pickle("./dm.pkl"))
	filename = request.args["filename"]
	dm.data.to_csv(filename)
	return send_file(filename)


if __name__ == "__main__":
	app.debug = True
	app.run(port=8000, host="0.0.0.0", debug=True)
