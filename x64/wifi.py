import sys
import subprocess

from data.logger import Logger

class Log:
    """
    A simple logging class for messages related to wifi connection status.
    """
    @staticmethod
    def msg(status):
        """
        Log a message using the Logger class.

        Parameters:
        - status (str): The message to be logged.
        """
        Logger.__client_logger__(status, "logs.vs", "./logs/")


class Connection:
    """
    A class for checking wifi connection status.
    """
    @staticmethod
    def check_wifi():
        """
        Check the status of the wifi connection.

        This method uses the 'iwconfig' command to determine the status of the wifi connection.
        If 'iwconfig' is not found, an error message is logged, and the program exits.
        If the wifi connection is inactive, a message is logged, and the program exits.
        If an active wifi connection is found, a message is logged.

        Note: This method is designed to run on a Linux system with wireless support.

        Raises:
        - FileNotFoundError: If the 'iwconfig' command is not found.
        """
        try:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            output = result.stdout
            if 'ESSID:off/' in output:
                Log.msg("Make sure you have an active wifi connection")
                sys.exit()
            else:
                Log.msg("Active wifi connection found")
        except FileNotFoundError:
            Log.msg("Error: 'iwconfig' command not found. Run this on a Linux system with wireless support.")
            sys.exit()
