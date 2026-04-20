from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import create_agent
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize agent
print("Initializing Supermarket AI Assistant...")
agent = create_agent()
print("Agent ready!")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_message = data['message']
    print(f"User: {user_message}")
    
    try:
        response = agent.run(user_message)
        print(f"Bot: {response}")
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
