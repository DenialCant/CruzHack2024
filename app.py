from flask import Flask, render_template, request, url_for, flash, redirect
from transcribe import audio_to_text
from getVideos import yt_to_mp3

app = Flask(__name__)
app.config['SECRET_KEY'] = '3f500e5c4689bb1221d1bbc545931d898f30c1d9c2a9ad6a'

transcript_results = [{'title': 'FUCK YOU', 'content': 'NNN'}]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results/')
def results():
    return render_template('transcripts.html', transcript_results=transcript_results)

@app.route('/yt_transcribe/', methods=('GET', 'POST'))
def yt_transcribe():
    if request.method == 'POST':
        title = request.form['yt_url']

        # file_name = yt_to_mp3(title)
        # file_name
        # tran_rs = (audio_to_text(file_name))

        if not title:
            flash('YouTube Link is required!')
        else:
            transcript_results.append({'title': title, 'content': 'tran_rs'})
            return redirect(url_for('results'))
    return render_template('yt_transcribe.html')

if __name__ == '__main__':
    app.run(debug=True)
