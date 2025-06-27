# 🧠 OMR Sheet Checker by ML Model (CNN)

A machine learning–based web application for checking OMR (Optical Mark Recognition) answer sheets using a Convolutional Neural Network (CNN) model. The app detects filled and blank bubbles and compares them with the answer key to calculate scores.

---

## 🚀 Features

- 🟤 Detect filled vs blank OMR bubbles using image processing
- 🧠 Predict bubble fill status using a trained CNN model
- 📷 Upload scanned OMR sheets via a web interface (Django)
- 📝 Automatically generate a 2D matrix representing answers
- ✅ Compare student answers with correct answers and calculate results

---
## 🖼️ Demo
![Screenshot 2025-06-27 145257](https://github.com/user-attachments/assets/a05529cd-fa5e-4e93-b2c8-f5f06f7ae3ac)

![Screenshot 2025-06-27 145413](https://github.com/user-attachments/assets/780c1503-df52-4a69-a5c0-bc18c412eee0)

![Screenshot 2025-06-27 151926](https://github.com/user-attachments/assets/c5333883-d631-4431-8342-712bf4c4d1a0)

![Screenshot 2025-06-27 151942](https://github.com/user-attachments/assets/05f2c082-7f3d-4638-b53d-e23ab6c8ef14)

![Screenshot 2025-06-27 154948](https://github.com/user-attachments/assets/2a4fb719-fa5e-4ad3-99b7-ddd8a0f50016)

![Screenshot 2025-06-27 155034](https://github.com/user-attachments/assets/3a31daa8-039a-4db0-951b-965f8fbb3a1f)

![Screenshot 2025-06-27 155044](https://github.com/user-attachments/assets/9fe5ac6d-a782-4906-a981-ff1253a13958)

![Screenshot 2025-06-27 155210](https://github.com/user-attachments/assets/d143667d-9fab-4bd7-b987-15fc5fc3a2e8)

---

## 📂 Project Structure

OMR-Sheet-Checker-by-ML-Model-CNN/

│

├── omrChecker/ # Django app

│ ├── models.py # Image upload and database logic

│ ├── views.py # Main logic and predictions

│ ├── templates/ # HTML templates

│
├── omrmodel.py # CNN model architecture and Script to train the CNN

├── media/ # Uploaded OMR images

├── db.sqlite3 # Django database (local only)

├── .gitignore # Git ignore list

├── manage.py # Django runner

└── README.md


## 📸 How It Works
User uploads a scanned OMR sheet.

The system extracts and processes bubble regions using OpenCV.

Each bubble is passed through a trained CNN model.

A 2D matrix is generated (1 = filled, 0 = blank).

Compared with an answer key to calculate score.

Results displayed on the web UI.

## 🧠 Model Training
Training dataset: cropped bubble images (blank and filled)

Model: Convolutional Neural Network (CNN)

library: Torch , Torchvision , cv2 , numpy , matplotlib , math ,etc.

Trained model is saved and loaded during prediction

## 🛠️ Built With
🐍 Python

🎨 OpenCV , Torch , Torchvision , cv2 , numpy , matplotlib , math ,etc.

🌐 Django

🧪 HTML + Bootstrap

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clonehttps://github.com/priyamghorui/OMR-Sheet-Checker-by-ML-Model-CNN.git
cd OMR-Sheet-Checker-by-ML-Model-CNN
```
2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**

```bash
Install Dependencies
pip install -r requirements.txt
```
4. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Run the Server**

```bash
python manage.py runserver
```
# Thank You
