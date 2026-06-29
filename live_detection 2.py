import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# Load model
model = load_model("keras_model.h5", compile=False)

# Load labels
with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera could not be opened!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to PIL Image
    image = Image.fromarray(rgb)

    # Resize image
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # Convert to numpy array
    image_array = np.asarray(image)

    # Normalize image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Prepare input
    data = np.expand_dims(normalized_image_array, axis=0)

    # Prediction
    prediction = model.predict(data, verbose=0)

    index = np.argmax(prediction)
    confidence = prediction[0][index]

    # Remove "0 " or "1 " from label
    label = class_names[index].split(" ", 1)[1]

    # Display result
    text = f"{label} ({confidence*100:.2f}%)"

    cv2.putText(frame, text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Waste Classification", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()