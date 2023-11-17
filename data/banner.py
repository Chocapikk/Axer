class Varialbes:
    """
    Class to store global variables for the application.
    """
    __author__  = "oromos"
    __version__ = "v1.5"
    __repo__    = "github.com/0romos/axer"


class Display:
    """
    Class for displaying banners and other information.
    """

    @staticmethod
    def banner():
        """
        Print a banner with information about the application.

        The banner includes details such as the author, version, and repository.
        """
        print(f'''
                        m
     $m                mm            m
      "$mmmmm        m$"    mmmmmmm$"
            """$m   m$    m$""""""
          mmmmmmm$$$$$$$$$"mmmm
    mmm$$$$$$$$$$$$$$$$$$ m$$$$m  "    m  "
   $$$$$$$$$$$$$$$$$$$$$  $$$$$$"$$$                       Author   ➜  {Varialbes.__author__}
   mmmmmmmmmmmmmmmmmmmmm  $$$$$$$$$$                       Version  ➜  {Varialbes.__version__}
   $$$$$$$$$$$$$$$$$$$$$  $$$$$$$"""  m                    Repo     ➜  {Varialbes.__repo__}
   "$$$$$$$$$$$$$$$$$$$$$ $$$$$$  "      "
       """""""$$$$$$$$$$$m """"
         mmmmmmmm"  m$   "$mmmmm
       $$""""""      "$     """"""$$
        ''')
