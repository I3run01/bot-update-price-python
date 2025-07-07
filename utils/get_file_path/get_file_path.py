from tkinter import filedialog
import tkinter as tk

def get_file_path():

    root = tk.Tk()
    print('file path')
    root.withdraw()
    root.attributes('-topmost', True)
    return filedialog.askopenfilename(
        filetypes=[("All Files", "*.*")]
    )   


        