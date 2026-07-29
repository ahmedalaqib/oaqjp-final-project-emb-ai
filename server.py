from flask import Flask, render_template, request # Import necessary modules from flask
from EmotionDetection.emotion_detection import emotion_detector # Import Emotion Detection application

# Creating flask object
app = Flask("Emotion Detection")

# Method to be executed for the route '/emotionDetector'
@app.route('/emotionDetector')
def emotion_detect():
    # Retrieve the text to analyze
    text_to_analyze = request.args.get("textToAnalyze")

    # Storing the response of the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Extracting emotion scores
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    
    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Return the output
    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

# Method to be executed for the route '/'
@app.route("/")
def render_index_page():
    # Return the index page
    return render_template("index.html")

# Run the server
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)