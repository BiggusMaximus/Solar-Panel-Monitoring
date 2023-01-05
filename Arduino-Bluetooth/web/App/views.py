from flask import Blueprint, render_template, Response, jsonify, send_file
from .data import *

views = Blueprint('views', __name__)                 

@views.route('/')
def home():
    get_data()
    return render_template('home.html', data=data)

@views.route('/update', methods=["GET"])
def update():
    return jsonify(get_data())

@views.route('/download', methods=["GET"])
def download():
    file_path = '../../data.xlsx'
    return send_file(file_path, as_attachment=True)

