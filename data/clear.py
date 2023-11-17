import os
from x64.detect import SystemDetection

class ClearScreen:
    """
    A utility class for clearing the terminal screen.

    This class provides a platform-independent method for clearing the terminal screen.
    It uses the SystemDetection class to determine the underlying operating system.

    Methods:
        clear(): Clears the terminal screen based on the detected operating system.
    """

    @staticmethod
    def clear():
        """
        Clear the terminal screen based on the detected operating system.

        This static method checks the detected operating system using the SystemDetection class
        and uses the appropriate system command to clear the terminal screen.

        Note:
            On Windows, the 'cls' command is used to clear the screen.
            On Unix-like systems (Linux, macOS), the 'clear' command is used.
        """
        if SystemDetection.detect() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
