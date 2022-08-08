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
        self.panelFileUpload()

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

    def panelFileUpload(self):
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
        self.showCourses = customtkinter.CTkButton(master=self.frameRight1,text="Mostrar Cursos",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.showCourses.grid(row=0,column=0,pady=10,padx=5)

        self.addCourse = customtkinter.CTkButton(master=self.frameRight1,text="Agregar Curso",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.addCourse.grid(row=0,column=1,pady=10,padx=5)

        self.editCourse = customtkinter.CTkButton(master=self.frameRight1,text="Editar Curso",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.editCourse.grid(row=0,column=2,pady=10,padx=5)

        self.deleteCourse = customtkinter.CTkButton(master=self.frameRight1,text="Eliminar Curso",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.deleteCourse.grid(row=0,column=3,pady=10,padx=5)

        self.toReturn = customtkinter.CTkButton(master=self.frameRight1,text="Regresar",fg_color="gray40",hover_color="gray25",command=self.buttonEvent)
        self.toReturn.grid(row=0,column=4,pady=10,padx=5)

        self.route = customtkinter.CTkEntry(master=self.frameRight1,width=120,placeholder_text="Ruta del archivo")
        self.route.grid(row=1,column=0,columnspan=5,pady=20,padx=20,sticky="nwe")

        self.tableCourses()


    def tableCourses(self):
        self.table = customtkinter.CTkFrame(master=self.frameRight1)
        self.table.grid(row=2,column=0,columnspan=5,padx=20,sticky="nsew")
        self.table.rowconfigure(0, weight=1)
        self.table.columnconfigure(0, weight=1)        

        self.text = customtkinter.CTkLabel(master=self.table,text = "Código").grid(row=0,column=0)
        self.text = customtkinter.CTkLabel(master=self.table,text = "Nombre").grid(row=0,column=1)
        self.text = customtkinter.CTkLabel(master=self.table,text = "Prerrequisitos").grid(row=0,column=2)
        self.text = customtkinter.CTkLabel(master=self.table,text = "Obligatorio").grid(row=0,column=3)
        self.text = customtkinter.CTkLabel(master=self.table,text = "Semestre").grid(row=0,column=4)
        self.text = customtkinter.CTkLabel(master=self.table,text = "Creditos").grid(row=0,column=5)
        self.text = customtkinter.CTkLabel(master=self.table,text = "Estado").grid(row=0,column=6)
        self.results=[
            ['017','Social Humanística 1','','1','1','4','0'],
            ['017','Social Humanística 1','','1','1','4','0'],
            ['017','Social Humanística 1','','1','1','4','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['147','Física Básica','101','1','2','5','0'],
            ['150','Física 1','103,147','1','3','6','1'],
            ['150','Física 1','103,147','1','3','6','1'],
            ['150','Física 1','103,147','1','3','6','1'],
            ['150','Física 1','103,147','1','3','6','1'],
            ['150','Física 1','103,147','1','3','6','1']]
        for i in range(len(self.results)):
            for j in range(7):
                exec(f"self.e{i}_{j} = customtkinter.CTkEntry(self.table,width=150)")
                exec(f"self.e{i}_{j}.grid(row={i}+1,column={j},columnspan=1,sticky='we')")
                exec("self.e"+str(i)+"_"+str(j)+".insert('end',self.results["+str(i)+"]["+str(j)+"])")
                exec(f"self.e{i}_{j}.configure(state=tkinter.DISABLED)")

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
        Controller().readFile(fileRoute)
        self.route.insert(0,str(fileRoute))
        self.route.configure(state=tkinter.DISABLED)

    def buttonEvent(self):
        pass
        #self.frameRight1.grid_forget()

    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
