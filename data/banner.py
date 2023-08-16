class Varialbes:

    __author__  = "Username"
    __version__ = "v1.5"
    __repo__    = "github.com/user/project"


class Display:

    def banner():
        print(f"""
   /`-.        .'(   )\.---.     /`-.  
 ,' _  \   ,') \  ) (   ,-._(  ,' _  \  
(  '-' (  (  '/  /   \  '-,   (  '-' (          Author   ➜  {Varialbes.__author__}
 )   _  )  )     )    ) ,-`    ) ,_ .'          Version  ➜  {Varialbes.__version__}
(  ,' ) \ (  .'\ \   (  ``-.  (  ' ) \          Repo     ➜  {Varialbes.__repo__}
 )/    )/  )/   )/    )..-.(   )/   )/ 
                                       
""")
