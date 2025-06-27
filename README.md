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
![Screenshot 2025-06-27 145257](https://github.com/user-attachments/assets/ee78856c-ef88-4306-9ac0-c40f4fcdd9e2)

![Screenshot 2025-06-27 145413](https://github.com/user-attachments/assets/2b4aa01d-25ec-4b4a-9bfd-3bc9c348dcbb)

![Screenshot 2025-06-27 151926](https://github.com/user-attachments/assets/a0577f58-285e-42bc-bd8a-8ccc99e7cb16)

![Screenshot 2025-06-27 151942](https://github.com/user-attachments/assets/26dbc07f-4992-4d71-969f-80a261a330f9)

![Screenshot 2025-06-27 154948](https://github.com/user-attachments/assets/9963893f-14a8-4db6-92bd-1ed514404ff0)

![Screenshot 2025-06-27 155034](https://github.com/user-attachments/assets/9b23dbbf-3670-457b-a657-88ac3ce82353)

![Screenshot 2025-06-27 155044](https://github.com/user-attachments/assets/9eb510ce-b573-4718-a102-c66a04da387f)

![Screenshot 2025-06-27 155210](https://github.com/user-attachments/assets/141b6361-5ccf-49f4-95a0-7833f4064778)


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
