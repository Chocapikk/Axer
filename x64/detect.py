import os
import contextlib


class SystemDetection:
    """
    A utility class for detecting the underlying operating system.

    This class provides methods to detect the operating system by analyzing specific files
    and environment variables on Linux, Windows, and macOS.

    Methods:
        detect() -> str: Detect the underlying operating system.

    Attributes:
        None
    """

    @staticmethod
    def detect() -> str:
        """
        Detect the underlying operating system.

        This static method detects the operating system by analyzing specific files and
        environment variables. It returns a string indicating the detected operating system.

        Returns:
            str: The detected operating system. Possible values: "Linux", "Windows", "macOS", "Unknown".
        """
        try:
            with open("/proc/version", "r") as f:
                content = f.read()
                if "Linux" in content:
                    return "Linux"
        except FileNotFoundError:
            pass

        os_env = os.environ.get("OS")
        if os_env and os_env.startswith("Windows"):
            return "Windows"

        with contextlib.suppress(FileNotFoundError):
            with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as f:
                content = f.read().decode("utf-8")
                if "ProductVersion" in content and "Darwin" in content:
                    return "macOS"

        return "Unknown"
