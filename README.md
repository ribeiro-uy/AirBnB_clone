# AirBnB clone

This project contains the first module of the AirBnB clone done as final \
project of the Holberton School foundations programme. All source code is \
done in Python.

This program works both in interactive and non-interactive mode.

# General usage

## Installation

* Clone this repository: git clone "https://github.com/rmribeiro-uy/AirBnB_clone.git"
* Access AirBnb directory: cd AirBnB_clone
* Run hbnb (interactively): ./console
* Run hbnb (non-interactively): echo "<command>" | ./console.py

When running interactively, type a command and press return to run it.
This console allows for command completion, as well as command history.

´´´ $ ./console.py
´´´ (hbnb) help
´´´
´´´ Documented commands (type help <topic>):
´´´
´´´ ...
´´´ (hbnb) quit
´´´ $

# Commands

This is a list of the different commands, and a description of their function.
Most commands accept both an interface syntax (<command> <values>) as well as\
 a more pythonic command-line approach (<class name>.<values>). In this case,\
 values should be separated by a comma.

- create: Creates a new instance of the given class, saves it, and prints the id.

	Usage:	(hbnb) create <class name>

			(hbnb) <class name>.create

- show: Prints the string representation of an instance based on class name and id.

	Usage:	(hbnb) show <class name> <id>

			(hbnb) <class name>.show(<id>)

- all: Prints all string representations of all instances based or not on the class name.

	Usage:	(hbnb) all

			(hbnb) all <class name>

			(hbnb) <class name>.all()

- destroy: Deletes an instance based on class name and id, saving the change in the JSON file.

	Usage: 	(hbnb) destroy <class name> <id>

			(hbnb) <class name>.destroy(<id>)

- update: Updates an instance based on class name and id, by adding or updating an attribute.

	Usage: 	(hbnb) update <class name> <id> <attribute name> "<attribute value>"

			(hbnb) <class name>.update(<id>, <attribute name>, <attribute value>)

- count: Displays the number of instances of a given class.

	Usage: (hbnb) <class name>.count()

- help: Displays documentation. If a command is given, it will display information about \
said command, otherwise it will list all commands.

	Usage:	(hbnb) help

			(hbnb) help all

- quit: exit the console.

	Usage: (hbnb) quit

- EOF: same behaviour as quit.

# Future releases

A list of the features to develop in case we have some extra time:

- Console updates several attributes of an instance with a given dictionary.

	Usage: <class name>.update(<id>, <dictionary of attributes>)

# Tests

If you wish to run at the test for this application,
all of the test are located under the test/ folder.

From the root directory can execute all of them by simply running:
$ python3 -m unittest discover tests

# Bugs

No known bugs yet.

# Authors

Micaela Percovich
Roberto Ribeiro

February - 2020