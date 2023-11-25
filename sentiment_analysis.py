
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(texto):
    sia = SentimentIntensityAnalyzer()
    pontuacao = sia.polarity_scores(texto)
    if pontuacao['compound'] >= 0.05:
        return "Positive"
    elif pontuacao['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"
   
