from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'AutoFixer AI backend is running!'

@app.route('/autofixer', methods=['POST'])
def autofixer():
    data = request.get_json()
    zap_name = data.get('zap_name', '')
    error_msg = data.get('error_msg', '')


    # Dummy AI logic – You can enhance this!
    if "401" in error_msg or "unauthorized" in error_msg.lower():
        suggestion = "Check your API credentials. The token may be missing or expired."
    elif "404" in error_msg or "not found" in error_msg.lower():
        suggestion = "Verify the endpoint URL. It may be incorrect or unavailable."
    elif "parse" in error_msg.lower():
        suggestion = "Check network connection or server load. Try increasing timeout settings."
    else:
        suggestion = "This error needs manual review or more logs.."


    return jsonify({"suggestion": suggestion})

if __name__ == "__main__":
    app.run(debug=True)
