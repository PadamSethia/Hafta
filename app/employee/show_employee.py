from flask import Blueprint, render_template
from flask import render_template, redirect, url_for, request, session, jsonify
from flask_login import login_required
from app.employee import bp
from app.employee.model import Employee, EmployeeSchema, EmployeeBasicSchema , EmployeeMainSchema
from app.master.model import Company ,CompanySchema
from app import db


@bp.route('/', methods=['GET'])
@login_required
def show_employee():
    return render_template('employees/index.html')


@bp.route('/get/detail/<id>', methods=['POST'])
def get_detail(id):
    if request.method == 'POST':
        data_schema = EmployeeSchema()
        data = Employee.query.filter_by(id=int(id)).first()
        # print(data_schema)
        json_data = data_schema.dumps(data)
        print(json_data)
        return jsonify(json_data)


@bp.route('/get/basic', methods=['GET'])
def get_basic():
    if request.method == 'GET':
        data_schema = EmployeeBasicSchema(many=True)
        data = Employee.query.all()
        # print(data_schema)
        json_data = data_schema.dumps(data)
        print(json_data)
        return jsonify(json_data)


@bp.route('/get/by/company/<companyid>', methods=['GET'])
def get_by_company(companyid):
    if request.method == 'GET':
        # compna = Company.query.filter_by(id= int(companyid)).first().name
        employee_schema = EmployeeMainSchema(many=True)
        data = Employee.query.filter(Employee.company.any(Company.id == int(companyid)) ).all()
        print(data)
        # data = Company.query.filter_by(name=str(companyname)).first().emp_company
        # print(test[0].post)
        json_data = employee_schema.dumps(data)
        print(json_data)
        return jsonify(json_data)