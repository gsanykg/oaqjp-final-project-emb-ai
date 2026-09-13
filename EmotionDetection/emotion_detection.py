import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
    max_key = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = max_key
    formatted_json = json.dumps(emotion, indent=4, ensure_ascii=False)
    return formatted_json

#if __name__ == "__main__":
 #   emotion_detector("Я радий")    
