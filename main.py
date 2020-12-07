from flask import Flask, render_template, Response,request
import cv2
app = Flask(__name__)
video = cv2.VideoCapture(0)
import  os
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')
def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video')
def video_feed():
    global video
    return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == "__main__":
    app.run(debug=True)