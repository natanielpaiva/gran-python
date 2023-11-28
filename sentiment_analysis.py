from nltk.sentiment import SentimentIntensityAnalyzer  # Importa o SentimentIntensityAnalyzer do NLTK

def analyze_sentiment(texto):
    # Define uma função chamada 'analyze_sentiment' que recebe um texto como argumento

    sia = SentimentIntensityAnalyzer()  # Cria uma instância do SentimentIntensityAnalyzer
    pontuacao = sia.polarity_scores(texto)  # Calcula os scores de polaridade para o texto

    # Avalia o score composto para determinar o sentimento do texto:
    if pontuacao['compound'] >= 0.05:
        # Se o score composto for maior ou igual a 0.05, o texto é considerado positivo
        return "Positive"
    elif pontuacao['compound'] <= -0.05:
        # Se o score composto for menor ou igual a -0.05, o texto é considerado negativo
        return "Negative"
    else:
        # Se o score composto estiver entre -0.05 e 0.05, o texto é considerado neutro
        return "Neutral"
