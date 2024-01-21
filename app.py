from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from transcribe import audio_to_text, download_notes
from getVideos import yt_to_mp3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '3f500e5c4689bb1221d1bbc545931d898f30c1d9c2a9ad6a'

transcript_results = []
#transcript_results = [{'title': 'title', 'content': 'tran_rs'}]

@app.route('/')
def home():
    transcript_results.clear();
    return render_template('home.html')

name = ""
tran_rs = ""

@app.route('/yt_transcribe/', methods=('GET', 'POST'))
def yt_transcribe():
    global name, tran_rs

    if request.method == 'POST':
        if 'yt_url' in request.form:
            title = request.form['yt_url']

            file_name, name = yt_to_mp3(title)
            if file_name != "":
                tran_rs = audio_to_text(file_name)
                transcript_results.append({'title': name, 'content': tran_rs})
                try:
                    os.remove(file_name)
                finally:
                    print("File DOE")
            else:
                flash('Error: YouTube Link is not working')
        else:
            if 'return_code' in request.form:
                transcript_results.clear()
            elif 'download_code' in request.form:
                download_file()

    return render_template('yt_transcribe.html', transcript_results=transcript_results)

@app.route('/download')
def download_file():
    # title = "Sample Title"
    # body = "This is the body of the text file."
    global name, tran_rs
    content = f"{name}\n\n{tran_rs}"

    with open(name + '.txt', 'w') as file:
        file.write(content)

    return send_file(name + '.txt', as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
