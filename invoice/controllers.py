from flask import Flask
from http import HTTPStatus
from flask import jsonify, request, render_template, Blueprint
import json
from db.models import Customer, Invoice
from dbo import get_invoices_for_customers

invoice = Blueprint( 'invoice', __name__ )


@invoice.route( "/api/v1/invoices", methods=['GET'] )
def get_invoices():
    return jsonify( get_invoices_for_customers() )


def fetch_invoices():
    invoices = []
    result = get_invoices_for_customers()
    for i in result:
        invoices.append( i.to_json() )
    return invoices
