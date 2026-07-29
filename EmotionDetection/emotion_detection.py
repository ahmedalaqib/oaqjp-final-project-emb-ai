import requests # Import the requests library
import json # Import the JSON library

# Define a function that takes a string input
def emotion_detector(text_to_analyze):
    
    # URL for Emotion Detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers to be sent with the request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Data to be analyzed
    obj = { "raw_document": { "text": text_to_analyze } }
    
    # Request to the Emotion Detection service
    response = requests.post(url, json = obj, headers = header)

    # If the status code is 400, all key values are None
    if response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # If the status code is 200, extract keys from the response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"] # Extract emotions with scores
        dominant_emotion = max(emotions, key = emotions.get) # Extract the dominant emotion
        emotions["dominant_emotion"] = dominant_emotion # Add the dominant emotion to the emotions
    
    # Return the emotions
    return emotions