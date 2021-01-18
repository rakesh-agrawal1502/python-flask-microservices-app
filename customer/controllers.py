from flask import Flask
from http import HTTPStatus
from flask import jsonify, request, render_template, Blueprint
import json
from db.models import Customer, Invoice
from dbo import select_customers, insert_customer_with_invoices

customer = Blueprint('customer', __name__)


@customer.route( "/api/v1/customer", methods=['GET'] )
def get_customers():
    return jsonify( fetch_customers() )


@customer.route( "/api/v1/customer", methods=['POST'] )
def insert_customer():
    invoices = []
    # print("Input: ", request.data) JSON String
    # Covert JSON String to JSON object
    input_json = json.loads( request.data )

    for invoice in input_json["invoices"]:
        amount = invoice["amount"]
        invoices.append( Invoice( invoice["amount"] ) )
    cust = Customer( input_json["name"], input_json["address"], input_json["email"], invoices )
    insert_customer_with_invoices( cust )
    message = "Success Customer Name: " + str( cust.id )
    return message, HTTPStatus.OK


def fetch_customers():
    customers = []
    for c in select_customers():
        customers.append( c.to_json() )
    return customers
