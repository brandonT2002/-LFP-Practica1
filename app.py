import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class menu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Práctica1 - LFP")
        self.window.resizable(False, False)
        self.window.state('zoomed')
        self.colorButton=("gray77")
        self.titles()
        self.buttons()

        self.window.mainloop()

    def titles(self):
        self.title = tk.Label(self.window, text='Lenguajes Formales y de Programación')
        self.title.pack(anchor=tk.CENTER,ipady=10)
        self.title.config(font=('Verdana',24)) 

        self.name = tk.Label(self.window, text='Brandon Andy Jefferson Tejaxún Pichiyá')
        self.name.pack(anchor=tk.CENTER,ipady=10)
        self.name.config(font=('Verdana',20))

        self.carne = tk.Label(self.window, text='202112030')
        self.carne.pack(anchor=tk.CENTER,ipady=10)
        self.carne.config(font=('Verdana',20))

    def buttons(self):
        self.fileUpload = tk.Button(self.window,text="Cargar Archivo",bg=self.colorButton,width=16,height=2,command=self.selectFile)
        self.fileUpload.place(x=600,y=250)
        self.fileUpload.config(font=('Verdana',12))

        self.manageCourses = tk.Button(self.window,text="Gestionar Cursos",bg=self.colorButton,width=16,height=2,command=lambda:self.btnClik())
        self.manageCourses.place(x=600,y=320)
        self.manageCourses.config(font=('Verdana',12))

        self.credits = tk.Button(self.window,text="Conteo de Créditos",bg=self.colorButton,width=16,height=2,command=lambda:self.btnClik())
        self.credits.place(x=600,y=390)
        self.credits.config(font=('Verdana',12))

        self.leave = tk.Button(self.window,text="Salir",bg=self.colorButton,width=16,height=2,command=self.window.quit)
        self.leave.place(x=600,y=460)
        self.leave.config(font=('Verdana',12))

    def selectFile(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        showinfo(
            title='Selected File',
            message=filename
        )

if __name__ == '__main__':
    app = menu()  