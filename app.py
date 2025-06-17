from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'AutoFixer AI backend is running!'

@app.route('/autofixer', methods=['POST'])
def autofixer():
    data = request.get_json()
    zap_name = data.get('zap_name', '')
    error_msg = data.get('error_message', '')

    # Dummy AI logic – You can enhance this!
    if "401" in error_msg:
        suggestion = "Check your API credentials. The token may be missing or expired."
    elif "404" in error_msg:
        suggestion = "Verify the endpoint URL. It may be incorrect or unavailable."
    else:
        suggestion = "This error needs manual review or more logs."

    return jsonify({"suggestion": suggestion})

if __name__ == "__main__":
    app.run(debug=True)
