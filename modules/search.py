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
            search_term (str): The search term to match against exploit module attributes.
        """

        search_term_lower = search_term.lower()

        matching_exploits = [
            exploit
            for exploit in exploits
            if search_term_lower in exploit.name.lower()
            or search_term_lower in exploit.author.lower()
            or search_term_lower in exploit.description.lower()
            or search_term_lower in exploit.creation_date.lower()
        ]

        if matching_exploits:
            header_titles = ["#", "Name", "Author", "Date", "Description"]
            column_widths = [4, 20, 20, 20, 50]
            header_row = "".join(
                [
                    title.ljust(width)
                    for title, width in zip(header_titles, column_widths)
                ]
            )
            dash_line = "".join(
                [
                    ("-" * len(title)).ljust(width)
                    for title, width in zip(header_titles, column_widths)
                ]
            )
            search_result = f"Search Results for '{search_term}'"

            print(f"\n    {search_result}\n    {'=' * (len(search_result))}")
            print(f"    {header_row}")
            print(f"    {dash_line}")

            for i, exploit_instance in enumerate(matching_exploits, 1):
                row_data = [
                    str(i),
                    exploit_instance.name,
                    exploit_instance.author,
                    exploit_instance.creation_date,
                    exploit_instance.description,
                ]
                row = "".join(
                    [data.ljust(width) for data, width in zip(row_data, column_widths)]
                )
                print(f"    {row}")
            print()
        else:
            print(" ")
            Log.msg(f"No results found for -> {search_term}\n")
