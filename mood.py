def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ["happy", "excited", "great", "good", "fun", "joy"]):
        return "😊 Happy"
    elif any(word in text for word in ["sad", "upset", "depressed", "cry", "tired"]):
        return "😔 Sad"
    elif any(word in text for word in ["angry", "mad", "furious", "annoyed"]):
        return "😠 Angry"
    elif any(word in text for word in ["love", "grateful", "thankful", "blessed"]):
        return "😍 Loved"
    else:
        return "😐 Neutral"
