import tkinter as tk
from tkinter import filedialog
import cv2

class ImageResizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        self.source_label = tk.Label(master, text="Source Image:")
        self.source_label.grid(row=0, column=0)

        self.source_entry = tk.Entry(master, width=50)
        self.source_entry.grid(row=0, column=1)

        self.source_button = tk.Button(master, text="Browse", command=self.browse_source)
        self.source_button.grid(row=0, column=2)

        self.destination_label = tk.Label(master, text="Destination Image:")
        self.destination_label.grid(row=1, column=0)

        self.destination_entry = tk.Entry(master, width=50)
        self.destination_entry.grid(row=1, column=1)

        self.destination_button = tk.Button(master, text="Browse", command=self.browse_destination)
        self.destination_button.grid(row=1, column=2)

        self.scale_label = tk.Label(master, text="Scale Percentage:")
        self.scale_label.grid(row=2, column=0)

        self.scale_entry = tk.Entry(master)
        self.scale_entry.grid(row=2, column=1)

        self.resize_button = tk.Button(master, text="Resize Image", command=self.resize_image)
        self.resize_button.grid(row=3, column=1)

    def browse_source(self):
        filename = filedialog.askopenfilename()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, filename)

    def browse_destination(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png")
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, filename)

    def resize_image(self):
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        scale_percent = int(self.scale_entry.get())

        src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
        new_width = int(src.shape[1] * scale_percent / 100)
        new_height = int(src.shape[0] * scale_percent / 100)
        output = cv2.resize(src, (new_width, new_height))
        cv2.imwrite(destination, output)
        tk.messagebox.showinfo("Image Resizer", "Image resized successfully!")

def main():
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
