# To-Do List Application

A simple yet functional **To-Do List Application** implemented in Python with both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** using `PySimpleGUI`. The project demonstrates clean, modular design, file handling, and real-time updates.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Demo](#demo)
8. [Future Enhancements](#future-enhancements)

---

## Overview
This project allows users to manage their daily tasks efficiently by providing options to add, edit, complete, and display tasks. The tasks are persistently stored in a `todos.txt` file. The program features two interfaces:
- **CLI**: Manage tasks using terminal commands.
- **GUI**: A user-friendly graphical interface with real-time clock updates.

---

## Features

### Command-Line Interface (CLI)
- **Add a Task**: Add new tasks by typing `add <task>`.
- **Show Tasks**: View all tasks with their corresponding indexes.
- **Edit a Task**: Modify existing tasks by selecting their index.
- **Complete a Task**: Remove tasks after completion.
- **Exit**: Safely exit the application.

### Graphical User Interface (GUI)
- **Real-Time Clock**: Displays current date and time dynamically.
- **Add Tasks**: Add new tasks via an input field.
- **Edit Tasks**: Modify selected tasks.
- **Complete Tasks**: Mark and remove completed tasks.
- **Interactive List**: View all tasks in a scrollable listbox.
- **Exit Button**: Close the application gracefully.

---

## Technologies Used
- **Python**: Core programming language.
- **PySimpleGUI**: Library for building the graphical user interface.
- **File I/O**: Persistent task storage via `todos.txt`.
- **Time Module**: Dynamic clock display in the GUI.

---

## Project Structure
```
.
├── cli.py         # Command-line interface implementation
├── gui.py         # GUI implementation using PySimpleGUI
├── functions.py   # Utility functions for task management
├── todos.txt      # Persistent task storage
└── README.md      # Project documentation
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   cd todo-list-app
   ```

2. **Install Dependencies**:
   ```bash
   pip install PySimpleGUI
   ```

3. **Run the CLI Application**:
   ```bash
   python cli.py
   ```

4. **Run the GUI Application**:
   ```bash
   python gui.py
   ```

---

## Usage

### Running the CLI
- **Add Task**: `add <task>`
- **Show Tasks**: `show`
- **Edit Task**: `edit <task_index>`
- **Complete Task**: `complete <task_index>`
- **Exit**: `exit`

Example:
```bash
Type add or show or exit or edit or complete: add Buy groceries
Type add or show or exit or edit or complete: show
1. Buy groceries
```

### Running the GUI
1. Launch `gui.py`.
2. Use the interface to **add**, **edit**, or **complete** tasks.
3. View real-time updates with the clock display.

---

## Demo
### GUI Interface
![GUI Screenshot](link_to_image_here)

---

## Future Enhancements
- Add **task prioritization** with color-coded labels.
- Implement **due dates** and reminders.
- Enable synchronization with cloud storage for cross-device support.

---

## Author
**Your Name**  
LinkedIn: [Your LinkedIn Profile](#)  
GitHub: [Your GitHub Profile](https://github.com/yourusername)
