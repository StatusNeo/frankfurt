from flask import Flask, jsonify
from src import *
import boto3

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index_page():
    return frankfurt_handler()

@app.route('/list_tables', methods=['GET'])
def list_dynamodb_tables():
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb', aws_access_key_id="", aws_secret_access_key="",  region_name='eu-central-1')
    try:
        # Use the list_tables method to retrieve a list of all DynamoDB tables in your AWS account
        response = dynamodb.list_tables()
        table_names = response['TableNames']
        return jsonify(table_names)
    except Exception as e:
        return str(e), 500

if __name__=='__main__':
    app.run(debug=True)