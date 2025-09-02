from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import chromadb

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call this API

# Connect to existing Chroma collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="career_data")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '').strip()

    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Query Chroma for top 3 documents
    results = collection.query(query_texts=[question], n_results=3)
    context = "\n".join([doc for doc in results['documents'][0]])

    # Build prompt for Ollama
    full_prompt = f"""Context:
{context}

Question: {question}
Answer as a personalized career and skills advisor:"""

    # Call Ollama LLaMA 2 model
    result = subprocess.run(
        ['ollama', 'run', 'personal-advisor', full_prompt],
        capture_output=True,
        text=True
    )

    return jsonify({"answer": result.stdout.strip()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
