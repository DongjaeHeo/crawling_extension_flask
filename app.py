from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Server started'

@app.route('/post', methods=['POST'])
def handle_post():
    # Ensure there is data in the request
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    return jsonify(data)  # Return the JSON data received

if __name__ == '__main__':
    app.run('0.0.0.0', port=8090, debug=True)
