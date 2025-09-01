from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/api/advice', methods=['POST'])
def get_advice():
    data = request.json
    user_query = data.get('query', '')
    
    # Call Ollama with subprocess (assuming 'llama2' model installed)
    result = subprocess.run(
        ["ollama", "run", "llama2", user_query],
        capture_output=True,
        text=True
    )

    return jsonify({
        "response": result.stdout.strip()
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
