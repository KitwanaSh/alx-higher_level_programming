## 0x0C-Python - Almost a Circle
### Background Context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:

- args and kwargs
- Serialization/Deserialization
- JSON
![Image]
### Resources
#### Read or watch:

- [args/kwargs]('https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/')
- [JSON encoder and decoder]('https://docs.python.org/3/library/json.html')
- [unittest module]('https://docs.python.org/3.4/library/unittest.html')
- [Python test cheatsheet]('https://www.pythonsheets.com/notes/python-tests.html')
### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
#### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.
#### Requirements
##### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should be documented: python3 -c 'print(`__import__`("my_module").`__doc__)`'
- All your classes should be documented: python3 -c 'print(`__import__`("my_module").MyClass.`__doc__`)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(`__import__`("my_module").my_function.`__doc__`)' and python3 -c 'print(`__import__`("my_module").MyClass.my_function.`__doc__`)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
##### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test_
- Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
- We strongly encourage you to work together on test cases so that you don’t miss any edge case
### Task
<hr>
<table>
 <thead>
  <tr>
   <th>0. If it's not tested it doesn't work </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
All your files, classes and methods must be unit tested and be PEP 8 validated.

```
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
"----------------------------------------------------------------------"
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
```
_Note that this is just an example. The number of tests you create can be different from the above example._

**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0C-python-almost_a_circle`
- File: `tests/`
   </td>
  </tr>
 </tbody>
</table>
<hr>
<table>
 <thead>
  <tr>
   <th>1. Base class </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
Write the first class Base:

Create a folder named models with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named models/base.py:

- Class Base:
	- private class attribute `__nb_objects = 0`
	- class constructor: `def __init__(self, id=None):`
		- if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
		- otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 

```
__Repo:__

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0C-python-almost_a_circle`
- File: `models/base.py, models/__init__.py`
   </td>
  </tr>
 </tbody>
</table>
<hr>
<table>
 <thead>
  <tr>
   <th>First Rectangle </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
Write the class `Rectangle` that inherits from `Base`:

- In the file `models/rectangle.py`
- Class Rectangle inherits from `Base`
- Private instance attributes, each with its own public getter and setter:
	- `__width -> width`
	- `__height -> height`
	- `__x -> x`
	- `__y -> y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
	- Call the super class with `id` - this super call with use the logic of the `__init__` of the Base class
	- Assign each argument `width`, `height`, `x` and `y` to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
```
__Repo:__

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`
   </td>
  </tr>
 </tbody>
</table>