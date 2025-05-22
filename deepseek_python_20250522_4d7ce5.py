from flask import Flask, send_file
import youtube_dl

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    ydl_opts = {'format': 'bestvideo[ext=mp4]'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f'https://youtu.be/{url}', download=False)
        return send_file(requests.get(info['url']).content, mimetype='video/mp4')