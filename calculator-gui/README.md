# Calculator in `Python`
![calculator_in_python](https://github.com/tpauldike/rough_work/blob/main/screenshots/calculator.png)

## About the App
This is a deskstop application, a simple calculator built with `Python Tkinter`, that performs more than basic arithmetic operations, such as addition, subtraction, multiplication and division of natural numbers.

It was developed and tested on Ubuntu 22.04.2

## Features of the Calculator
It has the following features:
1. **Good graphical user interface** built with `Python Tkinter`, nicely colored with mouse hover effects on each button.
2. **Other arithmetic operations**, such as
    - `x` squared
    - `x` raised to power `y`
    - square root of `x`
    - inputing negative values (`-x`)
    - calculating decimal values
3. **Displays zero by default and controls inputs and outputs**. For example;
    - You can not input `+` after `-`, the `-` will change to `+`
    - You can not input 2.0.2, only one dot will be allowed for each number
    - Inputing ^ (for power) twice will behave as inputing dot does
    - It does not display decimal values as answer unnecesarily, i.e, you'll get 2 instead of 2.0, except there was some fraction in the answer
4. **Some extra non-arithmetic functions**:
    - A power button to switch the calculator off/on
    - It stores the latest answer, enabling the user to refer to it for further calculations
    - 'clear' and 'backspace' buttons and more
5. **Accepts and control keyboard inputs**:
    - Receives only 0-9 and the available mathematical symbols or signs from the keyboard; any other thing pressed is not accepted as an input and will not be displayed, **except** one clicks on the calculator screen with the mouse, in which case anything can be entered but the calculator will not regard the input as valid and will display a warning and clear everything when '=' or 'Return/Enter' is pressed.
    - *Enter* works like `=`; *Meta/Alt* (the one on the right side) works `answer`; *Esc* works like `clear`, *Backspace* works like `←`, *'/'* inputs `÷` on the screen and *'Shift + 8'* (the * character) displays `×` on the screen

## How to Install and Use the Calculator
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
$ git clone https://github.com/tpauldike/CodeClauseInternship.git
# Check to see whether you have CodeClauseInternship on your terminal by now
$ ls
# Navigate into the calculator folder
$ cd CodeClauseInternship/calculator
# Run the app
$ python3 app.py
```

And the calculator should be up and running by now, waiting to receive your inputs

###### Author: [Topman Paul-Dike](https://github.com/tpauldike)