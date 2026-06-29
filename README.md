# Waste_Classification
Waste Classification Using Deep Learning project for classifying recyclable and non-recyclable waste .
## 📌 Project Description
This project is a Deep Learning-based waste classification system that identifies waste as **Recyclable** or **Non-Recyclable** using a webcam. The model was trained using Google Teachable Machine and integrated into Python using TensorFlow.

## 🎯 Objective
The objective of this project is to classify waste correctly and promote proper waste management and recycling.

## 🗂️ Dataset
- Dataset Source: Kaggle
- Total Images: 6500+
- Classes:
  - Recyclable
  - Non-Recyclable

## ⚙️ Project Workflow
1. Downloaded the waste image dataset from Kaggle.
2. Uploaded the dataset to Google Teachable Machine.
3. Created two classes:
   - Recyclable
   - Non-Recyclable
4. Trained the model using Teachable Machine.
5. Exported the trained TensorFlow model (`keras_model.h5`) and `labels.txt`.
6. Installed Python 3.10 in Visual Studio Code.
7. Installed the required libraries:
   - TensorFlow
   - Keras
   - OpenCV
   - NumPy
   - Pillow
8. Downloaded the TensorFlow code from Teachable Machine.
9. Ran the project in Visual Studio Code.
10. The webcam captures waste images and predicts whether they are Recyclable or Non-Recyclable.

## 🛠️ Technologies Used
- Python 3.10
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pillow
- Google Teachable Machine
- Visual Studio Code

## 📂 Project Files
```
Waste-Classification/
│── keras_model.h5
│── labels.txt
│── main.py
│── requirements.txt
│── README.md
```

## ▶️ How to Run
1. Install Python 3.10.
2. Install the required libraries:
   ```bash
   pip install tensorflow opencv-python numpy pillow
   ```
3. Run the project:
   ```bash
   python main.py
   ```
4. Show a waste object to the webcam.
5. The model will display whether the waste is **Recyclable** or **Non-Recyclable**.
## 📄 License
This project is developed for educational purposes.
