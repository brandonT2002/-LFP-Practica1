import tkinter
from tkinter import filedialog as fd
import customtkinter
from readData import Controller

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    WIDTH = 1250
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
        self.getCourses.grid(row=0,column=0,pady=10,padx=5)

        self.showCourses = customtkinter.CTkButton(master=self.frameRight1,text="Mostrar Cursos",fg_color="gray40",hover_color="gray25",command=self.option2)
        self.showCourses.grid(row=0,column=1,pady=10,padx=5)

        self.addCourse = customtkinter.CTkButton(master=self.frameRight1,text="Agregar Curso",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.addCourse.grid(row=0,column=2,pady=10,padx=5)

        self.editCourse = customtkinter.CTkButton(master=self.frameRight1,text="Editar Curso",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.editCourse.grid(row=0,column=3,pady=10,padx=5)

        self.deleteCourse = customtkinter.CTkButton(master=self.frameRight1,text="Eliminar Curso",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.deleteCourse.grid(row=0,column=4,pady=10,padx=5)

        self.route = customtkinter.CTkEntry(master=self.frameRight1,width=120,placeholder_text="Ruta del archivo")
        self.route.grid(row=1,column=0,columnspan=5,pady=20,padx=20,sticky="nwe")
        
        self.tableCourses()


    def tableCourses(self):
        self.table = customtkinter.CTkFrame(master=self.frameRight1)
        self.table.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=20,sticky="nwe")
        self.table.rowconfigure(0, weight=1)
        self.table.columnconfigure(0, weight=1)

        self.text = customtkinter.CTkLabel(master=self.table,text = "Código").grid(row=0,column=0,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Nombre").grid(row=0,column=1,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Prerrequisitos").grid(row=0,column=2,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Obligatorio").grid(row=0,column=3,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Semestre").grid(row=0,column=4,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Creditos").grid(row=0,column=5,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.table,text = "Estado").grid(row=0,column=6,sticky="we")
        
        self.tableData()

    def showCourses(self):        
        self.panel = customtkinter.CTkFrame(master=self.frameRight1)
        self.panel.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=20,sticky="nwe")
        self.panel.rowconfigure(0, weight=1)
        self.panel.columnconfigure(0, weight=1)


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

    def tableData(self):
        self.results = self.data.courses
        for i in range(len(self.results)):
            exec(f"self.e{i}code = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}code.grid(row={i}+1,column=0,columnspan=1,sticky='we')")
            exec(f"self.e{i}code.insert('end',self.results[{i}].code)")
            exec(f"self.e{i}code.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}name = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}name.grid(row={i}+1,column=1,columnspan=1,sticky='we')")
            exec(f"self.e{i}name.insert('end',self.results[{i}].name)")
            exec(f"self.e{i}name.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}prerequisite = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}prerequisite.grid(row={i}+1,column=2,columnspan=1,sticky='we')")
            exec(f"self.e{i}prerequisite.insert('end',self.results[{i}].prerequisite)")
            exec(f"self.e{i}prerequisite.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}mandatory = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}mandatory.grid(row={i}+1,column=3,columnspan=1,sticky='we')")
            exec(f"self.e{i}mandatory.insert('end',self.results[{i}].mandatory)")
            exec(f"self.e{i}mandatory.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}semester = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}semester.grid(row={i}+1,column=4,columnspan=1,sticky='we')")
            exec(f"self.e{i}semester.insert('end',self.results[{i}].semester)")
            exec(f"self.e{i}semester.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}credits = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}credits.grid(row={i}+1,column=5,columnspan=1,sticky='we')")
            exec(f"self.e{i}credits.insert('end',self.results[{i}].credits)")
            exec(f"self.e{i}credits.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}state = customtkinter.CTkEntry(self.table,width=150)")
            exec(f"self.e{i}state.grid(row={i}+1,column=6,columnspan=1,sticky='we')")
            exec(f"self.e{i}state.insert('end',self.results[{i}].state)")
            exec(f"self.e{i}state.configure(state=tkinter.DISABLED)")
            """
            for j in range(7):
                exec(f"self.e{i}_{j} = customtkinter.CTkEntry(self.table,width=150)")
                exec(f"self.e{i}_{j}.grid(row={i}+1,column={j},columnspan=1,sticky='we')")
                exec("self.e"+str(i)+"_"+str(j)+".insert('end',self.results["+str(i)+"]["+str(j)+"])")
                exec(f"self.e{i}_{j}.configure(state=tkinter.DISABLED)")
            """
        print(self.data.courses)

    def option1(self):
        pass
        #self.panel.grid_forget()
        #self.table.grid()

    def option2(self):
        pass
        #self.table.grid_forget()

    def buttonEvent(self):
        pass
        #self.frameRight1.grid_forget()

    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
