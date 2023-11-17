import sys
import subprocess

from data.logger import Logger


class Log:
    def msg(status):
        Logger.__client_logger__(status, "logs.vs", "./logs/")


class Connection:
    @staticmethod
    def check_wifi():
        try:
            result = subprocess.run(["iwconfig"], capture_output=True, text=True)
            output = result.stdout
            if "ESSID:off/" in output:
                Log.msg("Make sure you have an active wifi connection")
                sys.exit()
            else:
                Log.msg("Active wifi connection found")
        except FileNotFoundError:
            Log.msg(
                "Error: 'iwconfig' command not found. Run this on a Linux system with wireless support."
            )
            sys.exit()
