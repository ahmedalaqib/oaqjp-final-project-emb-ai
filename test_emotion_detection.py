from EmotionDetection.emotion_detection import emotion_detector # Import the application
import unittest # Import unittest library

# Define a test class to test the application
class TestEmotionDetection(unittest.TestCase):

    # Define the test function
    def test_emotion_detector(self):

        # First test case
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

        # Second test case
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

        # Third test case
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

        # Fourth test case
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

        # Fifth test case
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

# Ensure this is executed directly
if __name__ == "__main__":

    # Run the test
    unittest.main()