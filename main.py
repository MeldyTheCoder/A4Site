import config
from flask import Flask, render_template, abort
from video_parser import VideoParser

app = Flask(__name__, template_folder=config.templates_path, static_folder=config.static_path)
vp = VideoParser()

@app.route('/', methods=["GET", "POST"])
@app.route('/main/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/videos/', methods=["GET", "POST"])
def videos():
    try:
        videos = vp.get_videos()
        return render_template('videos.html', videos=videos)
    except Exception as e:
        print(e)
        return abort(500)

@app.route('/bio', methods=["GET", "POST"])
def bio():
    return render_template('bio.html')

@app.route('/view_video/<video_id>/')
def view_video(video_id: str):
    try:
        video_data = vp.get_video(video_id)
        return render_template('video.html', video=video_data)
    except Exception as e:
        print(e)
        return abort(500)

@app.errorhandler(404)
def error_404(*args, **kwargs):
    return render_template('error404.html'), 404

@app.errorhandler(500)
def error_500(*args, **kwargs):
    return render_template('error500.html'), 500


app.run(debug=True)