import re
from collections import Counter


POSITIVE_WORDS = {
    "happy", "good", "great", "excellent", "amazing",
    "awesome", "love", "like", "wonderful", "fantastic",
    "joy", "excited", "success", "best", "beautiful",
    "enjoy", "enjoyed", "fun", "positive"
}

NEGATIVE_WORDS = {
    "sad", "bad", "terrible", "hate", "angry",
    "upset", "worst", "awful", "horrible", "lonely",
    "stress", "stressed", "anxiety", "anxious",
    "worried", "fear", "failed", "failure", "negative"
}

EMOTIONS = {
    "Happy": {
        "happy", "joy", "excited", "great", "awesome",
        "wonderful", "love", "fun"
    },

    "Sad": {
        "sad", "unhappy", "lonely", "cry", "upset"
    },

    "Angry": {
        "angry", "mad", "furious", "annoyed", "hate"
    },

    "Anxious": {
        "anxiety", "anxious", "worried", "nervous",
        "stress", "stressed", "fear"
    }
}


def tokenize(text):

    return re.findall(r"\b[a-zA-Z]+\b", text.lower())


def analyze_text(text):

    words = tokenize(text)

    word_count = len(words)

    unique_words = len(set(words))

    positive_count = sum(
        1 for word in words
        if word in POSITIVE_WORDS
    )

    negative_count = sum(
        1 for word in words
        if word in NEGATIVE_WORDS
    )

    if positive_count > negative_count:
        sentiment = "Positive 😊"

    elif negative_count > positive_count:
        sentiment = "Negative 😔"

    else:
        sentiment = "Neutral 😐"

    emotion_scores = {}

    for emotion, emotion_words in EMOTIONS.items():

        score = sum(
            1 for word in words
            if word in emotion_words
        )

        emotion_scores[emotion] = score

    if max(emotion_scores.values()) == 0:
        emotion = "Neutral"

    else:
        emotion = max(
            emotion_scores,
            key=emotion_scores.get
        )

    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "positive_words": positive_count,
        "negative_words": negative_count,
        "sentiment": sentiment,
        "emotion": emotion,
        "emotion_scores": emotion_scores
    }


def most_common_words(text, count=5):

    words = tokenize(text)

    stop_words = {
        "the", "is", "a", "an", "and", "or",
        "to", "of", "in", "on", "for", "i",
        "am", "it", "this", "that", "my",
        "me", "you", "are"
    }

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return Counter(filtered_words).most_common(count)