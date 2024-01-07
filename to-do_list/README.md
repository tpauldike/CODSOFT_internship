# ToDo App with `Python Tkinter`
![todo_app_with_python_tkinter](https://github.com/tpauldike/rough_work/blob/main/screenshots/todo_app.png)

## About the App
This is a desktop application built using `Python` Tkinter as the Graphical User Interface tool. It's a unique todo app with extra features and with some edge cases handled. The entire application was coded in `Python` programming language.

This app was built as one of the requirements to be certified as a CodSoft intern in `Python development`.

The version used was `Python 3.10.12` and the development environment was `Ubuntu 22.04.2`

## Technologies Used
**Front End (GUI):** `Python Tkinter`

**Logic:** `Python` (OOP)

**Database:** `SQLite`

## Features
1. The application has a good looking graphical user interface, with hover effects on the menus, buttons and popup windows.

2. It has a menu bar at the top, some of which have sub-menus for some extra functionalities beyond CRUD (create, read, update, delete). These functionalities include:
    - Locking the app with a password
    - Sorting the list in any of the 3 different orders
    - Hiding or showing the todo list
    - Creating a new todo list that overwrites the current one
    - Searching for a task on the list, if the list has many tasks

3. On the left side is the widget on which the todo list is displayed.

4. On the right side of the frame are all the necessary input fields and buttons that allow the user to:
    - Add tasks to the todo list
    - Include a description (which is optional)
    - Update any single task
    - Delete single or multiple task(s)
    - Delete the entire todo list
    - Hide or display the todo list

5. At the bottom of the right frame is a box where feedback notifications are displayed for a good user experience. It welcomes the user with the text;

```
Welcome!
Notifications are displayed here
```
6. Popup windows, apart from dialogue boxes for confirmation and warnings, invoked by certain actions such as; 'delete' and 'edit'

## How to Install the App
> *If you prefer seeing a video tutorial, [watch me demonstrate the installation here](https://youtu.be/_HAj5oL9GPA?si=oECWArJe0WmvKXBN).*

It is quite easy to use. Take the following steps on the command line (I mean your terminal):

**Install `python3`:**

The first thing to do is to download and install python3, if you do not have it on the machine already, visit [https://www.python.org/downloads](https://www.python.org/downloads/) to get it.

> *The first code block of instructions can be skipped, by Windows users, but is very necessary for those who use Linux distros (such as Debian, Ubuntu, Fedora, and openSUSE), who may get the `ModuleNotFoundError`*

**Install the module:**

```bash
# Tkinter is inbuilt in python3 but, if you're a Linux distro, you may need to do this:
$ python3 -m tkinter
# This is supposed to display a brief information on a small window about tkinter
# If it rather says "/usr/bin/python3: No module named tkinter" then do this
$ sudo apt install python3-tk
# Confirm that it is now present
$ python3 -m tkinter
```

**Get the app and run it:**

```bash
# Clone the git repository on your CLI
$ git clone https://github.com/tpauldike/CODSOFT.git
# Check to see whether you have CODSOFT on your terminal by now
$ ls
# Navigate into the todo_app folder
$ cd CODSOFT/to-do_list
# Run the app
$ python3 todo_list.py
# Note that an easier way to start the app is
$ ./todo_list.py
```

> *The app should be running by now and ready for use, it will automatically generate a file named 'todo_list.db' that serves as your database and holds all saved data, retrievable when you exit the app and return later*

## How to Use the App
Please see [this short video]() to learn how to use the app or contact [Topman Paul-Dike](https://github.com/tpauldike) if you need some help or have suggestions/complaints

## How to Contribute to this App
If you wish to refactor the code, add some feature, fix a bug, or do anything that will improve the application, I invite you to collaborate with me. Please read [this document](../CONTRIBUTION.md) to know exactly what is expected of you in order for your contribution to be accepted.

###### Author: [Topman Paul-Dike](https://github.com/tpauldike)
