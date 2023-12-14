# app.py
from flask import Flask
from routers.route import health_check_bp

app = Flask(__name__)

# Đăng ký Blueprint cho route health check
app.register_blueprint(health_check_bp)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
