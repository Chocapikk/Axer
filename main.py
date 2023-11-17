import os
import sys
import inspect

from x64.wifi            import Connection
from data.clear          import ClearScreen
from data.banner         import Display
from data.logger         import Logger
from core.modular        import Module
from modules.help        import HelpCommand
from modules.search      import SearchCommand
from importlib.machinery import SourceFileLoader

class Log:
    """
    Log class for handling and displaying log messages.

    Methods:
        msg(status: str) -> None:
            Log a message using the Logger class.

    Attributes:
        None
    """

    def msg(status: str) -> None:
        """
        Log a message using the Logger class.

        Parameters:
            status (str): The message to be logged.

        Returns:
            None
        """
        Logger.__client_logger__(status, "logs.vs", "./logs/")


class ExploitLoader:
    """
    A class to load and manage exploit modules.

    Methods:
        __init__() -> None:
            Initialize an ExploitLoader object with an empty list of exploits.

        load_exploits(directory: str = "exploits") -> None:
            Load exploit modules from the specified directory and its subfolders.

    Attributes:
        exploits (list): A list to store loaded exploit instances.
    """

    def __init__(self) -> None:
        """Initialize an ExploitLoader object with an empty list of exploits."""
        self.exploits = []

    def load_exploits(self, directory: str = "exploits") -> None:
        """
        Load exploit modules from the specified directory and its subfolders.

        This method iterates through Python files in the specified directory
        and its subfolders, loads each module, and instantiates classes that
        are subclasses of Module. The instantiated exploit instances are added
        to the 'exploits' list.

        Parameters:
            directory (str): The base directory to search for exploit modules.

        Returns:
            None
        """
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".py") and filename != "__init__.py":
                    full_path = os.path.join(root, filename)
                    exploit_module = SourceFileLoader(
                        filename[:-3], full_path).load_module()
                    for name, obj in inspect.getmembers(exploit_module):
                        if inspect.isclass(obj) and issubclass(obj, Module) and obj is not Module:
                            exploit_instance = obj()
                            exploit_instance.folder = os.path.relpath(root, directory)
                            self.exploits.append(exploit_instance)
                    Logger.__client_logger__(f"Loaded {filename[:-3]} module", "logs.vs", "./logs/")
        print(" ")

def main(loader: ExploitLoader, help_command: HelpCommand, search_command: SearchCommand) -> None:
    """
    Main function to interact with loaded exploit modules.

    This function provides a loop that takes user input, allowing interaction
    with loaded exploit modules. Users can execute exploits, display help,
    search for exploits, or exit the program.

    Parameters:
        loader (ExploitLoader): An instance of the ExploitLoader class.
        help_command (HelpCommand): An instance of the HelpCommand class.
        search_command (SearchCommand): An instance of the SearchCommand class.

    Returns:
        None
    """
    try:
        while True:
            user_input = input("(local) axer ~$ ").strip().split()
            command = user_input[0] if user_input else None

            match command:
                case "":
                    pass
                case "help":
                    folder_name = user_input[1] if len(user_input) > 1 else None
                    help_command.execute(loader.exploits, folder_name)
                case "search":
                    search_term = user_input[1] if len(user_input) > 1 else None
                    if search_term:
                        search_command.execute(loader.exploits, search_term)
                    else:
                        print("")
                        Log.msg("Please provide a search term\n")
                case "exit":
                    Log.msg("Exiting Axer...")
                    break
                case _ if command is not None:
                    exploit_instance = next(
                        (exploit for exploit in loader.exploits if exploit.name == command), None)
                    if exploit_instance:
                        print()
                        exploit_instance.execute()
                        print()
                    else:
                        help_command.execute_command(command)
                case _:
                    pass

    except KeyboardInterrupt:
        print("")
        Log.msg("Exiting Axer...")
        sys.exit()


if __name__ == "__main__":
    ClearScreen.clear()
    Display.banner()
    Connection.check_wifi()
    loader = ExploitLoader()
    loader.load_exploits()
    help_command = HelpCommand()
    search_command = SearchCommand()
    main(loader, help_command, search_command)
