import tkinter as tk
import sys
from tkinter import filedialog, messagebox

def get_file_path():
    """ Function will return selected file path.
        If no file selected warning message will pop up and program execution will be terminated
    """
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    if file_path == '':
        messagebox.showwarning( title="Warning",
                                message="No file was selected")

        sys.exit(0)

    return file_path