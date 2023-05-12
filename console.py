#!/usr/bin/python3
"""
The Console Module.
"""
import cmd
import re
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """Command line interpreter for HBNB application."""

    prompt = "(hbnb) "

    # an empty line +
    # enter shouldn’t execute anything
    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    # checks when input is invalid
    def default(self, arg):

        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    # handles the EOF to exit program
    def do_EOF(self, arg):
        print()
        return True

    # handles the quit action of the program
    def do_quit(self, arg):
        return True

    def do_create(self, arg):

        # handles the create command
        # creates a new class instance & prints its id
        # arg represents the class being called

        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except AttributeError:
            print("** class doesn't exist **")


    def do_show(self, arg):

        # handles the show command
        # displays a string representation of a class instance

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        # if classname is missing

        if class_name not in storage.__class__():
            print("** class doesn't exist **")
            return

        # if classname does not exist

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()

        # if the instance id is missing

        if key not in instances:
            print("** no instance found **")
            return

        instance = instances[key]
        print(instance)

    def do_destroy(self, arg):

        # handles the destroy command
        # destroys the class instance of a given id

        args = arg.split()

        # prints if the classname is missing
        if not args:
            print("** class name missing **")
            return

        # prints if classname doesn't exist
        class_name = args[0]
        if class_name not in storage.__class__():
            print("** class doesn't exist **")
            return

        # prints if the instance id is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        # check instances & deletes instance from storage

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()

        # saves the changes in the code

        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        storage.save()

    def do_all(self, arg):
        # print the string representation of all the classes instance
        # represents the all command
        instances = storage.all()

        # prints if no classname is provided
        if not arg:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = arg.strip()

            # prints if classname is not provided
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            print([str(instance) for instance in instances.values() if instance.__class__.__name__ == class_name])

    def do_update(self, arg):

    # handles the update command
    # updates an instance based on the class name & id
    # saves the change into the JSON file


        args = arg.split()

        # print if the class name is missing
        if not args:
            print("** class name missing **")
            return

        # print if the class name doesn't exist
        class_name = args[0]
        if class_name not in storage.__class__():
            print("** class doesn't exist **")
            return

        # print if the instance id is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        # check if the instance exists
        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()

        # print if no instance is found
        if key not in instances:
            print("** no instance found **")
            return

        instance = instances[key]

        # print if the attribute name is missing
        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        # print if the value for the attribute name is missing
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        # update the attribute value
        setattr(instance, attribute_name,eval(attribute_value))
        # storage.save()
        instance.save()


# the cmdloop call starts the interpreter
# prevent code from being executed when the module is imported
# cmdloop() method will continue to prompt the user for input
# til they exit the interpreter.
if __name__ == "__main__":
    HBNBCommand().cmdloop()
