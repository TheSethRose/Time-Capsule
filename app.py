from flask import Flask, render_template, request, jsonify
from time_capsule import TimeCapsule  # Import your main TimeCapsule class

app = Flask(__name__)
time_capsule = TimeCapsule()  # Initialize your TimeCapsule object

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_memory', methods=['POST'])
def add_memory():
    data = request.json
    # Call your TimeCapsule method to add a memory
    result = time_capsule.add_memory(data['text'])
    return jsonify({'success': result})

@app.route('/retrieve_memories', methods=['GET'])
def retrieve_memories():
    # Call your TimeCapsule method to retrieve memories
    memories = time_capsule.retrieve_memories()
    return jsonify(memories)

if __name__ == '__main__':
    app.run(debug=True)
