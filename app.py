from flask import Flask, render_template, request, url_for, flash, redirect

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

        if not title:
            flash('YouTube Link is required!')
        else:
            transcript_results.append({'title': title, 'content': 'NNN'})
            return redirect(url_for('results'))
    return render_template('yt_transcribe.html')

if __name__ == '__main__':
    app.run(debug=True)
