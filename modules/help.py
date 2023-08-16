class HelpCommand:
    """
    A class to display a help menu for available exploit modules.

    This class provides a method to display a formatted help menu containing information
    about available exploit modules, including their names, authors, creation dates, and descriptions.

    Methods:
        execute(exploits): Display the help menu for available exploit modules.

    Attributes:
        None
    """

    def __init__(self):
        """Initialize a HelpCommand object (no specific attributes required)."""
        pass

    def execute(self, exploits):
        """
        Display a formatted help menu for available exploit modules.

        This method prints a formatted help menu that lists the available exploit modules,
        including their names, authors, creation dates, and descriptions.

        Args:
            exploits (list): A list of exploit instances to be displayed in the help menu.
        """
        print("""
    Help Menu
    =========
        
    #   Name               Author         Date              Description
    -   ----               ------         ----              -----------""")
        for i, exploit_instance in enumerate(exploits, 1):
            print(f"    {i: <4}{exploit_instance.name: <19}{exploit_instance.author: <15}{exploit_instance.creation_date: <18}{exploit_instance.description}")
        print()
