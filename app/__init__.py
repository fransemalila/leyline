from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from app.api import api_blueprint
from app.metrics import metrics_blueprint
from app.database import init_db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app, path='/metrics')

# Register blueprints
app.register_blueprint(api_blueprint)
app.register_blueprint(metrics_blueprint)

# Initialize the database
init_db(app)

# Health check endpoint
@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

# Root endpoint providing version, date, and Kubernetes detection
@app.route('/')
def root():
    import time
    import os
    
    current_time = int(time.time())
    is_kubernetes = os.getenv('KUBERNETES_SERVICE_HOST') is not None
    
    return {
        'version': '0.1.0',
        'date': current_time,
        'kubernetes': is_kubernetes
    }, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
