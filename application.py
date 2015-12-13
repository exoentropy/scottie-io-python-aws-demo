from flask import Flask, request, url_for, jsonify
from boto.s3.key import Key
import boto
import boto.s3.connection
import uuid


application = Flask(__name__)

@application.route("/data/", methods = ["POST"])
def data():
	try:
		data = request.form["data"]
		connection = boto.connect_s3()
		#update with your S3 bucket name here
		bucket_name = "test"
		bucket = connection.get_bucket(bucket_name, validate = False)
		key = Key(bucket)
		guid = uuid.uuid4()
		key.key = guid
		key.set_contents_from_string(data)
		key.make_public()
		return jsonify({"status" : "success"}), 201
	except Exception as exception:
		return jsonify({"status" : "error", "message" : str(exception)}), 500

if __name__ == "__main__":
    application.run()
    