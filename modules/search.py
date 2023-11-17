from data.logger import Logger
from modules.table import Table


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
            search_term (str): The search term to match against exploit module attributes.
        """

        search_terms_lower = search_term.lower().split()

        matching_exploits = [
            exploit
            for exploit in exploits
            if any(
                word in exploit.name.lower()
                or word in exploit.author.lower()
                or word in exploit.description.lower()
                or word in exploit.creation_date.lower()
                for word in search_terms_lower
            )
        ]

        title = f"Search Results for '{search_term}'"
        header_titles = ["#", "Name", "Author", "Date", "Description"]
        column_widths = [4, 20, 20, 20, 50]
        table = Table(header_titles, column_widths, title=title)

        if matching_exploits:
            data_rows = [
                [
                    str(i),
                    exploit_instance.name,
                    exploit_instance.author,
                    exploit_instance.creation_date,
                    exploit_instance.description,
                ]
                for i, exploit_instance in enumerate(matching_exploits, 1)
            ]

            table.print_table(data_rows)
            print("")
        else:
            print(f"\n{' ' * column_widths[0]}No results found for -> {search_term}\n")
