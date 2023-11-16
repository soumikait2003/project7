from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import base64

app = Flask(__name__)

def encode_image(image):

    return base64.b64encode(image)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

   

        # You can process the image here if needed

    encoded_image = encode_image(file)

    return render_template('result.html', encoded_image=encoded_image)

if __name__ == '__main__':
    app.run(debug=True)
