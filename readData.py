from builder import Course

class Controller:
    def __init__(self):
        self.courses = []

    def readFile(self):
        cursos = open('cursos.lfp',encoding='utf-8').read().split('\n')
        for curso in cursos:
            curso = curso.split(',')
            self.courses.append(Course(int(curso[0]),curso[1],curso[2].split(';'),int(curso[3]),int(curso[4]),int(curso[5]),curso[6]))

Controller().readFile()