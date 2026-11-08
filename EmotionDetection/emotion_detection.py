import requests

def emotion_detector(text_to_analyze):
    """
    Detect emotions using the Watson NLP Emotion Predict function.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    return response.text

import json

def emotion_predictor(response_text):
    """
    Extract emotion scores and identify the dominant emotion.
    """
    result = json.loads(response_text)
    emotions = result['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    emotions['dominant_emotion'] = dominant_emotion

    return emotions
