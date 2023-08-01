import file

import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()
root.withdraw()

# 获取文件夹路径
f_path = filedialog.askopenfilename()
file.Update.update_file(f_path)
