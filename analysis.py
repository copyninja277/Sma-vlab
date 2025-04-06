from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # For headless environments (no GUI)
import matplotlib.pyplot as plt
from io import BytesIO

# Initialize app and config
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size
CORS(app)

# Load BERT model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Map labels from model to readable sentiments
label_map = {
    "LABEL_0": "negative",
    "LABEL_1": "neutral",
    "LABEL_2": "positive"
}

@app.route('/predict-sentiment', methods=['POST'])
def predict_sentiment():
    data = request.json
    text = data.get('text', '')

    result = classifier(text)[0]
    sentiment = label_map.get(result['label'], 'unknown')
    confidence = round(result['score'], 3)

    return jsonify({'sentiment': sentiment, 'confidence': confidence})

@app.route('/predict-from-file', methods=['POST'])
def predict_from_file():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    try:
        df = pd.read_csv(file)
        texts = df.iloc[:, 0].dropna().astype(str).tolist()

        predictions = [classifier(text)[0]['label'] for text in texts]
        mapped_preds = [label_map[pred] for pred in predictions]

        sentiment_counts = pd.Series(mapped_preds).value_counts().reindex(['positive', 'neutral', 'negative'], fill_value=0)

        # Generate pie chart
        fig, ax = plt.subplots()
        colors = ['#00C49F', '#FFBB28', '#FF4D4F']  # green, yellow, red
        ax.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title('Sentiment Distribution')
        plt.axis('equal')

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        buf.seek(0)
        plt.close()

        return send_file(buf, mimetype='image/png', download_name='sentiment_piechart.png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5003)
