from flask import Flask, render_template, request, url_for, flash, redirect
from transcribe import audio_to_text
from getVideos import yt_to_mp3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '3f500e5c4689bb1221d1bbc545931d898f30c1d9c2a9ad6a'

transcript_results = []
# transcript_results = [{'title': 'title', 'content': 'tran_rs'}]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/yt_transcribe/', methods=('GET', 'POST'))
def yt_transcribe():
    if request.method == 'POST':
        if 'yt_url' in request.form:
            title = request.form['yt_url']

            file_name, name = yt_to_mp3(title)
            if file_name != 0:
                tran_rs = (audio_to_text(file_name))
                transcript_results.append({'title': name, 'content': tran_rs})
                os.remove(file_name)
            else:
                flash('Error: YouTube Link is not working')
        else:
            transcript_results.clear()
        
    return render_template('yt_transcribe.html', transcript_results=transcript_results)

if __name__ == '__main__':
    app.run(debug=True)
