#!/usr/bin/python3
"""This module contains all methods for the console.
Accepted commands:
    help
    EOF
    quit
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the console commands.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console when pressing Ctrl+D or typing "EOF"."""
        print()
        return True

    # Help updates: (end all of them with a new line)
    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        print("Press Ctrl+'D' to exit the program")
        print()

    # Miscellaneous code:
    def emptyline(self):
        """What it does with enters and empty lines."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
