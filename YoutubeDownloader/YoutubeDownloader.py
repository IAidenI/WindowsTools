from tkinter import filedialog
from bin.package import *
from bin.colors import *
import tkinter as tk
import threading
import os


class GlobalMethode:
    def ColorMode(self):
        self.currentModeColor = not self.currentModeColor
        self.colors.DarkLightMode()
        self.allColors = self.colors.GetCurrentColor()
        self.configure(bg=self.allColors[self.BACKGROUND])
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.configure(bg=self.allColors[self.BACKGROUND])

        if self.currentModeColor:
            self.colorMode.config(image=self.lightMode)
        else:
            self.colorMode.config(image=self.darkMode)

    def StartThread(self, function, button):
        button.config(state="disabled")
        thread = threading.Thread(target=function)
        thread.start()


class InstallDependancy(tk.Tk, GlobalMethode):
    NAME = "Demande permissions"

    colors = Colors()
    allColors = colors.GetCurrentColor()
    BACKGROUND = 0
    FOREGROUND = 1
    GREY       = 2
    INFO       = 3
    INFO_ERROR = 4

    WINDOW_W = 470
    WINDOW_H = 160

    def __init__(self):
        tk.Tk.__init__(self)
        self.InitWindow(self.WINDOW_W, self.WINDOW_H)
        self.Widgets()

    def InitWindow(self, width, height):
        self.title(self.NAME)
        self.resizable(False, False)
        self.iconbitmap(default=os.path.join("src", "images", "icon.ico"))
        self.geometry('%dx%d+%d+%d' % (width, height, self.winfo_screenwidth() / 2 - width / 2,
                                       self.winfo_screenheight() / 2 - height / 2))
        self.configure(bg=self.allColors[self.BACKGROUND])

    def Widgets(self):
        self.indications = tk.Label(self, text="Cette application a besoin d'installer des dépendances pour fonctionner.",
                                    font=("Arial", 11), fg=self.allColors[self.FOREGROUND], bg=self.allColors[self.BACKGROUND])
        self.indications.grid(row=0, column=0, pady=(10, 20))

        installImage = tk.PhotoImage(file=os.path.join("src", "images", "installation.png"))
        self.install = tk.Button(self, image=installImage, command=lambda: self.StartThread(self.Install, self.install),
                                 bd=0, highlightthickness=0)
        self.install.image = installImage
        self.install.grid(row=1, column=0, pady=(5, 10))

        self.installProgress = tk.Label(self, text="Installation en cours...", font=("Arial", 11),
                                        fg=self.allColors[self.FOREGROUND], bg=self.allColors[self.BACKGROUND])
        self.installProgress.grid(row=2, column=0, pady=10)
        self.installProgress.grid_remove()

        self.currentModeColor = False
        self.darkMode = tk.PhotoImage(file=os.path.join("src", "images", "dark_mode.png"))
        self.lightMode = tk.PhotoImage(file=os.path.join("src", "images", "light_mode.png"))
        self.colorMode = tk.Button(self, image=self.darkMode, command=self.ColorMode, bd=0, highlightthickness=0)
        self.colorMode.grid(row=3, column=0, sticky="se")

        self.ColorMode()  # ¯\_(ツ)_/¯
        self.ColorMode()  # ¯\_(ツ)_/¯

    def Install(self):
        self.installProgress.grid()
        if LibInstall("yt-dlp"):
            self.installProgress.configure(text="Installation terminé, fermez l'application et relancer la.")
        else:
            self.installProgress.configure(text="Une erreur est surrvenu, réessayer plus tard.")


