from flask import Flask, render_template, request
from transcribe import audio_to_text
from getVideos import yt_to_mp3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    youtube_url = request.form['youtube_url'] #get url
    output_path = yt_to_mp3(youtube_url) #get mp3 file path
    text_result = audio_to_text(output_path)
    return render_template('result.html', text_result=text_result)

if __name__ == '__main__':
    app.run(debug=True)
