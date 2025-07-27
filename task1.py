from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity

if __name__ == "__main__":
    user_input = input("Enter text for sentiment analysis: ")
    sentiment, polarity = analyze_sentiment(user_input)
    print(f"Sentiment: {sentiment}")
    print(f"Polarity Score: {polarity}")
