from xmlrpc.client import Boolean


class Course:
    def __init__(self,code : int,name : str,prerequisite : list,mandatory : int,semester : int,credits : int,state : str):
        self.code = code
        self.name = name
        self.prerequisite = prerequisite
        self.mandatory = mandatory
        self.semester = semester
        self.credits = credits
        self.state = state