class Application(tk.Tk, GlobalMethode):
    NAME = "Youtube Downloader"

    colors = Colors()
    allColors = colors.GetCurrentColor()
    BACKGROUND = 0
    FOREGROUND = 1
    GREY       = 2
    INFO       = 3
    INFO_ERROR = 4

    WINDOW_W = 600
    WINDOW_H = 275
    folderOut = ""

    def __init__(self):
        tk.Tk.__init__(self)
        self.InitWindow(self.WINDOW_W, self.WINDOW_H)
        self.Widgets()

    def InitWindow(self, width, height):
        self.title(self.NAME)
        self.resizable(False, False)
        self.iconbitmap(default=os.path.join("src", "images", "icon.ico"))
        self.geometry('%dx%d+%d+%d' % (width, height, self.winfo_screenwidth() / 2 - width / 2,
                                       self.winfo_screenheight() / 2 - height / 2))
        self.labelTitle = tk.Label(self, text=self.NAME, font=("Arial", 40), fg=self.allColors[self.FOREGROUND],
                                   bg=self.allColors[self.BACKGROUND])
        self.labelTitle.pack(side="top")
        self.configure(bg=self.allColors[self.BACKGROUND])

    def Widgets(self):
        self.currentModeColor = False
        self.darkMode = tk.PhotoImage(file=os.path.join("src", "images", "dark_mode.png"))
        self.lightMode = tk.PhotoImage(file=os.path.join("src", "images", "light_mode.png"))
        self.colorMode = tk.Button(self, image=self.darkMode, command=self.ColorMode, bd=0, highlightthickness=0)
        self.colorMode.pack(side="bottom", anchor="se", padx=10, pady=10)

        self.urlTextBox = tk.Text(self, width=20, height=1)
        self.urlTextBox.insert("1.0", "Saisir l'url")
        self.urlTextBox.tag_configure("style", font=("Arial", 10, "italic"), foreground=self.allColors[self.GREY])
        self.urlTextBox.tag_add("style", "1.0", "end")
        self.urlTextBox.place(x=5, y=self.WINDOW_H // 2 - self.urlTextBox.winfo_reqheight() // 2)

        arrowImage = tk.PhotoImage(file=os.path.join("src", "images", "arrow.png"))
        self.arrow = tk.Label(self, image=arrowImage)
        self.arrow.image = arrowImage
        self.arrow.place(x=self.WINDOW_W // 2 - arrowImage.width() // 2, y=self.WINDOW_H // 2 - arrowImage.height() // 2)

        folderImage = tk.PhotoImage(file=os.path.join("src", "images", "file_explorer_.png"))
        self.folderPath = tk.Button(self, image=folderImage, command=self.GetFolderOut, bd=0, highlightthickness=0)
        self.folderPath.image = folderImage
        self.folderPath.place(x=(self.WINDOW_W - folderImage.width()) - 5, y=self.WINDOW_H // 2 - folderImage.height() // 2)

        self.folderTextBox = tk.Text(self, width=20, height=1)
        self.folderTextBox.insert("1.0", "Saisir un chemin d'accès")
        self.folderTextBox.tag_configure("style", font=("Arial", 10, "italic"), foreground=self.allColors[self.GREY])
        self.folderTextBox.tag_add("style", "1.0", "end")
        self.folderTextBox.place(x=((self.WINDOW_W - folderImage.width()) - 5) - self.folderTextBox.winfo_reqwidth() - 5,
                                 y=self.WINDOW_H // 2 - self.folderTextBox.winfo_reqheight()// 2)

        dlImage = tk.PhotoImage(file=os.path.join("src", "images", "download.png"))
        self.download = tk.Button(self, image=dlImage, command=lambda: self.StartThread(self.Download, self.download),
                                  bg=self.allColors[self.BACKGROUND], bd=0, highlightthickness=0)
        self.download.image = dlImage
        self.download.place(x=self.WINDOW_W // 2 - dlImage.width() // 2, y=(self.WINDOW_H // 2 - dlImage.height() // 2) + 75)

        self.info = tk.Label(self, text="Aucun dossier de sortie selectionné.", fg=self.allColors[self.INFO_ERROR],
                             bg=self.allColors[self.BACKGROUND])

        self.ColorMode() # ¯\_(ツ)_/¯
        self.ColorMode() # ¯\_(ツ)_/¯

    def GetFolderOut(self):
        self.folderOut = filedialog.askdirectory()
        self.folderTextBox.delete("1.0", "end")
        self.folderTextBox.insert("1.0", self.folderOut)

    def Download(self):
        import yt_dlp

        folder = self.folderTextBox.get("1.0", "end-1c")
        if folder == "":
            self.info.place(relx=0.5, rely=1.0, anchor="s")
            self.download.config(state="active")
        elif os.path.exists(folder):
            self.info.configure(text="Téléchargement en cours...", fg=self.allColors[self.INFO])
            self.info.place(relx=0.5, rely=1.0, anchor="s")

            url = self.urlTextBox.get("1.0", "end-1c")
            try:
                ydl_opts = {
                    'outtmpl': folder + '/%(title)s.%(ext)s'
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                self.info.configure(text="Téléchargement terminé.", fg=self.allColors[self.INFO])
                self.download.config(state="active")
            except Exception:
                self.info.configure(text="Vérifiez votre url ou votre connexion internet.", fg=self.allColors[self.INFO_ERROR])
                self.download.config(state="active")
        else:
            self.info.configure(text="Verifiez le chemin d'accès de sortie.")
            self.info.place(relx=0.5, rely=1.0, anchor="s")
            self.download.config(state="active")


if __name__ == '__main__':
    if not IsLibInstalled("yt-dlp"):
        appInstall = InstallDependancy()
        appInstall.protocol("WM_DELETE_WINDOW", lambda: exit())
        appInstall.mainloop()
    else:
        app = Application()
        app.mainloop()
