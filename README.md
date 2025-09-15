# 📝 Simple CRUD Application (Flask + SQLite)

This is a simple **CRUD (Create, Read, Update, Delete)** web application built using **Flask** and **SQLite**.  
It allows you to manage users by adding, viewing, updating, and deleting records through a web interface.

---

## 🚀 Features
- Add new users with name and email
- View all users in a list
- Update existing user details
- Delete users
- Lightweight backend with Flask
- SQLite database for easy setup (no external dependencies)

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Frontend**: HTML (Jinja2 templates)

---

## 📂 Project Structure
```
crud_app/
│── app.py # Main Flask app
│── database.db # SQLite database (auto-created on first run)
│── requirements.txt # Dependencies
│── templates/ # HTML templates
│ ├── index.html
│ └── update.html
```
---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Gyanvii/crud_app.git
cd crud_app
```
### 2. Create a virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the app
```
python app.py
```

6. Open in browser

Go to [👉 http://127.0.0.1:5000](http://127.0.0.1:5000)


📜 License

This project is licensed under the MIT License.


---
