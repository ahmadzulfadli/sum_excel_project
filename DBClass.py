from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, send_file
# objek flask
app = Flask(__name__)

# api-key
app.secret_key = "djfljdfljfnkjsfhjfshjkfjfjfhjdhfdjhdfu"

# koneksi ke database
userpass = "mysql+pymysql://nama_db:pass@"
basedir = "host"
dbname = "/excel_tools"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
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
    name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    status_transaction = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, transaction_id, sheet_name, column_name, header_number, name, address, email, status_transaction):
        self.transaction_id = transaction_id
        self.sheet_name = sheet_name
        self.column_name = column_name
        self.header_number = header_number
        self.name = name
        self.address = address
        self.email = email
        self.status_transaction = status_transaction
