#!/usr/bin/python3
"""
This module contains the methods for the console.
"""
import cmd
import sys
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """This class defines the console commands.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the console.
        """
        return True

    def do_EOF(self, arg):
        """Exit the console when pressing Ctrl+D or typing "EOF".
        """
        print()
        return True

    # Commands
    def do_create(self, arg):
        """This command creates a new instace of BaseModel
        and saves it to JSON file, printing the ID.
        """
        args_list = parse(arg)
        # Check if the class name is missing
        if len(args_list) < 1:
            print("** class name missing **")
        # Check if the class name doesn’t exist
        elif check_class(args_list[0]) is False:
            print("** class doesn't exist **")
        else:
            class_name = args_list[0]
            new_instance = eval(class_name+'()')
            storage.new(new_instance)
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print string representation of an instance
        based on class name and id.
        """
        args_list = parse(arg)
        # Check if the class name is missing
        if len(args_list) < 1:
            print("** class name missing **")
        # Check if the class name doesn’t exist
        elif check_class(args_list[0]) is False:
            print("** class doesn't exist **")
        # Check if the id is given as a parameter
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            # Create a dictionary with all objects, and search if key exists.
            # Key is "<class_name>.id" and the values stored are instances.
            key = args_list[0] + '.' + args_list[1]
            new_dict = storage.all()
            # If the value exists, we can print the string representation
            # of said instance. Otherwise, an error message will be displayed.
            if key not in new_dict:
                print("** no instance found **")
            else:
                print(new_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args_list = parse(arg)
        # Check if the class name is missing
        if len(args_list) < 1:
            print("** class name missing **")
        # Check if the class name doesn’t exist
        elif check_class(args_list[0]) is False:
            print("** class doesn't exist **")
        # Check if the id is given as a parameter
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            # Create a dictionary with all objects,
            # and search if the key exists.
            # Key is "<class_name>.id" and the values stored are instances.
            key = args_list[0] + '.' + args_list[1]
            new_dict = storage.all()
            # If the value does not exist, an error message will be displayed.
            if key not in new_dict:
                print("** no instance found **")
            else:
                new_dict.pop(key, None)  # Delete that object from dict
                storage.save()  # Save update in json file

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all."""

        args_list = parse(arg)
        new_dict = storage.all()  # This is a dict of instances.
        new_list = []
        if len(args_list) == 0:
            for val in new_dict.values():
                new_list.append(val.__str__())
            print(new_list)
        else:
            # Check if the class name doesn’t exist
            if check_class(args_list[0]) is False:
                print("** class doesn't exist **")
            else:
                # Check if value class name is the argument, then append.
                for val in new_dict.values():
                    if val.__class__.__name__ == args_list[0]:
                        new_list.append(val.__str__())
                print(new_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        args_list = parse(arg)
        new_dict = storage.all()  # This is a dict of instances.
        # list[0] = classname
        # list[1] = id
        # list[2] = attribute name
        # list[3] = "atribute value"
        if len(args_list) < 1:
            print("** class name missing **")
        # Check if the class name doesn’t exist
        elif check_class(args_list[0]) is False:
            print("** class doesn't exist **")
        # Check if the id is given as a parameter
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            new_key = args_list[0] + '.' + args_list[1]  # This is the key
            if new_key not in new_dict.keys():
                print("** no instance found **")
            elif len(args_list) < 3:
                print("** attribute name missing **")
            elif len(args_list) < 4:
                print("** value missing **")
            else:
                # Get the instance
                instance = new_dict[new_key]
                # Get the attribute to update from that instance
                try:
                    # Get the type of the attribute
                    # Cast the attribute value to corresponding type
                    up_attr = getattr(instance, args_list[2])
                    attr_type = type(up_attr)
                    casted_val = eval('attr_type' + '(' + args_list[3] + ')')
                    setattr(instance, args_list[2], casted_val)
                except Exception:
                    # If attribute does not exist, save value to set.
                    setattr(instance, args_list[2], args_list[3])
                # Set attribute with new value
                # Save changes to JSON file
                storage.save()

    # Help updates: (end all of them with a new line)
    def help_quit(self):
        """Help for quit command.
        """
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """Help for EOF.
        """
        print("Press Ctrl+'D' to exit the program")
        print()

    def help_create(self):
        """Help for create command.
        """
        print("Create a new instance of the given class. If it works"
              "the id will be displayed.")
        print("Usage: create <class name>")
        print()

    def help_show(self):
        """Help for show command.
        """
        print("Print the string representation of an instance")
        print("Usage: show <Class> <id>")
        print()

    def help_destroy(self):
        """Help for destroy command
        """
        print("Destroy an instance")
        print("Usage: destroy <Class> <id>")
        print()

    def help_all(self):
        """Help for all command.
        """
        print("Print the string representations of all instances.")
        print("If a class is given, only instances of said class will" +
              "be displayed.")
        print("Usage: all <class name> or all")
        print()

    def help_update(self):
        """Help for update command.
        """
        print("Change value of an attribute of an instance")
        print("If the attribute doesn't exist the command will create it")
        print("Usage: update <Class> <id> <attribute name> <attribute value>")
        print()

    # Miscellaneous code:
    def emptyline(self):
        """What it does with enters and empty lines.
        """
        pass

    def default(self, line):
        """
        This method is called when the command is not found.
        """
        for c in line:
            if c is '.':
                try:
                    arg = line.replace("(", ".(")
                    args_list = arg.split(".")
                    if check_class(args_list[0]):
                        if args_list[1] == "count":  # This works
                            dictionary = storage.all()
                            thenumber = 0
                            for key in dictionary:
                                key = key.split('.')
                                if key[0] == args_list[0]:
                                    thenumber += 1
                            print(thenumber)
                        elif args_list[1] == "all":  # This works
                            self.do_all(args_list[0])
                        elif args_list[1] == "show":  # This works
                            args_list[2] = args_list[2].replace("(", "")
                            args_list[2] = args_list[2].replace(")", "")
                            self.do_show(args_list[0] + ' ' + args_list[2])
                        elif args_list[1] == "destroy":  # This works
                            args_list[2] = args_list[2].replace("(", "")
                            args_list[2] = args_list[2].replace(")", "")
                            self.do_destroy(args_list[0] + ' ' + args_list[2])
                        elif args_list[1] == "update":  # This works
                            args_list[2] = args_list[2].replace("(", "")
                            args_list[2] = args_list[2].replace(")", "")
                            parameters = args_list[2].split(",")
                            print(parameters)
                            aidi = parameters[0]
                            name = parameters[1]
                            value = parameters[2]
                            self.do_update(args_list[0] + ' ' + aidi +
                                           ' ' + name + ' ' + value)
                    else:
                        print("** command not found **")
                except:
                    pass


def parse(arg):
    """Converts a string to an argument list.
    This list will not contain the command as first argument.
    """
    args_list = split(arg)
    return args_list


def check_class(string):
    """Check if a given string is a valid class.
    """
    all_classes = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
    if string in all_classes:
        return True
    else:
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
