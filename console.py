#!/usr/bin/python3
"""
    a program called console.py that contains
    the entry point of the command interpreter:
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        A class that defines quite and EOF methods

        Attributes:
            prompt (str): custom prompt
    """
    prompt = "(hbnb) "

    def emptyline(self):
        return False

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        """
            quit the command to exit the program
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self, line):
        """
            creates an new instance of BaseModel
        """
        if line:
            if line != 'BaseModel':
                print("** class doesn't exist **")
            else:
                new_obj = BaseModel()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, line):
        """
            Prints a string representation of an object
            based on class name and id
        """
        cmds = line.split()
        cmds_len = len(cmds)

        if cmds_len == 0:
            print("** class name missing **")
            return
        if cmds_len == 1:
            print("** instance id missing **")
            return

        a_class, id = cmds
        if a_class != 'BaseModel':
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        for key in all_objs.keys():
            obj = all_objs[key]
            match_id = obj.get('id')
            class_name = obj.get('__class__')

            if id == match_id and a_class == class_name:
                new_obj = BaseModel(**obj)
                print(new_obj)
                return

        print("** no instance found **")

    def do_destroy(self, line):
        """
            Deletes an object based on className and id
        """
        cmds = line.split()
        cmds_len = len(cmds)

        if cmds_len == 0:
            print("** class name missing **")
            return

        if cmds_len == 1:
            print("** instance id missing **")
            return

        a_class, id = cmds
        all_objs = storage.all()

        for key in storage.all():
            obj = all_objs[key]
            match_id = obj.get('id')
            match_class = obj.get('__class__')

            if id == match_id and a_class == match_class:
                del all_objs[key]
                storage.save()
                return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
