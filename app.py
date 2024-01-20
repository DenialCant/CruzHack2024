from flask import Flask, render_template, request
from transcribe import download_audio, audio_to_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    youtube_url = request.form['youtube_url']
    output_path = "path/to/downloaded/audio.mp3"
    # download_audio(youtube_url, output_path)
    text_result = audio_to_text(output_path)
    return render_template('result.html', text_result=text_result)

if __name__ == '__main__':
    app.run(debug=True)
