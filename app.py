from flask import Flask, request, jsonify
from model import CodeGenerator

app = Flask(__name__)
generator = CodeGenerator()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data.get('text')
    max_length = int(data.get('max_length'))

    prediction = generator.predict(text, max_length)
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
