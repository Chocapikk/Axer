from data.logger import Logger


class Log:

    def msg(status):
        Logger.__client_logger__(status, "logs.vs", "./logs/")


class SearchCommand:
    """
    A class to perform a search for exploit modules.

    Methods:
        execute(exploits, search_term): Perform a search for exploit modules based on a search term.

    Attributes:
        None
    """

    def __init__(self):
        """Initialize a SearchCommand object (no specific attributes required)."""
        pass

    def execute(self, exploits, search_term):
        """
        Perform a search for exploit modules based on a search term.

        This method prints a formatted list of exploit modules that match the search term.

        Args:
            exploits (list): A list of exploit instances to be searched.
            search_term (str): The search term to match against exploit module names.
        """
        matching_exploits = [exploit for exploit in exploits if search_term.lower() in exploit.name.lower()]

        if matching_exploits:
            print(f"\n    Search Results for '{search_term}'\n    {'=' * (24 + len(search_term))}")
            print("""
    #   Name               Author         Date              Description
    -   ----               ------         ----              -----------""")
            for i, exploit_instance in enumerate(matching_exploits, 1):
                print(f"    {i: <4}{exploit_instance.name: <19}{exploit_instance.author: <15}{exploit_instance.creation_date: <18}{exploit_instance.description}")
            print()
        else:
            print(" ")
            Log.msg(f"No results found for -> {search_term}\n")
