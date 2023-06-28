from flask import Flask, request, jsonify
from model import CodeGenerator

app = Flask(__name__)
# Use a global variable to store the model so it's not loaded every time.
generator = {} 

@app.route('/predict', methods=['POST'])
def predict():
    global generator
    data = request.get_json(force=True)

    # Error handling for missing or invalid data
    if 'text' not in data or not isinstance(data['text'], str):
        return jsonify({'error': 'Missing or invalid "text" field.'}), 400
    if 'max_length' not in data or not isinstance(data['max_length'], int) or data['max_length'] < 1:
        return jsonify({'error': 'Missing or invalid "max_length" field.'}), 400
    if 'max_token_length' not in data or not isinstance(data['max_token_length'], int) or data['max_token_length'] < 1:
        return jsonify({'error': 'Missing or invalid "max_token_length" field.'}), 400
    model = ''
    if 'model' not in data:
        model = 'Salesforce/codegen-2B-mono'
    else:
        model = data['model']

    # If the model hasn't been loaded yet, load it now.
    if model not in generator:
        print("Loading model...")
        generator[model] = CodeGenerator(model)
        print("Loading model end")

    text = data['text']
    max_length = data['max_length']
    max_token_length = data['max_token_length']

    # Model performance monitoring
    import time
    start_time = time.time()

    generator_res = generator[model].predict(text, max_length, max_token_length)

    elapsed_time = time.time() - start_time
    print(f"Prediction took {elapsed_time} seconds.")

    return jsonify({'prediction': generator_res['prediction'], 'use_time': elapsed_time, 'text': generator_res['text'], 'model': model})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
