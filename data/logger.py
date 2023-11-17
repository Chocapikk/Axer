import os
import time
import datetime

from cutepy import HEX


class Variables:
    """
    A class for managing global variables used in the application.

    Attributes:
        None
    """

    global start_time, logger_time

    start_time = time.time()
    logger_time = datetime.datetime.now()
    logger_time = logger_time.strftime("%H:%M:%S")


class Colors:
    """
    A class for defining color codes used for console output.

    Attributes:
        green (str): The color code for green.
        muted (str): The color code for muted.
        foreground (str): The color code for foreground.
        reset (str): The color code to reset formatting.
    """

    green = HEX.print("e3d5ae")
    muted = HEX.print("877a69")
    foreground = HEX.print("efe9d4")
    reset = HEX.reset


class Logger:
    """
    A class for logging status messages to the console.

    Attributes:
        None

    Methods:
        __client_logger__(status): Log a status message to the console.
    """

    @staticmethod
    def __client_logger__(status: str, file_name: str, path: str) -> str:
        """
        Log a status message to the console and write it to a file.

        Args:
            status (str): The status message to be logged.
            file_name (str): The name of the file to write the status message.
            path (str): The path to the directory where the file should be saved.

        Returns:
            None
        """
        log_message = f"{Colors.muted}{logger_time}{Colors.reset} {Colors.green}__{Logger.__client_logger__}__{Colors.reset}{Colors.foreground} | {status} {Colors.reset}"
        print(log_message)

        with open(os.path.join(path, file_name), "a") as file:
            file.write(f"__{Logger.__client_logger__}__ | {status}" + "\n")
