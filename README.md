# SW Todo List App (Flask)

## 📄 Description
A Flask web application to create, manage, and delete todo list activities.


## Acknowledgements

Special thanks to [@alexroel] for their excellent course and guidance.

## 🚀 Technologies Used

- Python
- Flask
- SQLite
- Jinja2

## ⚙️ How to run
🖥️
python -m venv env-todo
source env-todo/bin/activate  # Linux/Mac
env-todo\Scripts\activate     # Windows
pip install -r requirements.txt
python run.py


## 📁 Folder Structure
sw-todo-list-app-flask/
├── env-todo/
├── instance/
├── todor/
	├── templates/ 
		├── auth/
			├── login.html
			├── register.html				
		├── todo/
			├── create.html
			├── index.html
			├── update.html
		├── base.html
		├── index.html
	├── auth.py
	├── models.py
	├── todo.py
	├── __init__.py
├── .gitignore
├── README.md
├── requirements.txt
├── run.py