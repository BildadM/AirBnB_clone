#!/usr/bin/python3
"""Console module"""

import cmd
import json
import shlex
from datetime import datetime
from models.base_model import BaseModel
#from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """Create command"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show command"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            instance_id = args[1]
            instance = storage.get(class_name, instance_id)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy command"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            instance_id = args[1]
            instance = storage.get(class_name, instance_id)
            if instance:
                instance.delete()
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """All command"""
        objects = []

        if arg:
            try:
                objects = storage.all(arg)
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            objects = storage.all()

        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Update command"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            instance_id = args[1]
            instance = storage.get(class_name, instance_id)

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attribute_name = args[2]

            if len(args) < 4:
                print("** value missing **")
                return

            attribute_value = args[3]

            # Cast the attribute value to the correct type
            attribute_value = BaseModel.cast_attribute_value(attribute_name, attribute_value)

            # Update the attribute
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """Print help message for quit command"""
        print("Quit the command line interface")

    def help_create(self):
        """Print help message for create command"""
        print("Create a new instance of a given class")

    def help_show(self):
        """Print help message for show command"""
        print("Show the string representation of an instance")

    def help_destroy(self):
        """Print help message for destroy command"""
        print("Delete an instance based on the class name and id")

    def help_all(self):
        """Print help message for all command"""
        print("Print all string representations of all instances or of a specific class")

    def help_update(self):
        """Print help message for update command"""
        print("Update an instance based on the class name and id")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
