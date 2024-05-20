"""
Controller
"""
import os
from itertools import product
import json
from flask import Blueprint, request, current_app
from flask_cors import cross_origin
# pylint: disable=import-error, no-name-in-module
# pylint: enable=import-error, no-name-in-module
from src.api.create_pdp import pdp_policy_creation


from dotenv import load_dotenv

load_dotenv()




reports_app = Blueprint('mtek_app', __name__)

@reports_app.route('/load/data', methods=['POST'])
@cross_origin()
def load_data_into():
    """
    Creates a pdp
    """

  

   

    return load_data_into
