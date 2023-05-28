import tkinter as tk
import winreg

class ApplicationLister:
    def __init__(self, master):
        self.master = master
        master.title("Lista de aplicaciones instaladas")

        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(master, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.listbox.yview)

        self.get_installed_apps()

    def get_installed_apps(self):
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall") as key:
            for i in range(winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                with winreg.OpenKey(key, subkey_name) as subkey:
                    try:
                        display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        self.listbox.insert(tk.END, display_name)
                    except OSError:
                        pass

root = tk.Tk()
app = ApplicationLister(root)
root.mainloop()