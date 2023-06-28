# Code Generation API

This is a simple Flask-based API for generating code using a transformer model.

## Installation

Make sure you have Python 3.7 or later installed. Then, install the required dependencies:

```bash
pip install flask transformers
```

## Usage

First, start the server:

```bash
python app.py
```

The server will start on `0.0.0.0:8088`.

You can then send POST requests to the `/predict` endpoint. The request should be a JSON object with the following fields:

- `text` (string): The initial text that you want to extend.
- `max_length` (integer): The maximum length of the generated code. This is a positive integer that represents the number of tokens to generate.

For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "def hello():", "max_length": 5}' http://localhost:8088/predict
```

This will return a JSON object with a `prediction` field that contains the generated code.

## Monitoring

The server will print the time it takes to generate a prediction. This can be used for performance monitoring.

## Error Handling

The server includes basic error handling. If a request is missing a field or a field is of the wrong type, the server will return a 400 status code and a JSON object with an `error` field describing the problem.

## Caching

The model and tokenizer are loaded when the first request is made and are then cached for future requests. This improves the performance of subsequent requests.

## Model

The default model is `Salesforce/codegen-2B-mono`, but you can change this by modifying the `model` argument when instantiating the `CodeGenerator` class.