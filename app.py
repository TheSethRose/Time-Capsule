# Main Flask application file for the Time Capsule project

from flask import Flask, render_template, request, jsonify
from time_capsule import TimeCapsule  # Import the main TimeCapsule class

app = Flask(__name__)
time_capsule = TimeCapsule()  # Initialize the TimeCapsule object

@app.route('/')
def index():
    # Render the main page
    return render_template('index.html')

@app.route('/add_memory', methods=['POST'])
def add_memory():
    # Handle adding a new memory
    data = request.json
    # Call TimeCapsule method to add a memory
    result = time_capsule.add_memory(data['text'])
    return jsonify({'success': result})

@app.route('/retrieve_memories', methods=['GET'])
def retrieve_memories():
    # Handle retrieving memories
    # Call TimeCapsule method to retrieve memories
    memories = time_capsule.retrieve_memories()
    return jsonify(memories)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
