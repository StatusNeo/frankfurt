from flask import jsonify
import boto3
from boto3.dynamodb.conditions import Key

# Define Flask route for handling API requests
def frankfurt_handler():
    # Convert start_time and end_time to ISO 8601 format for DynamoDB query
    start_time = '1698667995705'
    end_time = '1698667995708'
    symbol = 'EURUSD'
    table_name = 'tr-jpk-ticks'
    # Define the DynamoDB resource
    dynamodb = boto3.client('dynamodb', aws_access_key_id="", aws_secret_access_key="",  region_name='')


    try:
        # Define a filter expression based on the desired condition
        filter_expression = '#symbol = :symbol AND #time_msc BETWEEN :start_time_msc AND :end_time_msc'

        # Define attribute names and values
        expression_attribute_names = {
            '#symbol': 'symbol',
            '#time_msc': 'time_msc'
        }
        expression_attribute_values = {
            ':symbol': {'S': symbol},
            ':start_time_msc': {'N': start_time},
            ':end_time_msc': {'N': end_time}
        }

        # Perform a Scan operation with the filter expression
        response = dynamodb.scan(
            TableName=table_name,
            FilterExpression=filter_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        print(response)
        items = response.get('Items', [])
        return jsonify(items)

    except Exception as e:
        print(f"Error querying DynamoDB: {e}")
        return jsonify([])
    return jsonify([])



