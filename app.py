<<<<<<< HEAD
from flask import Flask, render_template, request, url_for, flash, redirect
=======
from flask import Flask, render_template, request
from transcribe import audio_to_text
from getVideos import yt_to_mp3
>>>>>>> a353e09dcb462926c4e0bcd63e06422fbf978971

app = Flask(__name__)
app.config['SECRET_KEY'] = '3f500e5c4689bb1221d1bbc545931d898f30c1d9c2a9ad6a'

transcript_results = [{'title': 'FUCK YOU', 'content': 'NNN'}]

@app.route('/')
def home():
    return render_template('home.html')

<<<<<<< HEAD
@app.route('/results/')
def results():
    return render_template('transcripts.html', messages=transcript_results)

@app.route('/yt_transcribe/', methods=('GET', 'POST'))
def yt_transcribe():
    if request.method == 'POST':
        title = request.form['yt_url']

        if not title:
            flash('YouTube Link is required!')
        else:
            transcript_results.append({'title': title, 'content': 'NNN'})
            return redirect(url_for('results'))
    return render_template('yt_transcribe.html')
=======
@app.route('/process_url', methods=['POST'])
def process_url():
    youtube_url = request.form['youtube_url'] #get url
    output_path = yt_to_mp3(youtube_url) #get mp3 file path
    text_result = audio_to_text(output_path)
    return render_template('result.html', text_result=text_result)
>>>>>>> a353e09dcb462926c4e0bcd63e06422fbf978971

if __name__ == '__main__':
    app.run(debug=True)
