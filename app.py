from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import os

app = Flask(__name__)

model = load_model("models/deteksi_retak_model.h5")

def preprocess_image(filepath):
    img = Image.open(filepath)
    img = img.convert("L")                 # grayscale
    img = img.resize((128, 128))           # sesuai input model
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=-1)   # (128,128,1)
    img_processed = np.expand_dims(img_array, axis=0)  # (1,128,128,1)
    return img_processed

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        file = request.files["image"]
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        img_processed = preprocess_image(filepath)

        pred = model.predict(img_processed)[0][0]

        if pred > 0.5:
            prediction = f"Retak Terdeteksi ({pred*100:.2f}% confidence)"
        else:
            prediction = f"Tidak Retak ({(1-pred)*100:.2f}% confidence)"

        return render_template("index.html", prediction=prediction, image_path=filepath)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
