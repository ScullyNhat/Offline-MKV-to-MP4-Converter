#pip install tk ffmpeg-python
#Khai bao thu vien can thiet
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg

#Khai bao bien
input_folder = "films"
output_folder = "converted_films"

#Ham can hien thuc
def convert_to_mp4(mkv_file, output_folder):
    name, ext = os.path.splitext(os.path.basename(mkv_file))
    out_name = os.path.join(output_folder, name + ".mp4")
    ffmpeg.input(mkv_file).output(out_name, codec='copy').run(overwrite_output=True)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def convert_selected_file():
    mkv_file = entry_file_path.get()
    if not mkv_file:
        messagebox.showerror("Error", "Please select a MKV file!")
        return
    convert_to_mp4(mkv_file, output_folder)
    messagebox.showinfo("Success", "Selected file conversion completed!")

def convert_all_files():
    count = 0
    for path, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.mkv'):
                input_path = os.path.join(path, file)
                convert_to_mp4(input_path, output_folder)
                count += 1
    if count > 0:
        messagebox.showinfo("Success", f"Files converted successfully! Total: {count}")
    else:
        messagebox.showerror("Error", "No MKV file found in the folder")

# Setup GUI
def center_window(window):
    window_width = 500
    window_height = 100
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

root = tk.Tk()
root.title("MKV to MP4 Converter")
center_window(root)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Select MKV file:").grid(row=0, column=0, padx=5, pady=5)
entry_file_path = tk.Entry(frame, width=40)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)
btn_select = tk.Button(frame, text="Browse", command=select_file)
btn_select.grid(row=0, column=2, padx=5, pady=10)

btn_convert_all = tk.Button(frame, text="Convert Files in Films", command=convert_all_files)
btn_convert_all.grid(row=1, column=1, pady=5)
btn_convert_selected = tk.Button(frame, text="Convert Selected File", command=convert_selected_file)
btn_convert_selected.grid(row=1, column=2, pady=5)

root.mainloop()
