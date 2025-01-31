from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, send_file
from dotenv import load_dotenv
from sqlalchemy.sql import func
import os

# objek flask
app = Flask(__name__)

load_dotenv()

# Akses variabel dari file .env
env = os.getenv("FLASK_ENV")

# Load environment variables based on the 'env' argument
if env == 'production':
    load_dotenv('.env.production')
elif env == 'testing':
    load_dotenv('.env.testing')
else:  # Default to development
    load_dotenv('.env.development')

# configurasi app
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Table
class SumExcelTransactions(db.Model):
    __tablename__ = 'sum_excel_transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(100), nullable=True)
    sheet_name = db.Column(db.String(100), nullable=True)
    column_name = db.Column(db.Text, nullable=True)
    header_number = db.Column(db.Integer, nullable=True)
    columns_formula = db.Column(db.String(100), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    status_transaction = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, transaction_id, sheet_name, column_name, header_number, name, address, email, status_transaction, columns_formula):
        self.transaction_id = transaction_id
        self.sheet_name = sheet_name
        self.column_name = column_name
        self.header_number = header_number
        self.columns_formula = columns_formula
        self.name = name
        self.address = address
        self.email = email
        self.status_transaction = status_transaction

class SumExcelComment(db.Model):
    __tablename__ = 'sum_excel_comment'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    comment = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, email, comment):
        self.name = name
        self.email = email
        self.comment = comment

class SumExcelParameterUi(db.Model):
    __tablename__ = 'sum_excel_parameter_ui'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def get_parameter_max_id():
        return db.session.query(SumExcelParameterUi).order_by(SumExcelParameterUi.id.desc()).first()