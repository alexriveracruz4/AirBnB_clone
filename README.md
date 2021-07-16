# AirBnB clone - The console

![holberton_airbnb_logo](images/Airbnb_clone.png)

## Table of Contents

* [Description](#description)
* [Block Diagram of the Project](#Diagram)
* [Requirements](#requirements)
* [File Structure](#file-structure)
* [Execution](#execution)
* [Examples](#examples)
* [Bugs](#bugs)
* [Authors](#authors)

## Description

**hbnb** is a big project whose purpose is make a full Airbnb clon, in this repository we work the first part of this big project. We covered The console part where we made a simple command interpreter that parses and evaluates input from the commandline appropriately. Test suite included.

## Block Diagram of the Project

![holberton_airbnb_logo](images/Diagram_project_airbnb.png)

## Requirements

* Must follow [Pep8](https://www.python.org/dev/peps/pep-0008/) style and document guidelines
* Allowed editors: `vi`, `vim`, `emacs`
* Must have a `README.md` file
* All header files must be include guarded
* Must have unittests that can be executed using `python3 -m unittest discover tests`

## File Structure

* [AUTHORS](AUTHORS) - list of participants of the project
* [base_model.py](/models/base_model.py) - class that cover the initialization, serialization and deserialization of future instances
  * `__init__` - initialize instance attributes
  * `__str__` - creates formatted string representation of instance
  * `save` - updates public instance attribute `updated_at` with current datetime
  * `to_dict` - creates a dictionary containing all keys/values of `__dict__` of the instance
* [file_storage.py](/models/engine/file_storage.py) - class FileStorage
  * `all` - returns the dictionary __objects
  * `new` - sets in `__objects` the obj with key `<obj class name>.id`
  * `save` - serializes `__objects` to the JSON file
  * `reload` - deserializes the JSON file to `__objects`
* [console.py](console.py) - command interpreter
  * `do_create` - create a new instance of a class
  * `do_show` - prints string representation of an instance based on class name and id
  * `do_all` - prints all string representation of all instances
  * `do_destroy` - deletes an instance based on the class
  * `do_update` - updates an instance based on the class
  * `do_quit` - quit program
  * `do_EOF` - exit at end of file
* [user.py](/models/user.py) - class User
* [city.py](/models/city.py) - class City
* [state.py](/models/state.py) - class State
* [place.py](/models/place.py) - class Place
* [review.py](/models/review.py) - class Review
* [amenity.py](/models/amenity.py) - class Amenity
* [`__init__.py`](/models/__init__.py) - initialization code for Python package models
* [tests](/tests/) - unit test files
* [web_static](/web_static/103-index.html) - HTML and CSS files

### Execution

### Unit Testing

```python3 -m unittest discover tests```

### Console

```./console.py```

## Examples

### Interactive Mode

```c
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
**Creating a new object**
```
(hbnb) create
** class name missing **
(hbnb) create User
1f57ab9c-79bd-440e-8bdb-b00e132b0d51
(hbnb)
```
**Show all created objects**
```
(hbnb) all
["[User] (1f57ab9c-79bd-440e-8bdb-b00e132b0d51) {'updated_at': datetime.datetime(2021, 6, 30, 14, 46, 37, 323844), 'id': '1f57ab9c-79bd-440e-8bdb-b00e132b0d51', 'created_at': datetime.datetime(2021, 6, 30, 14, 46, 37, 323783)}"]
(hbnb)
```
**Update an object**
```
(hbnb) update User 1f57ab9c-79bd-440e-8bdb-b00e132b0d51 Name "Jhonatan"
(hbnb) show User 1f57ab9c-79bd-440e-8bdb-b00e132b0d51
[User] (1f57ab9c-79bd-440e-8bdb-b00e132b0d51) {'created_at': datetime.datetime(2021, 6, 30, 14, 46, 37, 323783), 'id': '1f57ab9c-79bd-440e-8bdb-b00e132b0d51', 'updated_at': datetime.datetime(2021, 6, 30, 14, 46, 37, 323844), 'Name': 'Jhonatan'}
(hbnb)
```
### Non-Interactive Mode

```c
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Bugs

At this time, there are no known bugs.

## Authors

* Alex Rivera | [GitHub](https://github.com/alexriveracruz4)
* Jhonatan Jauja | [GitHub](https://github.com/jhonnjc15)

