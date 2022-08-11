import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
import customtkinter
from readData import Controller

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    WIDTH = 1325
    HEIGHT = 600

    def __init__(self):
        super().__init__()
        self.data = Controller()

        self.title("Practica1 - LFP")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.minsize(App.WIDTH,App.HEIGHT)

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frameLeft = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frameLeft.grid(row=0,column=0,sticky="nswe")  

        self.frameRight1 = customtkinter.CTkFrame(master=self)
        self.frameRight1.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelOptions()
        self.panelManageCourses()

    def panelOptions(self):
        # ============ frame_left ============
        # configure grid layout (1x11)
        self.frameLeft.grid_rowconfigure(0, minsize=10)
        self.frameLeft.grid_rowconfigure(5, weight=1)
        self.frameLeft.grid_rowconfigure(8, minsize=20)
        self.frameLeft.grid_rowconfigure(11, minsize=10)

        self.options = customtkinter.CTkLabel(master=self.frameLeft,text="Opciones",text_font=("Roboto Medium",16))
        self.options.grid(row=1,column=0,pady=10,padx=10)

        self.fileUpload = customtkinter.CTkButton(master=self.frameLeft,text="Cargar Archivos",command=self.selectFile)
        self.fileUpload.grid(row=2,column=0,pady=10,padx=20)

        self.manageCourses = customtkinter.CTkButton(master=self.frameLeft,text="Gestionar Cursos",command=self.buttonEvent)
        self.manageCourses.grid(row=3,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frameLeft,text="Conteo de Creditos",command=self.buttonEvent)
        self.credits.grid(row=4,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frameLeft,text="Salir",fg_color="#D35B58",hover_color="#C77C78",command=self.quit)
        self.credits.grid(row=9,column=0,pady=10,padx=20)

    def panelManageCourses(self):
        # ============ frame_right ============
        # configure grid layout (3x7)
        self.frameRight1.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.frameRight1.rowconfigure(5, weight=10)
        self.frameRight1.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.frameRight1.columnconfigure(5, weight=0)
        """
        self.data = customtkinter.CTkLabel(master=self.frameRight1,text="Lenguajes Formales y de Programación\nBrandon Andy J. Tejaxún Pichiyá\n202112030",height=70,corner_radius=6,fg_color=("white", "gray38"),justify=tkinter.CENTER)
        self.data.grid(column=0,row=0,columnspan=2,rowspan=4,sticky="nwe",padx=20,pady=20)
        self.data.config(font=('Roboto Medium',13))
        """
        self.getCourses = customtkinter.CTkButton(master=self.frameRight1,text="Listar Cursos",fg_color="gray40",hover_color="gray25",command=self.option1)
        self.getCourses.grid(row=0,column=0,pady=10,padx=(20,5),sticky="nwe")

        self.showCourses = customtkinter.CTkButton(master=self.frameRight1,text="Mostrar Cursos",fg_color="gray40",hover_color="gray25",command=self.option2)
        self.showCourses.grid(row=0,column=1,pady=10,padx=5,sticky="nwe")

        self.addCourse = customtkinter.CTkButton(master=self.frameRight1,text="Agregar Curso",fg_color="gray40",hover_color="gray25",command=self.option3)
        self.addCourse.grid(row=0,column=2,pady=10,padx=5,sticky="nwe")

        self.editCourse = customtkinter.CTkButton(master=self.frameRight1,text="Editar Curso",fg_color="gray40",hover_color="gray25",command=self.option4)
        self.editCourse.grid(row=0,column=3,pady=10,padx=5,sticky="nwe")

        self.deleteCourse = customtkinter.CTkButton(master=self.frameRight1,text="Eliminar Curso",fg_color="gray40",hover_color="gray25",command=self.option5)
        self.deleteCourse.grid(row=0,column=4,pady=10,padx=(5,20),sticky="nwe")

        self.route = customtkinter.CTkEntry(master=self.frameRight1,width=120,placeholder_text="Ruta del archivo")
        self.route.grid(row=1,column=0,columnspan=5,pady=20,padx=20,sticky="we")

        self.getCourses.configure(state=tkinter.DISABLED)
        
        self.panelshowCourses()
        self.tableCourses()
        self.panelAddCourse()
        self.panelShow.grid_remove()
        self.panelAdd.grid_remove()

    def tableCourses(self):
        self.table = customtkinter.CTkFrame(master=self.frameRight1)
        self.table.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nwe")
        self.table.rowconfigure(0, weight=1)
        self.table.columnconfigure(0, weight=1)
        
        self.tableData()

    def tableData(self):
        self.results = self.data.courses
        
        self.text = customtkinter.CTkLabel(master=self.table,text = "Código",width=50).grid(row=0,column=0,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Nombre",width=250).grid(row=0,column=1,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Prerrequisitos",width=150).grid(row=0,column=2,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Obligatorio",width=150).grid(row=0,column=3,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Semestre",width=150).grid(row=0,column=4,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Creditos",width=150).grid(row=0,column=5,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Estado",width=150).grid(row=0,column=6,sticky="we")

        for i in range(len(self.results)):
            exec(f"self.e{i}code = customtkinter.CTkEntry(self.table,width=50)")
            exec(f"self.e{i}code.grid(row={i}+1,column=0,columnspan=1,sticky='we')")
            exec(f"self.e{i}code.insert('end',self.results[{i}].code)")
            exec(f"self.e{i}code.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}name = customtkinter.CTkEntry(self.table,width=250)")
            exec(f"self.e{i}name.grid(row={i}+1,column=1,columnspan=1,sticky='we')")
            exec(f"self.e{i}name.insert('end',self.results[{i}].name)")
            exec(f"self.e{i}name.configure(state=tkinter.DISABLED)")

            pre = ''
            for pr in self.results[i].prerequisite:
                pre += pr + ' '
            exec(f"self.e{i}prerequisite = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}prerequisite.grid(row={i}+1,column=2,columnspan=1,sticky='e')")
            exec(f"self.e{i}prerequisite.insert('end','{pre}')")
            exec(f"self.e{i}prerequisite.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}mandatory = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}mandatory.grid(row={i}+1,column=3,columnspan=1,sticky='e')")
            if self.results[i].mandatory == 1:
                exec(f"self.e{i}mandatory.insert('end','Obligatorio')")
            else:
                exec(f"self.e{i}mandatory.insert('end','Opcional')")
            exec(f"self.e{i}mandatory.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}semester = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}semester.grid(row={i}+1,column=4,columnspan=1,sticky='e')")
            exec(f"self.e{i}semester.insert('end',self.results[{i}].semester)")
            exec(f"self.e{i}semester.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}credits = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}credits.grid(row={i}+1,column=5,columnspan=1,sticky='e')")
            exec(f"self.e{i}credits.insert('end',self.results[{i}].credits)")
            exec(f"self.e{i}credits.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}state = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}state.grid(row={i}+1,column=6,columnspan=1,sticky='e')")
            if self.results[i].state == 0:
                exec(f"self.e{i}state.insert('end','Aprobado')")
            elif self.results[i].state == 1:
                exec(f"self.e{i}state.insert('end','Cursando')")
            else:
                exec(f"self.e{i}state.insert('end','Pendiente')")
            exec(f"self.e{i}state.configure(state=tkinter.DISABLED)")

    def panelshowCourses(self):        
        self.panelShow = customtkinter.CTkFrame(master=self.frameRight1)
        self.panelShow.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nwe")
        self.panelShow.rowconfigure(0, weight=1)
        self.panelShow.columnconfigure(0, weight=1)

        self.codeE = customtkinter.CTkEntry(master=self.panelShow,width=120,placeholder_text="Ingrese el Código del Curso")
        self.codeE.grid(row=1,column=0,columnspan=6,pady=20,padx=20,sticky="nwe")

        self.searchCourse = customtkinter.CTkButton(master=self.panelShow,text="Buscar Curso",fg_color="gray40",hover_color="gray25",command=self.getCode)
        self.searchCourse.grid(row=1,column=6,pady=20,padx=(5,20),sticky="nwe")

        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Código",width=50).grid(row=2,column=0,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Nombre",width=250).grid(row=2,column=1,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Prerrequisitos",width=150).grid(row=2,column=2,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Obligatorio",width=150).grid(row=2,column=3,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Semestre",width=150).grid(row=2,column=4,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Creditos",width=150).grid(row=2,column=5,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Estado",width=150).grid(row=2,column=6,sticky="we")

    def tableDataShow(self):
        for i in range(1):
            exec(f"self.e{i}codeS = customtkinter.CTkEntry(self.panelShow,width=50)")
            exec(f"self.e{i}codeS.grid(row={i+3},column=0,columnspan=1,sticky='we')")
            exec(f"self.e{i}codeS.insert('end',self.courseFound.code)")
            exec(f"self.e{i}codeS.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}nameS = customtkinter.CTkEntry(self.panelShow,width=150)")
            exec(f"self.e{i}nameS.grid(row={i+3},column=1,columnspan=1,sticky='we')")
            exec(f"self.e{i}nameS.insert('end',self.courseFound.name)")
            exec(f"self.e{i}nameS.configure(state=tkinter.DISABLED)")

            pre = ''
            for pr in self.courseFound.prerequisite:
                pre += pr + ' '
            exec(f"self.e{i}prerequisite = customtkinter.CTkEntry(self.panelShow,width=150)")
            exec(f"self.e{i}prerequisite.grid(row={i+3},column=2,columnspan=1,sticky='e')")
            exec(f"self.e{i}prerequisite.insert('end','{pre}')")
            exec(f"self.e{i}prerequisite.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}mandatoryS = customtkinter.CTkEntry(self.panelShow,width=150)")
            exec(f"self.e{i}mandatoryS.grid(row={i+3},column=3,columnspan=1,sticky='we')")
            if self.courseFound.mandatory == 1:
                exec(f"self.e{i}mandatoryS.insert('end','Obligatorio')")
            else:
                exec(f"self.e{i}mandatoryS.insert('end','Opcional')")
            exec(f"self.e{i}mandatoryS.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}semesterS = customtkinter.CTkEntry(self.panelShow,width=150)")
            exec(f"self.e{i}semesterS.grid(row={i+3},column=4,columnspan=1,sticky='we')")
            exec(f"self.e{i}semesterS.insert('end',self.courseFound.semester)")
            exec(f"self.e{i}semesterS.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}creditsS = customtkinter.CTkEntry(self.panelShow,width=150)")
            exec(f"self.e{i}creditsS.grid(row={i+3},column=5,columnspan=1,sticky='we')")
            exec(f"self.e{i}creditsS.insert('end',self.courseFound.credits)")
            exec(f"self.e{i}creditsS.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}stateS = customtkinter.CTkEntry(self.panelShow,width=150)")
            exec(f"self.e{i}stateS.grid(row={i+3},column=6,columnspan=1,sticky='we')")
            if self.courseFound.state == 0:
                exec(f"self.e{i}stateS.insert('end','Aprobado')")
            elif self.courseFound.state == 1:
                exec(f"self.e{i}stateS.insert('end','Cursando')")
            else:
                exec(f"self.e{i}stateS.insert('end','Pendiente')")
            exec(f"self.e{i}stateS.configure(state=tkinter.DISABLED)")

    def getCode(self):
        self.result = self.codeE.get()
        if self.result == '':
            messagebox.showinfo("Información", "Debe ingresar un Código de Curso")
        else:
            try:
                self.courseFound = self.data.searchCourse(int(self.result))
                if self.courseFound:
                    self.tableDataShow()
                    self.codeE.delete(0, 'end')
                    self.codeE.insert(0,str(''))
                else:
                    messagebox.showinfo("Información", "El curso no existe")
                    self.codeE.delete(0, 'end')
                    self.codeE.insert(0,str(''))
            except:
                messagebox.showinfo("Información", "Debe ingresar solo números")
                self.codeE.delete(0, 'end')
                self.codeE.insert(0,str(''))

    def panelAddCourse(self):        
        self.panelAdd = customtkinter.CTkFrame(master=self.frameRight1)
        self.panelAdd.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nwe")
        self.panelAdd.rowconfigure(0, weight=1)
        self.panelAdd.columnconfigure(0, weight=1)

        self.titleAdd = customtkinter.CTkLabel(master=self.panelAdd,text="Agregar Nuevo Curso",text_font=("Roboto Medium",16))
        self.titleAdd.grid(row=0,column=0,columnspan=7,pady=(20,10),padx=10)

        self.codeAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Código")
        self.codeAdd.grid(row=1,column=0,columnspan=2,pady=(20,10),padx=(120,0),sticky="nw")

        self.nameAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Nombre")
        self.nameAdd.grid(row=1,column=2,columnspan=2,pady=(20,10),padx=(0,120),sticky="ne")

        self.prerequisiteAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Prerrequisito")
        self.prerequisiteAdd.grid(row=2,column=0,columnspan=2,pady=(20,10),padx=(120,0),sticky="nw")

        self.mandatoryAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Obligatorio")
        self.mandatoryAdd.grid(row=2,column=2,columnspan=2,pady=(20,10),padx=(0,120),sticky="ne")

        self.semesterAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Semestre")
        self.semesterAdd.grid(row=3,column=0,columnspan=2,pady=(20,10),padx=(120,0),sticky="nw")

        self.creditsAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Creditos")
        self.creditsAdd.grid(row=3,column=2,columnspan=2,pady=(20,10),padx=(0,120),sticky="ne")

        self.searchCourse = customtkinter.CTkButton(master=self.panelAdd,text="Agregar Curso",width=800,height=40,text_font=("Roboto Medium",12),command=self.getCode)
        self.searchCourse.grid(row=9,column=0,columnspan=3,pady=(20,80),padx=(120,0),sticky="nwe")

    def selectFile(self):
        self.route.configure(state=tkinter.NORMAL)
        filetypes = (
            ('text files', '*.lfp'),
            ('All files', '*.*')
        )
        fileRoute = fd.askopenfilename(
            title='Open a file',
            initialdir='',
            filetypes=filetypes)
        self.route.delete(0, 'end')
        self.data.readFile(fileRoute)
        self.tableData()
        self.route.insert(0,str(fileRoute))
        self.route.configure(state=tkinter.DISABLED)

    def option1(self):
        self.getCourses.configure(state=tkinter.DISABLED)
        self.showCourses.configure(state=tkinter.NORMAL)
        self.addCourse.configure(state=tkinter.NORMAL)
        self.editCourse.configure(state=tkinter.NORMAL)
        self.deleteCourse.configure(state=tkinter.NORMAL)
        self.route.configure(state=tkinter.NORMAL)
        self.route.configure(state=tkinter.DISABLED)

        self.panelShow.grid_remove()
        self.panelAdd.grid_remove()
        self.table.grid()

    def option2(self):
        self.getCourses.configure(state=tkinter.NORMAL)
        self.showCourses.configure(state=tkinter.DISABLED)
        self.addCourse.configure(state=tkinter.NORMAL)
        self.editCourse.configure(state=tkinter.NORMAL)
        self.deleteCourse.configure(state=tkinter.NORMAL)
        self.route.configure(state=tkinter.DISABLED)

        self.table.grid_remove()
        self.panelAdd.grid_remove()
        self.panelShow.grid()

    def option3(self):
        self.getCourses.configure(state=tkinter.NORMAL)
        self.showCourses.configure(state=tkinter.NORMAL)
        self.addCourse.configure(state=tkinter.DISABLED)
        self.editCourse.configure(state=tkinter.NORMAL)
        self.deleteCourse.configure(state=tkinter.NORMAL)
        self.route.configure(state=tkinter.DISABLED)

        self.table.grid_remove()
        self.panelShow.grid_remove()
        self.panelAdd.grid()

    def option4(self):
        self.getCourses.configure(state=tkinter.NORMAL)
        self.showCourses.configure(state=tkinter.NORMAL)
        self.addCourse.configure(state=tkinter.NORMAL)
        self.editCourse.configure(state=tkinter.DISABLED)
        self.deleteCourse.configure(state=tkinter.NORMAL)
        self.route.configure(state=tkinter.DISABLED)

    def option5(self):
        self.getCourses.configure(state=tkinter.NORMAL)
        self.showCourses.configure(state=tkinter.NORMAL)
        self.addCourse.configure(state=tkinter.NORMAL)
        self.editCourse.configure(state=tkinter.NORMAL)
        self.deleteCourse.configure(state=tkinter.DISABLED)
        self.route.configure(state=tkinter.DISABLED)

    def buttonEvent(self):
        pass
        #self.frameRight1.grid_forget()

    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
