from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return 'server start'


@app.route('/post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        # Get JSON data from the request
        data = request.get_json()
        # Return the received data as a JSON response
        return jsonify(data)  # Use jsonify to ensure proper JSON formatting

if __name__ == '__main__':
    app.run('0.0.0.0', port = 8090, debug = True)
