import os
import re
from flask import Flask, render_template, request, current_app
from helper import get_files

app = Flask(__name__) 

app = Flask(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='static'
)

path_to_movies = '../movies_for_media_server'
files = get_files(path_to_movies)['The Last Of Us.2022.S01.WEB-DL.1080p']

@app.route("/")
def home():
    return render_template("player.html")


@app.route("/video/<int:index>", methods=["GET"])
def video(index):
    if index < 0 or int(index) > len(files) - 1:
        return current_app.response_class(status=400)

    headers = request.headers
    if not "range" in headers:
        return current_app.response_class(status=400)

    video_path = os.path.abspath(os.path.join(path_to_movies, files[index]))
    size = os.stat(video_path)
    size = size.st_size

    chunk_size = (10 ** 6) * 3 #1000kb makes 1mb * 3 = 3mb (this is based on your choice)
    start = int(re.sub("\\D", "", headers["range"]))
    end = min(start + chunk_size, size - 1)

    content_lenght = end - start + 1

    def get_chunk(video_path, start, chunk_size):
        with open(video_path, "rb") as f:
            f.seek(start)
            chunk = f.read(chunk_size)
        return chunk

    headers = {
        "Content-Range": f"bytes {start}-{end}/{size}",
        "Accept-Ranges": "bytes",
        "Content-Length": content_lenght,
        "Content-Type": "video/mp4",
    }

    return current_app.response_class(get_chunk(video_path, start,chunk_size), 206, headers)


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8000, debug=True)
    app.run(host="0.0.0.0", port=8800, debug=True)