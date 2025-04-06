
# Sentiment Analysis Virtual Lab

This project is a **Virtual Lab for Sentiment Analysis**, designed to help users understand and explore sentiment classification on social media texts using modern NLP techniques. It supports both **single text inputs** and **bulk file uploads (CSV)** with sentiment visualization via pie charts.

## Project Overview

This virtual lab allows students, researchers, and practitioners to:
- Understand sentiment analysis using transformer models like **BERT (RoBERTa variant)**.
- Perform real-time sentiment detection on user queries or uploaded `.csv` files.
- Visualize sentiment distribution with clear, intuitive charts.
- Learn the full NLP pipeline from text input to model inference and visualization.

## Features

- ✅ Supports `positive`, `neutral`, and `negative` sentiment detection.
- ✅ Uses `cardiffnlp/twitter-roberta-base-sentiment` for classification.
- ✅ File input via `.csv` (first column treated as input text).
- ✅ Interactive UI built with **React** and **Flask** backend.
- ✅ Auto-generated sentiment pie charts from CSV input.
- ✅ Clear feedback and result summary.

## Tech Stack

| Component     | Technology                      |
|---------------|----------------------------------|
| Frontend      | React.js, HTML/CSS              |
| Backend       | Flask (Python)                  |
| Model         | BERT via HuggingFace Transformers |
| Visualization | Matplotlib                      |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment-lab.git
cd sentiment-lab
```

### 2. Backend Setup (Python)

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

### 3. Frontend Setup (React)

```bash
cd client
npm install
npm start
```

Make sure React is running on `http://localhost:3000` and Flask on `http://localhost:5003`.

## Folder Structure

```
sentiment-lab/
├── app.py                     # Flask API for prediction
├── requirements.txt
├── /client                    # React frontend
│   ├── SentimentCheck.js
│   ├── SentimentLanding.js
│   └── ...
└── /models                    # Optional: Saved models/vectorizers
```

## Input Types

### 1. Query Text (Single)

- Type your text and click "Check Sentiment".
- Example:
  > "The river looks much cleaner after the cleanup drive."

### 2. File Input (Bulk)

- Upload `.csv` file with 1st column as input text.
- A pie chart will be displayed showing sentiment breakdown.

## Example Sentences

| Sentiment | Example |
|-----------|---------|
| Positive  | "I love the initiative to clean the river!" |
| Neutral   | "The program started last year." |
| Negative  | "The river still looks very polluted." |

## Visual Output

- Real-time prediction result for query.
- Pie chart for CSV input showing sentiment percentages.

## Future Scope

- Add more languages & multilingual models.
- Live API integration from Twitter, YouTube.
- Admin dashboard for managing uploads & results.
- Export results as PDF/DOCX reports.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Built with ❤️ for NLP learners, researchers, and data enthusiasts.
