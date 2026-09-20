# Student Task Manager

A simple and responsive web-based task management application built using Python, Flask, HTML, CSS, JavaScript, and SQLite.

The application allows students to create, organize, update, search, filter, and track their daily tasks through a simple web interface.

## Features

- Add new tasks
- Edit existing tasks
- Delete tasks with confirmation
- Mark tasks as completed or pending
- Set task priority
- Set task due dates
- Search tasks
- Filter tasks by priority
- Filter tasks by status
- View total, completed, and pending task counts
- Responsive user interface
- Persistent task storage using SQLite
- Completed task visual status

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- SQLite
- Git
- GitHub

## Project Structure

```
student-task-manager/
├── database/
│   └── tasks.db
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   ├── index.html
│   └── edit.html
├── app.py
├── README.md
└── requirements.txt 
```

## Application Architecture
```text
User
  ↓
HTML / CSS / JavaScript
  ↓
Flask Backend
  ↓
SQLite Database
```

## Task Management Workflow

```text
Create Task
     ↓
Store Task in SQLite
     ↓
Display Task
     ↓
Search / Filter / Update
     ↓
Mark Complete or Delete
```

## Future Improvements

- User authentication and login
- Task categories
- Task sorting
- Notifications and reminders
- REST API
- MongoDB integration
- Cloud deployment
- Dashboard with task statistics
- Calendar-based task management

## Learning Outcomes

- Python programming
- Flask web development
- CRUD operations
- SQLite database integration
- HTML and CSS development
- JavaScript DOM manipulation
- Backend and frontend integration
- Form handling
- Database queries
- Responsive web design
- Debugging and problem solving

## How to Run

### 1. Create a Virtual Environment

```bash
python -m venv venv
```
### 2. Activate the Virtual Environment
For Windows:  
```bash 
python venv\Scripts\activate
```
For macOS/Linux: 
```bash 
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
python app.py
```
### 5. Open the Application
Open browser and visit:  
`http://127.0.0.1:5000`

### 6. Stop the Application
Press:
Ctrl + C

### 7. Deactivate the Virtual Environment
deactivate


## Author
**Aakanchha Singh**

B.Tech Computer Science & Engineering  
Dr. B. C. Roy Engineering College, Durgapur

GitHub: `aakanchhasinghofficial-cloud`