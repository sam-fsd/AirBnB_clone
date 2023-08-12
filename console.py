#!/usr/bin/python3
"""
    a program called console.py that contains
    the entry point of the command interpreter:
"""

import cmd
class HBNBCommand(cmd.Cmd):
    """
        A class that defines quite and EOF methods
        
        Attributes:
            prompt (str): custom prompt
    """
    prompt = "(hbnb) "
    def do_quit(self, line):
        return True
    def do_EOF(self, line):
        """
            quit the command to exit the program
        """
        return True
    def help_quit(self):
        print("Quit command to exit the program")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
