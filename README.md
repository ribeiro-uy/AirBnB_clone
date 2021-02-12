# AirBnB clone

This project contains the first module of the AirBnB clone done as final \
project of the Holberton School foundations programme. All source code is \
done in Python.

This program works both in interactive and non-interactive mode.

# General usage

Download this repository and execute the console file. Then input commands.

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

- create: Creates a new instance of the given class, saves it, and prints the id.
	Usage: (hbnb) create <class name>

- show: Prints the string representation of an instance based on class name and id.
	Usage: (hbnb) show <class name> <id>

- all: Prints all string representations of all instances based or not on the class name.\
Future release will take into account the class name, and print all instances of said class.
	Usage:	(hbnb) all
			(hbnb) all <class name>

- destroy: Deletes an instance based on class name and id, saving the change in the JSON file.
	Usage: (hbnb) destroy <class name> <id>

- update: Updates an instance based on class name and id, by adding or updating an attribute.
	Usage: (hbnb) update <class name> <id> <attribute name> "<attribute value>"

- help: Displays documentation. If a command is given, it will display information about \
said command, otherwise it will list all commands.
	Usage:	(hbnb) help
			(hbnb) help all

- quit: exit the console.
	Usage: (hbnb) quit

- EOF: same behaviour as quit.

# Future releases

A list of the features to develop in case we have some extra time:

- Console retrieves all instances of a given class.

- Console retrieves the number of instances of a given class.

- Console retrieves an instance based on its id.

- Console destroys an instance based on its id.

- Console updates an attribute of an instance based on its id.

- Console updates an instance based on its id (with a given dictionary).

# Bugs

No known bugs yet.

# Authors

Micaela Percovich
Roberto Ribeiro
