from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import math

app = Flask(__name__)

# Initialize DB
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')
    conn.close()

init_sqlite_db()

@app.route('/')
def index():
    search_query = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = 5  # Users per page

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Count total users
    if search_query:
        cursor.execute("SELECT COUNT(*) FROM users WHERE name LIKE ? OR email LIKE ?", 
                       (f"%{search_query}%", f"%{search_query}%"))
    else:
        cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    total_pages = math.ceil(total_users / per_page)

    # Get paginated users
    offset = (page - 1) * per_page
    if search_query:
        cursor.execute("SELECT * FROM users WHERE name LIKE ? OR email LIKE ? LIMIT ? OFFSET ?", 
                       (f"%{search_query}%", f"%{search_query}%", per_page, offset))
    else:
        cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (per_page, offset))

    users = cursor.fetchall()
    conn.close()

    return render_template("index.html", 
                           users=users, 
                           page=page, 
                           total_pages=total_pages, 
                           search_query=search_query)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        user = cursor.fetchone()
        conn.close()
        return render_template("update.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)
