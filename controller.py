"""
Controller
"""
import os
from itertools import product
import json
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import pandas as pd
import psycopg2 as pg
from psycopg2.extras import execute_values
import time
# pylint: disable=import-error, no-name-in-module
# pylint: enable=import-error, no-name-in-module
from src.api.insert_data_inputs import insert_data


from dotenv import load_dotenv

load_dotenv()

conn = pg.connect(dbname='data_pipeline_presentation_example',
                          host='localhost',
                          user='postgres',
                          password='password',
                 port ='5433')


reports_app = Blueprint('mtek_app', __name__)

@reports_app.route('/load/data', methods=['POST'])
@cross_origin()
def load_data_into():
   """
    Gets data and inserts to a warehouse
    """
   json_data = request.get_json()
   print(json_data)
   if not json_data:
        return jsonify({'error': 'No JSON data provided'}), 400
   for key, value in json_data.items():
        print(f"Key: {key}, Value: {value}")
        insert_data(conn,json_data)
        return jsonify({'message': 'Data received successfully'}), 200
