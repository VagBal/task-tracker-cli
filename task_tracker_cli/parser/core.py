import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Command line Task Tracker App")
        self.parser.add_argument("-a", "--add", metavar="", help="Add a new task")
        self.parser.add_argument("-d", "--delete", metavar="", help="delete a task by id")
        self.parser.add_argument("-u", "--update", nargs=2, metavar="", help="Update a task by id and new description")
        self.parser.add_argument("-m", "--mark", nargs=2, metavar="", help="Mark a task by id and new state")
        self.parser.add_argument("-la", "--listall", action="store_true", help="List all tasks")
        self.parser.add_argument("-ld", "--listdone", action="store_true", help="List all done tasks")
        self.parser.add_argument("-lip", "--listip", action="store_true", help="List all in progress tasks")
    
    def parse_args(self):
        try:
            return self.parser.parse_args()
        except SystemExit as e:
            print("Error parsing arguments:", e)
            raise  # Re-raise the exception to maintain the original behavior