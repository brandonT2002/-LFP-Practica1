from tabnanny import check
from builder import Course

class Controller:
    def __init__(self):
        self.courses = []

    def readFile(self):
        cursos = open('cursos.lfp',encoding='utf-8').read().split('\n')
        for course in cursos:
            course = course.split(',')
            self.courses.append(Course(int(course[0]),course[1],course[2].split(';'),int(course[3]),int(course[4]),int(course[5]),course[6]))

    def addCourse(self,code,name,prerequisite,mandatory,semester,credits,state):
        course = self.checkCourse(code)
        if course:
            print('El libro ya existe')
        else:
            self.courses.append(Course(code,name,prerequisite,mandatory,semester,credits,state))
            print('Curso creado exitosamente')

    def checkCourse(self,code):
        for i in self.courses:
            if i.code == code:
                return i
        return None