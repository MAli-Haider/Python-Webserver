from flask import Flask, render_template, Response
import cv2
import threading

app = Flask(__name__)

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
camera2 = cv2.VideoCapture(4,cv2.CAP_DSHOW)
camera3 = cv2.VideoCapture(2,cv2.CAP_DSHOW)
camera4 = cv2.VideoCapture(3,cv2.CAP_DSHOW)

def record1():
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('videos/output1.avi',fourcc, 20.0, (640,480))
    while(camera.isOpened()):
        ret, frame = camera.read()
        if ret==True:
            out.write(frame)
        else:
            break

def record2():
    camera = cv2.VideoCapture(4,cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('videos/output2.avi',fourcc, 20.0, (640,480))
    while(camera.isOpened()):
        ret, frame = camera.read()
        if ret==True:
            out.write(frame)
        else:
            break

def record3():
    camera = cv2.VideoCapture(2,cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('videos/output3.avi',fourcc, 20.0, (640,480))
    while(camera.isOpened()):
        ret, frame = camera.read()
        if ret==True:
            out.write(frame)
        else:
            break

def record4():
    camera = cv2.VideoCapture(3,cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('videos/output4.avi',fourcc, 20.0, (640,480))
    while(camera.isOpened()):
        ret, frame = camera.read()
        if ret==True:
            out.write(frame)
        else:
            break
        
    
def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
    
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    
def gen_frames2():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera2.read()
    
  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    
def gen_frames3():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera3.read()
    
  # read the camera frame
        if not success:
            break
        else:
        
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

def gen_frames4():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera4.read()
  # read the camera frame
        if not success:
            break
        else:

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames2(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames3(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed4')
def video_feed4():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames4(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/record1')
def record1():
    return record1()

@app.route('/record2')
def record2():
    return record2()
    
@app.route('/record3')
def record3():
    return record3()

@app.route('/record4')
def record4():
    return record4()


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')