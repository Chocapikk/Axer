class Table:
    def __init__(self, header_titles, column_widths, title=None, spacing=4):
        self.header_titles = header_titles
        self.column_widths = column_widths
        self.title = title
        self.spacing = " " * spacing

    def print_table(self, data_rows):
        if self.title:
            title_line = f"{self.spacing}{self.title}"
            print(f"\n{title_line}\n{self.spacing}{'=' * len(self.title)}")

        header = "".join([title.ljust(width) for title, width in zip(self.header_titles, self.column_widths)])
        dash_line = "".join([("-" * len(title)).ljust(width) for title, width in zip(self.header_titles, self.column_widths)])

        print(f"{self.spacing}{header}")
        print(f"{self.spacing}{dash_line}")

        for row in data_rows:
            formatted_row = "".join([str(item).ljust(width) for item, width in zip(row, self.column_widths)])
            print(f"{self.spacing}{formatted_row}")