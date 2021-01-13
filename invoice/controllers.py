from flask import Flask
from http import HTTPStatus
from flask import jsonify, request, render_template, Blueprint
import json
from db.models import Customer, Invoice

invoice = Blueprint('invoice', __name__)


