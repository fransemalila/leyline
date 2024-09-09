from flask import Blueprint, request, jsonify
import socket
import validators
from app.models import QueryLog
from app.database import db

api_blueprint = Blueprint('api', __name__, url_prefix='/v1/tools')

# Resolve IPv4 address for a given domain
@api_blueprint.route('/lookup', methods=['POST'])
def lookup():
    data = request.get_json()
    domain = data.get('domain')
    try:
        ipv4 = socket.gethostbyname(domain)
        log = QueryLog(domain=domain, ipv4=ipv4)
        db.session.add(log)
        db.session.commit()
        return jsonify({'domain': domain, 'ipv4': ipv4}), 200
    except socket.gaierror:
        return jsonify({'error': 'Invalid domain name'}), 400

# Validate if the input is an IPv4 address
@api_blueprint.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    ip = data.get('ip')
    if validators.ipv4(ip):
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 400

# Retrieve the latest 20 saved queries
@api_blueprint.route('/history', methods=['GET'])
def history():
    logs = QueryLog.query.order_by(QueryLog.created_at.desc()).limit(20).all()
    return jsonify([{'domain': log.domain, 'ipv4': log.ipv4, 'timestamp': log.created_at} for log in logs]), 200
