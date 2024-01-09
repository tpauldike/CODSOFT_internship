# Contact List
![contact_list_with_python_tkinter](https://github.com/tpauldike/rough_work/blob/main/screenshots/contact_list.png)

## About
> *loading...*

## Installation
> *You may prefer seeing [this video tutorial](https://youtu.be/_HAj5oL9GPA?si=oECWArJe0WmvKXBN), to watch and learn.*

Open your terminal (command line) and do the following:

**Install `python3`:**

The first thing is to download and install python3, if you do not have it on the machine already, visit [https://www.python.org/downloads](https://www.python.org/downloads/) to get it.

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
# Navigate into the calculator folder
$ cd CODSOFT/contact_list
# Run the app
$ python3 app.py
# alternatively, you can do
$ ./app.py
```

###### Author: [Topman Paul-Dike](https://github.com/tpauldike)