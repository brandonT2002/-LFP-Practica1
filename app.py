import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
from idlelib.tooltip import Hovertip
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

        self.manageCourses = customtkinter.CTkButton(master=self.frameLeft,text="Gestionar Cursos")
        self.manageCourses.grid(row=3,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frameLeft,text="Conteo de Creditos")
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
        self.getCourses.grid(row=0,column=0,pady=(20,0),padx=(20,5),sticky="nwe")

        self.showCourses = customtkinter.CTkButton(master=self.frameRight1,text="Mostrar Cursos",fg_color="gray40",hover_color="gray25",command=self.option2)
        self.showCourses.grid(row=0,column=1,pady=(20,0),padx=5,sticky="nwe")

        self.addCourse = customtkinter.CTkButton(master=self.frameRight1,text="Agregar Curso",fg_color="gray40",hover_color="gray25",command=self.option3)
        self.addCourse.grid(row=0,column=2,pady=(20,0),padx=5,sticky="nwe")

        self.editCourse = customtkinter.CTkButton(master=self.frameRight1,text="Editar Curso",fg_color="gray40",hover_color="gray25",command=self.option4)
        self.editCourse.grid(row=0,column=3,pady=(20,0),padx=5,sticky="nwe")

        self.deleteCourse = customtkinter.CTkButton(master=self.frameRight1,text="Eliminar Curso",fg_color="gray40",hover_color="gray25",command=self.option5)
        self.deleteCourse.grid(row=0,column=4,pady=(20,0),padx=(5,20),sticky="nwe")

        self.route = customtkinter.CTkEntry(master=self.frameRight1,width=120,placeholder_text="Ruta del archivo")
        self.route.grid(row=1,column=0,columnspan=5,pady=(15,10),padx=20,sticky="nwe")

        self.getCourses.configure(state=tkinter.DISABLED)
        
        self.panelshowCourses()
        self.tableCourses()
        self.panelAddCourse()
        self.panelEditCourses()
        self.panelDeleteCourse()
        self.panelShow.grid_remove()
        self.panelAdd.grid_remove()
        self.panelEdit.grid_remove()
        self.panelDelete.grid_remove()

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
        self.text = customtkinter.CTkLabel(master=self.table,text = "Opcionalidad",width=150).grid(row=0,column=3,sticky="we")
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
            if int(self.results[i].mandatory) == 1:
                exec(f"self.e{i}mandatory.insert('end','Obligatorio')")
            elif int(self.results[i].mandatory) == 0:
                exec(f"self.e{i}mandatory.insert('end','Opcional')")
            else:
                exec(f"self.e{i}mandatory.insert('end','Error')")
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
            if int(self.results[i].state) == 0:
                exec(f"self.e{i}state.insert('end','Aprobado')")
            elif int(self.results[i].state) == 1:
                exec(f"self.e{i}state.insert('end','Cursando')")
            elif int(self.results[i].state) == -1:
                exec(f"self.e{i}state.insert('end','Pendiente')")
            else:
                exec(f"self.e{i}state.insert('end','Error')")
            exec(f"self.e{i}state.configure(state=tkinter.DISABLED)")

    def panelshowCourses(self):        
        self.panelShow = customtkinter.CTkFrame(master=self.frameRight1)
        self.panelShow.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nwe")
        self.panelShow.rowconfigure(0, weight=1)
        self.panelShow.columnconfigure(0, weight=1)

        self.codeE = customtkinter.CTkEntry(master=self.panelShow,width=120,height=40,placeholder_text="Ingrese el Código del Curso")
        self.codeE.grid(row=1,column=0,columnspan=6,pady=20,padx=20,sticky="nwe")

        self.searchCourse = customtkinter.CTkButton(master=self.panelShow,text="Buscar Curso",height=40,fg_color="gray40",hover_color="gray25",command=self.getCode)
        self.searchCourse.grid(row=1,column=6,pady=20,padx=(5,20),sticky="nwe")

        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Código",width=50).grid(row=2,column=0,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Nombre",width=250).grid(row=2,column=1,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Prerrequisitos",width=150).grid(row=2,column=2,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelShow,text = "Opcionalidad",width=150).grid(row=2,column=3,sticky="we")
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
            if int(self.courseFound.mandatory) == 1:
                exec(f"self.e{i}mandatoryS.insert('end','Obligatorio')")
            elif int(self.courseFound.mandatory) == 0:
                exec(f"self.e{i}mandatoryS.insert('end','Opcional')")
            else:
                exec(f"self.e{i}mandatoryS.insert('end','Error')")
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
            if int(self.courseFound.state) == 0:
                exec(f"self.e{i}stateS.insert('end','Aprobado')")
            elif int(self.courseFound.state) == 1:
                exec(f"self.e{i}stateS.insert('end','Cursando')")
            elif int(self.courseFound.state) == -1:
                exec(f"self.e{i}stateS.insert('end','Pendiente')")
            else:
                exec(f"self.e{i}stateS.insert('end','Error')")
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
        self.panelAdd.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nswe")
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
        self.myTip = Hovertip(self.prerequisiteAdd,'\n     Ingrese los prerrequisitos separados por punto y coma     \n')

        self.creditsAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Creditos")
        self.creditsAdd.grid(row=2,column=2,columnspan=2,pady=(20,10),padx=(0,120),sticky="ne")

        self.semesterAdd = customtkinter.CTkEntry(master=self.panelAdd,width=400,height=40,placeholder_text="Semestre")
        self.semesterAdd.grid(row=3,column=0,columnspan=2,pady=(20,10),padx=(120,0),sticky="nw")

        self.mandatoryAdd = customtkinter.CTkComboBox(master=self.panelAdd,values=["Obligatorio","Opcional"],width=400,height=40)
        self.mandatoryAdd.grid(row=3,column=2,columnspan=2,pady=(20,10),padx=(0,120),sticky="ne")
        self.mandatoryAdd.set("Opcionalidad")

        self.stateAdd = customtkinter.CTkComboBox(master=self.panelAdd,values=["Aprobado","Cursando","Pendiente"],width=400,height=40)
        self.stateAdd.grid(row=4,column=0,columnspan=3,pady=(20,10),padx=(120,0),sticky="nwe")
        self.stateAdd.set("Estado")

        self.btnAddC = customtkinter.CTkButton(master=self.panelAdd,text="Agregar Curso",width=800,height=40,text_font=("Roboto Medium",12),command=self.addC)
        self.btnAddC.grid(row=9,column=0,columnspan=3,pady=(20,80),padx=(120,0),sticky="nwe")

    def addC(self):
        code = self.codeAdd.get()
        name = self.nameAdd.get()
        prerequisite = self.prerequisiteAdd.get()
        credits = self.creditsAdd.get()
        semester = self.semesterAdd.get()
        mandatory = self.mandatoryAdd.get()
        state = self.stateAdd.get()

        if mandatory == 'Opcional':
            mandatory = 1
        else:
            mandatory = 0

        if state == 'Aprobado':
            state = 0
        elif state == 'Cursando':
            state = 1
        else:
            state = -1
            
        if code == '' or name == '' or credits == '' or semester == '' or mandatory == 'Opcionalidad' or state == 'Estado':
            messagebox.showinfo("Información", "Todos los campos son obligatorios")
        else:
            try:
                int(code)
                int(credits)
                int(semester)
                if self.data.addCourse(code,name,prerequisite,mandatory,semester,credits,state):
                    messagebox.showinfo("Información", "Curso agregado exitosamente")
                    self.tableCourses()
                    self.table.grid_remove()

                    self.codeAdd.delete(0, 'end')
                    self.nameAdd.delete(0, 'end')
                    self.prerequisiteAdd.delete(0, 'end')
                    self.creditsAdd.delete(0, 'end')
                    self.semesterAdd.delete(0, 'end')
                    self.mandatoryAdd.set("Opcionalidad")
                    self.stateAdd.set("Estado")
                else:
                    messagebox.showinfo("Información", "El curso ya existe en el sistema, código duplicado")
                    self.codeAdd.delete(0, 'end')
            except: 
                messagebox.showinfo("Información", "Datos Incorrectos")

    def panelEditCourses(self):        
        self.panelEdit = customtkinter.CTkFrame(master=self.frameRight1)
        self.panelEdit.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nswe")
        self.panelEdit.rowconfigure(0, weight=1)
        self.panelEdit.columnconfigure(0, weight=1)

        self.codeEd = customtkinter.CTkEntry(master=self.panelEdit,width=120,height=40,placeholder_text="Ingrese el Código del Curso")
        self.codeEd.grid(row=1,column=0,columnspan=6,pady=20,padx=20,sticky="nwe")

        self.searchCEdit = customtkinter.CTkButton(master=self.panelEdit,text="Buscar Curso",height=40,fg_color="gray40",hover_color="gray25",command=self.btnSearchEdit)
        self.searchCEdit.grid(row=1,column=6,pady=20,padx=(5,20),sticky="nwe")

        titleE = customtkinter.CTkLabel(master=self.panelEdit,text="Editar Curso",text_font=("Roboto Medium",16))
        titleE.grid(row=2,column=0,columnspan=7,pady=(20,10),padx=10)

        self.codeEdit = customtkinter.CTkEntry(master=self.panelEdit,width=400,height=40,placeholder_text="Código")
        self.codeEdit.grid(row=3,column=0,columnspan=3,pady=(20,10),padx=(120,0),sticky="nw")
        self.codeEdit.configure(state=tkinter.DISABLED)

        self.nameEdit = customtkinter.CTkEntry(master=self.panelEdit,width=400,height=40,placeholder_text="Nombre")
        self.nameEdit.grid(row=3,column=4,columnspan=3,pady=(20,10),padx=(0,120),sticky="ne")
        self.nameEdit.configure(state=tkinter.DISABLED)

        self.prerequisiteEdit = customtkinter.CTkEntry(master=self.panelEdit,width=400,height=40,placeholder_text="Prerrequisito")
        self.prerequisiteEdit.grid(row=4,column=0,columnspan=3,pady=(20,10),padx=(120,0),sticky="nw")
        self.prerequisiteEdit.configure(state=tkinter.DISABLED)
        self.myTip = Hovertip(self.prerequisiteEdit,'\n     Ingrese los prerrequisitos separados por punto y coma     \n')

        self.creditsEdit = customtkinter.CTkEntry(master=self.panelEdit,width=400,height=40,placeholder_text="Creditos")
        self.creditsEdit.grid(row=4,column=4,columnspan=3,pady=(20,10),padx=(0,120),sticky="ne")
        self.creditsEdit.configure(state=tkinter.DISABLED)

        self.semesterEdit = customtkinter.CTkEntry(master=self.panelEdit,width=400,height=40,placeholder_text="Semestre")
        self.semesterEdit.grid(row=5,column=0,columnspan=3,pady=(20,10),padx=(120,0),sticky="nw")
        self.semesterEdit.configure(state=tkinter.DISABLED)

        self.mandatoryEdit = customtkinter.CTkComboBox(master=self.panelEdit,values=["Obligatorio","Opcional"],width=400,height=40)
        self.mandatoryEdit.grid(row=5,column=4,columnspan=3,pady=(20,10),padx=(0,120),sticky="ne")
        self.mandatoryEdit.set("Opcionalidad")
        self.mandatoryEdit.configure(state=tkinter.DISABLED)

        self.stateEdit = customtkinter.CTkComboBox(master=self.panelEdit,values=["Aprobado","Cursando","Pendiente"],width=400,height=40)
        self.stateEdit.grid(row=6,column=0,columnspan=7,pady=(20,10),padx=(120,120),sticky="nwe")
        self.stateEdit.set("Estado")
        self.stateEdit.configure(state=tkinter.DISABLED)

        self.btnEnableEdit = customtkinter.CTkButton(master=self.panelEdit,text="Editar",width=400,height=40,text_font=("Roboto Medium",12),command=self.enableEditing)
        self.btnEnableEdit.grid(row=7,column=0,columnspan=7,pady=(20,80),padx=(120,120),sticky="nwe")
        self.btnEnableEdit.configure(state=tkinter.DISABLED)

    def btnSearchEdit(self):
        codeV = self.codeEd.get()
        if codeV == '':
            messagebox.showinfo("Información", "Debe ingresar un código de curso")
            self.resetFormEdit()
        else:
            try:
                course = self.data.checkCourse(int(codeV))
                if course:
                    self.codeEd.delete(0, 'end')
                    self.codeEd.insert(0,'')

                    self.codeEdit.configure(state=tkinter.NORMAL)
                    self.nameEdit.configure(state=tkinter.NORMAL)
                    self.prerequisiteEdit.configure(state=tkinter.NORMAL)
                    self.creditsEdit.configure(state=tkinter.NORMAL)
                    self.semesterEdit.configure(state=tkinter.NORMAL)
                    self.mandatoryEdit.configure(state=tkinter.NORMAL)
                    self.stateEdit.configure(state=tkinter.NORMAL)

                    self.codeEdit.delete(0,'end')
                    self.nameEdit.delete(0,'end')
                    self.prerequisiteEdit.delete(0,'end')
                    self.creditsEdit.delete(0,'end')
                    self.semesterEdit.delete(0,'end')

                    pre = ''
                    for pr in course.prerequisite:
                        pre += pr + ' '

                    self.codeEdit.insert(0,str(course.code))
                    self.nameEdit.insert(0,str(course.name))
                    self.prerequisiteEdit.insert(0,str(pre))
                    self.creditsEdit.insert(0,str(course.credits))
                    self.semesterEdit.insert(0,str(course.semester))
                    if int(course.mandatory) == 1:
                        self.mandatoryEdit.set('Obligatorio')
                    elif int(course.mandatory) == 0:
                        self.mandatoryEdit.set('Opcional')
                    else:
                        self.mandatoryEdit.set('Error')

                    if int(course.state) == 0:
                        self.stateEdit.set('Aprobado')
                    elif int(course.state) == 1:
                        self.stateEdit.set('Cursando')
                    elif int(course.state) == -1:
                        self.stateEdit.set('Pendiente')
                    else:
                        self.stateEdit.set('Error')

                    self.codeEdit.configure(state=tkinter.DISABLED)
                    self.nameEdit.configure(state=tkinter.DISABLED)
                    self.prerequisiteEdit.configure(state=tkinter.DISABLED)
                    self.creditsEdit.configure(state=tkinter.DISABLED)
                    self.semesterEdit.configure(state=tkinter.DISABLED)
                    self.mandatoryEdit.configure(state=tkinter.DISABLED)
                    self.stateEdit.configure(state=tkinter.DISABLED)
                    self.btnEnableEdit.configure(state=tkinter.NORMAL)
                else:
                    messagebox.showinfo("Información", "El curso no existe")
                    self.codeEd.delete(0, 'end')
                    self.codeEd.insert(0,str(''))
                    self.resetFormEdit()
            except:
                messagebox.showinfo("Información", "Debe ingresar solo números")
                self.codeEd.delete(0, 'end')
                self.codeEd.insert(0,str(''))
                self.resetFormEdit()

    def enableEditing(self):
        self.btnEnableEdit.grid_remove()
        self.codeEd.configure(state=tkinter.DISABLED)
        self.searchCEdit.configure(state=tkinter.DISABLED)

        self.btnEdit = customtkinter.CTkButton(master=self.panelEdit,text="Guardar",width=400,height=40,text_font=("Roboto Medium",12),command=self.save)
        self.btnEdit.grid(row=7,column=0,columnspan=3,pady=(20,80),padx=(120,0),sticky="nw")

        self.btnCancel = customtkinter.CTkButton(master=self.panelEdit,text="Cancelar",fg_color="#D35B58",hover_color="#C77C78",width=400,height=40,text_font=("Roboto Medium",12),command=self.disableEditing)
        self.btnCancel.grid(row=7,column=4,columnspan=3,pady=(20,80),padx=(0,120),sticky="ne")

        self.nameEdit.configure(state=tkinter.NORMAL)
        self.prerequisiteEdit.configure(state=tkinter.NORMAL)
        self.creditsEdit.configure(state=tkinter.NORMAL)
        self.semesterEdit.configure(state=tkinter.NORMAL)
        self.mandatoryEdit.configure(state=tkinter.NORMAL)
        self.stateEdit.configure(state=tkinter.NORMAL)

    def disableEditing(self):
        self.btnEdit.grid_remove()
        self.btnCancel.grid_remove()
        self.btnEnableEdit.grid()

        codeV = self.codeEdit.get()

        self.nameEdit.delete(0,'end')
        self.prerequisiteEdit.delete(0,'end')
        self.creditsEdit.delete(0,'end')
        self.semesterEdit.delete(0,'end')

        pre = ''
        for pr in self.data.checkCourse(int(codeV)).prerequisite:
            pre += pr + ' '

        self.nameEdit.insert(0,str(self.data.checkCourse(int(codeV)).name))
        self.prerequisiteEdit.insert(0,str(pre))
        self.creditsEdit.insert(0,str(self.data.checkCourse(int(codeV)).credits))
        self.semesterEdit.insert(0,str(self.data.checkCourse(int(codeV)).semester))
        if int(self.data.checkCourse(int(codeV)).mandatory) == 1:
            self.mandatoryEdit.set('Obligatorio')
        elif int(self.data.checkCourse(int(codeV)).mandatory) == 0:
            self.mandatoryEdit.set('Opcional')
        else:
            self.mandatoryEdit.set('Error')

        if int(self.data.checkCourse(int(codeV)).state) == 0:
            self.stateEdit.set('Aprobado')
        elif int(self.data.checkCourse(int(codeV)).state) == 1:
            self.stateEdit.set('Cursando')
        elif int(self.data.checkCourse(int(codeV)).state) == -1:
            self.stateEdit.set('Pendiente')
        else:
            self.stateEdit.set('Error')

        
        self.codeEdit.configure(state=tkinter.DISABLED)
        self.nameEdit.configure(state=tkinter.DISABLED)
        self.prerequisiteEdit.configure(state=tkinter.DISABLED)
        self.creditsEdit.configure(state=tkinter.DISABLED)
        self.semesterEdit.configure(state=tkinter.DISABLED)
        self.mandatoryEdit.configure(state=tkinter.DISABLED)
        self.stateEdit.configure(state=tkinter.DISABLED)

        self.codeEd.configure(state=tkinter.NORMAL)
        self.searchCEdit.configure(state=tkinter.NORMAL)

    def save(self):
        code = self.codeEdit.get()
        name = self.nameEdit.get()
        prerequisite = self.prerequisiteEdit.get()
        credits = self.creditsEdit.get()
        semester = self.semesterEdit.get()
        mandatory = self.mandatoryEdit.get()
        state = self.stateEdit.get()

        if mandatory == 'Opcional':
            mandatory = 1
        else:
            mandatory = 0

        if state == 'Aprobado':
            state = 0
        elif state == 'Cursando':
            state = 1
        else:
            state = -1

        if name == '' or credits == '' or semester == '' or mandatory == 'Opcionalidad' or state == 'Estado':
            messagebox.showinfo("Información", "Todos los campos son obligatorios")
        else:
            try:
                if self.data.editCourse(int(code),name,prerequisite,mandatory,int(semester),int(credits),state):
                    messagebox.showinfo("Información", "Curso actualizado exitosamente")
                    self.reset()
            except:
                messagebox.showinfo("Información", "Datos Incorrectos")

    def panelDeleteCourse(self):        
        self.panelDelete = customtkinter.CTkFrame(master=self.frameRight1)
        self.panelDelete.grid(row=2,column=0,columnspan=5,rowspan=5,padx=20,pady=(10,20),sticky="nwe")
        self.panelDelete.rowconfigure(0, weight=1)
        self.panelDelete.columnconfigure(0, weight=1)

        self.codeD = customtkinter.CTkEntry(master=self.panelDelete,width=120,height=40,placeholder_text="Ingrese el Código del Curso")
        self.codeD.grid(row=1,column=0,columnspan=6,pady=20,padx=20,sticky="nwe")

        self.deleteC = customtkinter.CTkButton(master=self.panelDelete,text="Eliminar Curso",height=40,fg_color="gray40",hover_color="gray25",command=self.getCodeDelete)
        self.deleteC.grid(row=1,column=6,pady=20,padx=(5,20),sticky="nwe")

        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Código",width=50).grid(row=2,column=0,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Nombre",width=250).grid(row=2,column=1,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Prerrequisitos",width=150).grid(row=2,column=2,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Opcionalidad",width=150).grid(row=2,column=3,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Semestre",width=150).grid(row=2,column=4,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Creditos",width=150).grid(row=2,column=5,sticky="we")
        self.text = customtkinter.CTkLabel(master=self.panelDelete,text = "Estado",width=150).grid(row=2,column=6,sticky="we")

        self.btnDelete = customtkinter.CTkButton(master=self.panelDelete,text="Confirmar Eliminación",fg_color="#D35B58",hover_color="#C77C78",width=200,height=40,text_font=("Roboto Medium",12),command=self.delete)
        self.btnDelete.grid(row=7,column=1,columnspan=3,pady=(20,50),padx=(190,0),sticky="nw")

        self.btnCancelD = customtkinter.CTkButton(master=self.panelDelete,text="Cancelar",width=200,height=40,text_font=("Roboto Medium",12),command=self.cancelDelete)
        self.btnCancelD.grid(row=7,column=3,columnspan=3,pady=(20,50),padx=(0,190),sticky="ne")

        self.btnDelete.grid_remove()
        self.btnCancelD.grid_remove()

    def getCodeDelete(self):
        result = self.codeD.get()
        if result == '':
            messagebox.showinfo("Información", "Debe ingresar un Código de Curso")
        else:
            try:
                self.courseFound = self.data.searchCourse(int(result))
                if self.courseFound:
                    self.tableDataDelete()
                    self.btnDelete.grid()
                    self.btnCancelD.grid()
                    self.codeD.configure(state=tkinter.DISABLED)
                    self.deleteC.configure(state=tkinter.DISABLED)
                else:
                    messagebox.showinfo("Información", "El curso no existe")
                    self.codeD.delete(0, 'end')
                    self.codeD.insert(0,str(''))
            except:
                messagebox.showinfo("Información", "Debe ingresar solo números")
                self.codeD.delete(0, 'end')
                self.codeD.insert(0,str(''))

    def tableDataDelete(self):
        for i in range(1):
            exec(f"self.e{i}codeD = customtkinter.CTkEntry(self.panelDelete,width=50)")
            exec(f"self.e{i}codeD.grid(row={i+3},column=0,columnspan=1,sticky='we')")
            exec(f"self.e{i}codeD.insert('end',self.courseFound.code)")
            exec(f"self.e{i}codeD.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}nameD = customtkinter.CTkEntry(self.panelDelete,width=150)")
            exec(f"self.e{i}nameD.grid(row={i+3},column=1,columnspan=1,sticky='we')")
            exec(f"self.e{i}nameD.insert('end',self.courseFound.name)")
            exec(f"self.e{i}nameD.configure(state=tkinter.DISABLED)")

            pre = ''
            for pr in self.courseFound.prerequisite:
                pre += pr + ' '
            exec(f"self.e{i}prerequisiteD = customtkinter.CTkEntry(self.panelDelete,width=150)")
            exec(f"self.e{i}prerequisiteD.grid(row={i+3},column=2,columnspan=1,sticky='e')")
            exec(f"self.e{i}prerequisiteD.insert('end','{pre}')")
            exec(f"self.e{i}prerequisiteD.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}mandatoryD = customtkinter.CTkEntry(self.panelDelete,width=150)")
            exec(f"self.e{i}mandatoryD.grid(row={i+3},column=3,columnspan=1,sticky='we')")
            if int(self.courseFound.mandatory) == 1:
                exec(f"self.e{i}mandatoryD.insert('end','Obligatorio')")
            elif int(self.courseFound.mandatory) == 0:
                exec(f"self.e{i}mandatoryD.insert('end','Opcional')")
            else:
                exec(f"self.e{i}mandatoryD.insert('end','Error')")
            exec(f"self.e{i}mandatoryD.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}semesterD = customtkinter.CTkEntry(self.panelDelete,width=150)")
            exec(f"self.e{i}semesterD.grid(row={i+3},column=4,columnspan=1,sticky='we')")
            exec(f"self.e{i}semesterD.insert('end',self.courseFound.semester)")
            exec(f"self.e{i}semesterD.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}creditsD = customtkinter.CTkEntry(self.panelDelete,width=150)")
            exec(f"self.e{i}creditsD.grid(row={i+3},column=5,columnspan=1,sticky='we')")
            exec(f"self.e{i}creditsD.insert('end',self.courseFound.credits)")
            exec(f"self.e{i}creditsD.configure(state=tkinter.DISABLED)")

            exec(f"self.e{i}stateD = customtkinter.CTkEntry(self.panelDelete,width=150)")
            exec(f"self.e{i}stateD.grid(row={i+3},column=6,columnspan=1,sticky='we')")
            if int(self.courseFound.state) == 0:
                exec(f"self.e{i}stateD.insert('end','Aprobado')")
            elif int(self.courseFound.state) == 1:
                exec(f"self.e{i}stateD.insert('end','Cursando')")
            elif int(self.courseFound.state) == -1:
                exec(f"self.e{i}stateD.insert('end','Pendiente')")
            else:
                exec(f"self.e{i}stateD.insert('end','Error')")
            exec(f"self.e{i}stateD.configure(state=tkinter.DISABLED)")

    def cancelDelete(self):
        self.btnDelete.grid_remove()
        self.btnCancelD.grid_remove()
        self.codeD.configure(state=tkinter.NORMAL)
        self.deleteC.configure(state=tkinter.NORMAL)
        self.codeD.delete(0, 'end')
        self.codeD.insert(0,str(''))

        for i in range(1):
            exec(f"self.e{i}codeD.grid_remove()")
            exec(f"self.e{i}nameD.grid_remove()")
            exec(f"self.e{i}prerequisiteD.grid_remove()")
            exec(f"self.e{i}mandatoryD.grid_remove()")
            exec(f"self.e{i}semesterD.grid_remove()")
            exec(f"self.e{i}creditsD.grid_remove()")
            exec(f"self.e{i}stateD.grid_remove()")

    def delete(self):
        code = self.codeD.get()
        if code == '':
            messagebox.showinfo("Información", "Debe ingresar un código de curso")
        else:
            try:
                if self.data.deleteCourse(int(code)):
                    messagebox.showinfo("Información", "Curso eliminado exitosamente")
                    self.tableCourses()
                    self.table.grid_remove()
                    self.btnDelete.grid_remove()
                    self.btnCancelD.grid_remove()
                    self.codeD.configure(state=tkinter.NORMAL)
                    self.deleteC.configure(state=tkinter.NORMAL)
                    self.codeD.delete(0, 'end')
                    self.codeD.insert(0,str(''))

                    for i in range(1):
                        exec(f"self.e{i}codeD.grid_remove()")
                        exec(f"self.e{i}nameD.grid_remove()")
                        exec(f"self.e{i}prerequisiteD.grid_remove()")
                        exec(f"self.e{i}mandatoryD.grid_remove()")
                        exec(f"self.e{i}semesterD.grid_remove()")
                        exec(f"self.e{i}creditsD.grid_remove()")
                        exec(f"self.e{i}stateD.grid_remove()")
                else:
                    messagebox.showinfo("Información", "El curso no existe")
                    self.codeD.delete(0, 'end')
                    self.codeD.insert(0,str(''))
            except:
                messagebox.showinfo("Información", "Debe ingresar solo numeros")
                self.codeD.delete(0, 'end')
                self.codeD.insert(0,str(''))

    def selectFile(self):
        try:
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
        except:
            messagebox.showinfo("Información", "No se ha cargado niugún archivo")

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
        self.panelEdit.grid_remove()
        self.panelDelete.grid_remove()
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
        self.panelEdit.grid_remove()
        self.panelDelete.grid_remove()
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
        self.panelEdit.grid_remove()
        self.panelDelete.grid_remove()
        self.panelAdd.grid()

    def option4(self):
        self.getCourses.configure(state=tkinter.NORMAL)
        self.showCourses.configure(state=tkinter.NORMAL)
        self.addCourse.configure(state=tkinter.NORMAL)
        self.editCourse.configure(state=tkinter.DISABLED)
        self.deleteCourse.configure(state=tkinter.NORMAL)
        self.route.configure(state=tkinter.DISABLED)

        self.table.grid_remove()
        self.panelShow.grid_remove()
        self.panelAdd.grid_remove()
        self.panelDelete.grid_remove()
        self.panelEdit.grid()

    def option5(self):
        self.getCourses.configure(state=tkinter.NORMAL)
        self.showCourses.configure(state=tkinter.NORMAL)
        self.addCourse.configure(state=tkinter.NORMAL)
        self.editCourse.configure(state=tkinter.NORMAL)
        self.deleteCourse.configure(state=tkinter.DISABLED)
        self.route.configure(state=tkinter.DISABLED)

        self.table.grid_remove()
        self.panelShow.grid_remove()
        self.panelAdd.grid_remove()
        self.panelEdit.grid_remove()
        self.panelDelete.grid()

    def resetFormEdit(self):
        self.codeEdit.configure(state=tkinter.NORMAL)
        self.nameEdit.configure(state=tkinter.NORMAL)
        self.prerequisiteEdit.configure(state=tkinter.NORMAL)
        self.creditsEdit.configure(state=tkinter.NORMAL)
        self.semesterEdit.configure(state=tkinter.NORMAL)
        self.mandatoryEdit.configure(state=tkinter.NORMAL)
        self.stateEdit.configure(state=tkinter.NORMAL)
        self.codeEdit.delete(0, 'end')
        self.nameEdit.delete(0, 'end')
        self.prerequisiteEdit.delete(0, 'end')
        self.creditsEdit.delete(0, 'end')
        self.semesterEdit.delete(0, 'end')
        self.mandatoryEdit.set("Opcionalidad")
        self.stateEdit.set("Estado")
        self.codeEdit.configure(state=tkinter.DISABLED)
        self.nameEdit.configure(state=tkinter.DISABLED)
        self.prerequisiteEdit.configure(state=tkinter.DISABLED)
        self.creditsEdit.configure(state=tkinter.DISABLED)
        self.semesterEdit.configure(state=tkinter.DISABLED)
        self.mandatoryEdit.configure(state=tkinter.DISABLED)
        self.stateEdit.configure(state=tkinter.DISABLED)
        self.btnEnableEdit.configure(state=tkinter.DISABLED)

    def reset(self):
        self.tableCourses()
        self.table.grid_remove()
        self.btnEdit.grid_remove()
        self.btnCancel.grid_remove()
        self.btnEnableEdit.grid()

        self.codeEdit.configure(state=tkinter.NORMAL)
        self.codeEdit.delete(0, 'end')
        self.nameEdit.delete(0, 'end')
        self.prerequisiteEdit.delete(0, 'end')
        self.creditsEdit.delete(0, 'end')
        self.semesterEdit.delete(0, 'end')
        self.mandatoryEdit.set("Opcionalidad")
        self.stateEdit.set("Estado")
        self.codeEdit.configure(state=tkinter.DISABLED)
        self.nameEdit.configure(state=tkinter.DISABLED)
        self.prerequisiteEdit.configure(state=tkinter.DISABLED)
        self.creditsEdit.configure(state=tkinter.DISABLED)
        self.semesterEdit.configure(state=tkinter.DISABLED)
        self.mandatoryEdit.configure(state=tkinter.DISABLED)
        self.stateEdit.configure(state=tkinter.DISABLED)
        self.btnEnableEdit.configure(state=tkinter.DISABLED)
        self.codeEd.configure(state=tkinter.NORMAL)
        self.searchCEdit.configure(state=tkinter.NORMAL)

    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()