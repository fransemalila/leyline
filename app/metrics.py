from flask import Blueprint

metrics_blueprint = Blueprint('metrics', __name__)

@metrics_blueprint.route('/metrics')
def metrics():
    return 'Prometheus metrics available at /metrics', 200
