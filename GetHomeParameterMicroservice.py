from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-parameters', methods=['GET'])
def get_parameters():
    # Retrieve relevant home parameters (simplified for illustration)
    parameters = {'temperature': 20, 'user_preferences': {'eco_mode': True}}
    return jsonify(parameters)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
