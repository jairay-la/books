from flowise import Flowise  # assuming there's a Flowise Python API
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Flowise
flowise = Flowise()

# Load the flow from JSON
with open('flow/book_report_chatflow.json', 'r') as file:
    flow_json = file.read()
flowise.load_flow(flow_json)

@app.route('/api/process', methods=['POST'])
def process():
    # This is a placeholder for how you might process data with your flow
    data = request.json
    result = flowise.process(data)  # Assume there's a process method in Flowise
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
