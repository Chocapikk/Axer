class Table:
    """
    A class to represent a formatted table.

    Attributes:
        header_titles (list of str): Column titles for the table header.
        column_widths (list of int): Widths for each column in the table.
        title (str, optional): An optional title for the table. Defaults to None.
        spacing (int, optional): The number of spaces to indent the table. Defaults to 4.

    Methods:
        print_table(data_rows): Prints the table with given data rows.
    """

    def __init__(self, header_titles, column_widths, title=None, spacing=4):
        """
        Constructs all the necessary attributes for the Table object.

        Args:
            header_titles (list of str): Column titles for the table header.
            column_widths (list of int): Widths for each column in the table.
            title (str, optional): An optional title for the table. Defaults to None.
            spacing (int, optional): The number of spaces to indent the table. Defaults to 4.
        """

        self.header_titles = header_titles
        self.column_widths = column_widths
        self.title = title
        self.spacing = " " * spacing

    def print_table(self, data_rows):
        """
        Prints the table with the provided data rows.

        This method formats and prints a table based on the header titles, column widths,
        and an optional title. Each row of data is printed in its respective column.

        Args:
            data_rows (list of list of str/int): A list of rows, where each row is a
                                                 list containing data for each column.
        """

        if self.title:
            title_line = f"{self.spacing}{self.title}"
            print(f"\n{title_line}\n{self.spacing}{'=' * len(self.title)}")

        header = "".join(
            [
                title.ljust(width)
                for title, width in zip(self.header_titles, self.column_widths)
            ]
        )
        dash_line = "".join(
            [
                ("-" * len(title)).ljust(width)
                for title, width in zip(self.header_titles, self.column_widths)
            ]
        )

        print(f"{self.spacing}{header}")
        print(f"{self.spacing}{dash_line}")

        for row in data_rows:
            formatted_row = "".join(
                [str(item).ljust(width) for item, width in zip(row, self.column_widths)]
            )
            print(f"{self.spacing}{formatted_row}")
