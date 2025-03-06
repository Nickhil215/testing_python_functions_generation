from flask import Request

def hello_world(request: Request):
    request_json = request.get_json(silent=True)

    if request_json and "name" in request_json:
        return f"Hello, {request_json['name']}!"
    else:
        return "Hello, World!"
