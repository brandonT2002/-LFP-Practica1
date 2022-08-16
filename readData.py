from builder import Course

class Controller:
    def __init__(self):
        self.courses = []

    def readFile(self,route):
        #route = 'cursos.lfp'
        cursos = open(route,encoding='utf-8').read().split('\n')
        for course in cursos:
            course = course.split(',')
            self.courses.append(Course(int(course[0]),course[1],course[2].split(';'),int(course[3]),int(course[4]),int(course[5]),course[6]))

    def searchCourse(self,code):
        course = self.checkCourse(code)
        if course:
            return course
        else:
            return None

    def addCourse(self,code,name,prerequisite,mandatory,semester,credits,state):
        if self.checkCourse(code):
            return False
        self.courses.append(Course(code,name,prerequisite.split(';'),mandatory,semester,credits,state))
        return True

    def editCourse(self,code,name,prerequisite,mandatory,semester,credits,state):
        course = self.checkCourse(code)
        if course:
            course.name = name
            course.prerequisite = prerequisite.split(';')
            course.mandatory = mandatory
            course.semester = semester
            course.credits = credits
            course.state = state
            return True
        return False

    def deleteCourse(self,code):
        if self.checkCourse(code):
            self.courses.pop(self.index)
            return True
        return False

    def approvedCredits(self):
        self.count1 = 0
        for i in self.courses:
            if i.state == '0':
                self.count1 += i.credits

    def creditsStudying(self):
        self.count2 = 0
        for i in self.courses:
            if i.state == '1':
                self.count2 += i.credits

    def checkCourse(self,code):
        self.index = 0
        for i in self.courses:
            if i.code == code:
                return i
            self.index += 1
        return None