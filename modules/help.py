import os
import json

from data.logger import Logger


class Log:

    def msg(status):
        Logger.__client_logger__(status, "logs.vs", "./logs/")


class HelpCommand:
    """
    A class to display a help menu for available exploit modules.

    This class provides a method to display a formatted help menu containing information
    about available exploit modules, including their names, authors, creation dates, and descriptions.

    Methods:
        __init__: Initialize a HelpCommand object.
        load_help_commands: Load the help_commands_json from the specified file.
        execute: Display a formatted help menu for available exploit modules.
        execute_command: Execute a specific command with optional arguments.
    """

    def __init__(self):
        """Initialize a HelpCommand object."""
        self.commands = {
            "help": None,
            "exit": None,
            "clear": lambda: os.system("clear"),
            "exploits": Subcommands.list_exploits,
            "search": None
        }

        self.help_commands_json = self.load_help_commands()

    def load_help_commands(self):
        """
        Load the help_commands_json from the specified file.

        Returns:
            dict: The loaded JSON structure.
        """
        file_path = os.path.join(os.path.dirname(__file__), "help_commands", "struct.json")
        with open(file_path, "r") as file:
            return json.load(file)

    def execute(self, exploits, folder_name=None):
        """
        Display a formatted help menu for available exploit modules.

        This method prints a formatted help menu that lists the available exploit modules,
        including their names, authors, creation dates, and descriptions. It also supports
        filtering the display based on a specified folder.

        Args:
            exploits (list): A list of exploit instances to be displayed in the help menu.
            folder_name (str, optional): The name of the folder to filter exploits. Default is None.
        """
        print("""
    Help Menu
    =========
        
    #   Name               Author         Date              Description
    -   ----               ------         ----              -----------""")
        
        if folder_name:
            filtered_exploits = [exploit for exploit in exploits if exploit.folder == folder_name]
            if filtered_exploits:
                for i, exploit_instance in enumerate(filtered_exploits, 1):
                    print(f"    {i: <4}{exploit_instance.name: <19}{exploit_instance.author: <15}{exploit_instance.creation_date: <18}{exploit_instance.description}")
                print()
            else:
                Log.msg(f"No exploits found in the '{folder_name}' folder")
        else:
            for i, command in enumerate(self.help_commands_json["commands"], 1):
                print(f"    {i: <4}{command['name']: <19}{command['author']: <15}{command['date']: <18}{command['description']}")
            print("")

    def execute_command(self, command, *args):
        """
        Execute a specific command with optional arguments.

        Args:
            command (str): The command to execute.
            *args: Optional arguments for the command.
        """
        if command in self.commands:
            self.commands[command](*args)
        else:
            Log.msg(f"Command '{command}' not found in available commands.")


class Subcommands:
    """
    A class containing subcommands for the HelpCommand class.

    Methods:
        list_exploits: Display a list of available exploit modules.
    """

    @staticmethod
    def list_exploits():
        """
        Display a list of available exploit modules.
        """
        exploits_path = "exploits/"
        folders = [folder for folder in os.listdir(exploits_path) if os.path.isdir(os.path.join(exploits_path, folder))]
        
        print("""
    Exploits
    =========

    #   Name
    -   ----""")

        for i, folder in enumerate(folders, 1):
            print(f"    {i: <4}{folder}")
        
        print("\nSyntax: help <exploit-name>\n")
