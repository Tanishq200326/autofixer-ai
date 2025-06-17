from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")  # Switched from gemini-pro to gemini-1.5-flash

@app.route('/')
def index():
    return 'AutoFixer AI backend is running with Gemini 1.5 Flash!'

@app.route('/autofixer', methods=['POST'])
def autofixer():
    data = request.get_json()
    zap_name = data.get('zap_name', '')
    error_msg = data.get('error_message', '').strip()

    if not error_msg:
        return jsonify({"suggestion": "No error message provided."})

    prompt = f"""You are an expert DevOps assistant. Analyze the following error message and provide a short(in 1-2 lines), actionable suggestion to fix it:

Error: {error_msg}

Response:"""

    try:
        response = model.generate_content(prompt)
        suggestion = response.text.strip()
        return jsonify({"suggestion": suggestion})

    except Exception as e:
        print("Error from Gemini:", e)
        return jsonify({"suggestion": "Failed to generate suggestion. Please try again later."})

# Optional test route to check if generation is working directly
@app.route('/test')
def test_generation():
    try:
        response = model.generate_content("How do I fix a 404 error in an API?")
        return jsonify({"test_response": response.text.strip()})
    except Exception as e:
        print("Test error:", e)
        return jsonify({"error": "Test failed."})

if __name__ == "__main__":
    app.run(debug=True)
