import requests # Import the requests library
import json # Import the JSON library

def emotion_detector(text_to_analyze): # Define a function that takes a string input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL for Emotion Detection
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Headers to be sent with the request
    obj = { "raw_document": { "text": text_to_analyze } } # Data to be analyzed
    response = requests.post(url, json = obj, headers = header) # Request to the Emotion Detection service
    formatted_response = json.loads(response.text) # Convert json into Python dictionary
    emotions = formatted_response["emotionPredictions"][0]["emotion"] # Extract emotions with scores
    dominant_emotion = max(emotions, key = emotions.get) # Extract the dominant emotion
    emotions["dominant_emotion"] = dominant_emotion # Add the dominant emotion to the emotions
    return emotions # Return the response text