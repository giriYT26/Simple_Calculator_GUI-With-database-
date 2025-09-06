# 🧮 Simple_GUI_Calculator_With_database

A simple GUI-based calculator built using **Python (Tkinter + CustomTkinter)** with a **MySQL database integration** to store and manage calculation history.  

This project allows users to:  
- Perform basic arithmetic operations (`+`, `-`, `*`, `/`).  
- Save calculations automatically into a MySQL database.  
- View and clear past calculation history.  
- Securely connect to a MySQL server via a login GUI.  

---

## 📂 Project Structure
```
.
├── Main.py               # Entry point - Calculator GUI and logic
├── MYSQL_CONNECTION.py   # MySQL login and database setup handler
├── background_img.jpeg   # Background image for login window
```

---

## 🚀 Features
- **Login System**: Connect to your MySQL server with host, username, and password.  
- **Database Setup**: Automatically creates a database `calculator1_db` and table `calculations`.  
- **History Management**: View all past calculations or clear the history.  
- **Keyboard Support**: Enter numbers and operators directly from the keyboard.  
- **User-Friendly UI**: Built with `Tkinter` and styled using `CustomTkinter`.  

---

## ⚙️ Requirements
Make sure you have the following installed:

- Python 3.8+  
- MySQL Server  
- Required Python packages:
  ```bash
  pip install mysql-connector-python customtkinter pillow
  ```

---

## ▶️ Usage
1. Start the application:
   ```bash
   python Main.py
   ```
2. Enter your MySQL credentials in the login window.  
3. Once connected, the calculator will open.  
4. Perform calculations and check your history.  

---

## 🗄️ Database
- Database name: **`calculator1_db`**  
- Table name: **`calculations`**  

| Column    | Type           | Description                |
|-----------|----------------|----------------------------|
| `id`      | INT, AUTO INC  | Unique identifier          |
| `equation`| VARCHAR(225)   | The input equation         |
| `result`  | VARCHAR(225)   | The result of the equation |

---

## 📸 Screenshot
Login Window (with background image):  
*(The `background_img.jpeg` is used as the login screen background.)*  

<img width="597" height="476" alt="image" src="https://github.com/user-attachments/assets/be81b37e-26e6-4814-af5c-440cf2077fc5" />
<img width="669" height="483" alt="image" src="https://github.com/user-attachments/assets/4b4c2375-94c4-4a46-9304-cb7e5b911010" />
<img width="497" height="525" alt="image" src="https://github.com/user-attachments/assets/82c5c066-d67e-45d6-a43e-08d8ecf18c50" />
<img width="1000" height="530" alt="image" src="https://github.com/user-attachments/assets/964b6195-7675-4901-aaf1-3d65fe644eb1" />
<img width="1002" height="529" alt="image" src="https://github.com/user-attachments/assets/dd4ba670-b1c1-43ea-a416-6640aae7f31a" />
<img width="1000" height="530" alt="image" src="https://github.com/user-attachments/assets/6e4f2765-d882-4721-b051-1af6f05ba888" />

---

## 👨‍💻 Author
**S Giridharan**  

---  
