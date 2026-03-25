from flask import Flask, render_template, request
import os
import numpy as np
from SqDetector import contourDetection
import cv2

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        photo = request.files['photo']
        chemin = os.path.join('uploads', photo.filename)
        photo.save(chemin)
        # img = cv2.imread(chemin)
        base_img = cv2.imread( chemin, cv2.IMREAD_UNCHANGED)
        h,w,c = base_img.shape
        width = 512 # specify new width
        scale_f = width/w
        height = h*scale_f
        base_img = cv2.resize(base_img, (int(width),int(height)))
        # cv2.imshow("Img", img)
        _, _, nbr = contourDetection(base_img)
        print("Nombre de carre est : ", nbr)
        return render_template("index.html", succes="Enoye avec succes")
    else:
        return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['photo']
    photo.save(os.path.join('uploads', photo.filename))
    return 'Photo reçue !', 200


if __name__ == "__main__":
    os.makedirs('uploads', exist_ok=True)
    app.run(host="0.0.0.0", port=5050, debug=True)
