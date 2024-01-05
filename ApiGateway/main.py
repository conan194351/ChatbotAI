from flask import Flask
from flask_cors import CORS
from routers.route import routers

app = Flask(__name__)

# Đăng ký Blueprint cho route health check
app.register_blueprint(routers)

# Bật CORS cho tất cả các routes trên ứng dụng Flask
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
