from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Replace this with your actual API key
load_dotenv()  # Load from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return 'AutoFixer AI backend is running with GPT!'

@app.route('/autofixer', methods=['POST'])
def autofixer():
    data = request.get_json()
    zap_name = data.get('zap_name', '')
    error_msg = data.get('error_message', '').strip()

    if not error_msg:
        return jsonify({"suggestion": "No error message provided."})

    # Construct the prompt
    prompt = f"""You are an expert DevOps assistant. Analyze the following error message and provide a short, actionable suggestion to fix it:
    
    Error: {error_msg}

    Response:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for debugging software issues."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.4
        )

        suggestion = response.choices[0].message.content.strip()
        return jsonify({"suggestion": suggestion})

    except Exception as e:
        print("Error from OpenAI:", e)
        return jsonify({"suggestion": "Failed to generate suggestion. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)
