import json

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code, {"Content-Type": "application/json"}

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code, {"Content-Type": "application/json"}
