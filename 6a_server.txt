from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("emotionDetector")

@app.route("/emotionDetector")
def res_emotion_detector():
    query = request.args.get('q')
    res_dic = emotion_detector(query)
    res = 'For the given statement, the system response is '
    result = res + ", ".join(f"'{key}': {value}" for key, value in list(res_dic.items())[:-1])
    result = result + '. The dominant emotion is ' + str(res_dic['dominant_emotion'])+"."
    return str(result)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)