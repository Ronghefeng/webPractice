from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<span style='color:red'>I am app 1</span>"


# Nginx 下启动 uwsgi 服务:
# uwsgi --socket 127.0.0.1:3031 --wsgi-file uwsgi/flask_service.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
