# Python-File-Handling-and-Exception-Handling

## Overview
This guide covers essential concepts of file handling and exception handling in Python. File handling allows Python programs to read and write data to files, making it possible to store and retrieve data for future use. Exception handling is crucial for building robust applications that can handle unexpected errors gracefully.

## Contents
### File Handling in Python
* Opening Files
* Reading Files
* Writing Files
* Closing Files
* File Modes

### Exception Handling in Python
* try, except, else, finally blocks
* Custom Exceptions
* Common Exceptions

### 1. File Handling in Python
Python provides built-in functions for file handling, allowing for seamless reading, writing, and manipulation of files.

#### Opening Files
Use the open() function to open a file. It requires a file path and a mode (r for reading, w for writing, etc.).
```
file = open("filename.txt", "r")
```
#### Reading Files
You can read file content using methods like .read(), .readline(), and .readlines().
```
content = file.read()    # Reads entire file
line = file.readline()   # Reads one line at a time
lines = file.readlines() # Reads all lines into a list
```

#### Writing Files
To write to a file, open it in write mode (w) or append mode (a).

```
file = open("filename.txt", "w")
file.write("This is a new line.")
```
#### Closing Files
Always close files after reading or writing to free up resources.

```
file.close()
```
#### File Modes
* r: Read (default mode)<br>
* w: Write (overwrites existing content)<br>
* a: Append (adds content to the end)<br>
* rb / wb: Read/write in binary mode<br>

#### Using with Statement
The with statement automatically closes the file after the block of code is executed.
```
with open("filename.txt", "r") as file:
    content = file.read()
```
### 2. Exception Handling in Python
Exception handling allows programs to manage errors and continue running smoothly.

#### try and except
The try block lets you test code for errors. The except block lets you handle the error.

```
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

#### else
The else block runs if no exceptions occur.
```
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful!")
```
#### finally
The finally block executes no matter what, even if an exception occurs, making it useful for cleaning up resources like closing files.
```
try:
    file = open("filename.txt", "r")
    # Perform file operations
except Exception as e:
    print("An error occurred:", e)
finally:
    file.close()
```
#### Custom Exceptions
You can create your own exceptions by inheriting from the Exception class.

```
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)
```
#### Common Exceptions
* FileNotFoundError: Raised when a file is not found.
* ZeroDivisionError: Raised when dividing by zero.
* TypeError: Raised for invalid operations on types.
* ValueError: Raised when an operation receives an invalid value.

###  Examples

#### Reading from a File with Error Handling
```
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
```

#### Writing to a File and Handling Exceptions
```
try:
    with open("output.txt", "w") as file:
        file.write("Writing some data.")
except IOError:
    print("An error occurred while writing to the file.")
```

#### Custom Exception Usage
``` 
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return number

try:
    check_positive(-10)
except NegativeNumberError as e:
    print(e)
```
 
### Conclusion
Mastering file handling and exception handling in Python is essential for building reliable applications. By handling files and exceptions carefully, you can create scripts that work
with data files effectively and handle unexpected issues smoothly.


