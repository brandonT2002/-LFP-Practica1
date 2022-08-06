import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Practica1 - LFP")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frameLeft = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frameLeft.grid(row=0,column=0,sticky="nswe")

        self.frameRight = customtkinter.CTkFrame(master=self)
        self.frameRight.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

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

        self.manageCourses = customtkinter.CTkButton(master=self.frameLeft,text="Gestionar Cursos",command=self.button_event)
        self.manageCourses.grid(row=3,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frameLeft,text="Conteo de Creditos",command=self.button_event)
        self.credits.grid(row=4,column=0,pady=10,padx=20)

        self.credits = customtkinter.CTkButton(master=self.frameLeft,text="Salir",fg_color="#D35B58",hover_color="#C77C78",command=self.quit)
        self.credits.grid(row=9,column=0,pady=10,padx=20)

        # ============ frame_right ============
        # configure grid layout (3x7)
        self.frameRight.rowconfigure((0, 1, 2, 3), weight=1)
        self.frameRight.rowconfigure(7, weight=10)
        self.frameRight.columnconfigure((0, 1), weight=1)
        self.frameRight.columnconfigure(2, weight=0)
        """
        self.data = customtkinter.CTkLabel(master=self.frameRight,text="Lenguajes Formales y de Programación\nBrandon Andy J. Tejaxún Pichiyá\n202112030",height=70,corner_radius=6,fg_color=("white", "gray38"),justify=tkinter.CENTER)
        self.data.grid(column=0,row=0,columnspan=2,rowspan=4,sticky="nwe",padx=20,pady=20)
        self.data.config(font=('Roboto Medium',13))
        """
        self.route = customtkinter.CTkEntry(master=self.frameRight,width=120,placeholder_text="Ruta del archivo")
        self.route.grid(row=0,column=0,columnspan=2,pady=20,padx=20,sticky="nwe")

    def selectFile(self):
        self.route.configure(state=tkinter.NORMAL)
        self.route.delete(0, 'end')
        filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
        )
        fileRoute = fd.askopenfilename(
            title='Open a file',
            initialdir='',
            filetypes=filetypes)
        fichero = open(fileRoute,'r')
        text = fichero.read()
        print(text)
        self.route.insert(0,str(fileRoute))
        self.route.configure(state=tkinter.DISABLED)

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
