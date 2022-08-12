"""
构建 uwsgi 服务
1、下载 Python 支持 uwsgi 插件
    pip install uwsgi
2、编写响应程序 service.py
3、启动服务
    uwsgi --http :9090 --wsgi-file uwsgi/service.py
4、测试服务
    curl http://127.0.0.1:9090

"""


def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Hello World"]
