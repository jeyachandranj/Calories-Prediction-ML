from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the Hugging Face model for text generation
generator = pipeline("text-generation", model="distilgpt2")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_calories', methods=['POST'])
def generate_calories():
    if request.method == 'POST':
        try:
            prompt_text = request.form['prompt']

            generated_info = generator(prompt_text, max_length=100, num_return_sequences=1)[0]['generated_text']
            
            return jsonify({'generated_info': generated_info})

        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
