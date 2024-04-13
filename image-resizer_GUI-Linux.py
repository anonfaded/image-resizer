import os
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

class ImageResizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        # Set dark mode theme
        master.configure(bg="#1E1E1E")
        self.label_color = "#FFFFFF"
        self.entry_bg = "#333333"
        self.button_bg = "#555555"
        self.button_fg = "#FFFFFF"
        self.github = "green"

        # Labels
        self.source_label = tk.Label(master, text="Source Image:", bg="#1E1E1E", fg=self.label_color)
        self.source_label.grid(row=0, column=0)

        self.destination_label = tk.Label(master, text="Output Image Name:", bg="#1E1E1E", fg=self.label_color)
        self.destination_label.grid(row=1, column=0)

        self.scale_label = tk.Label(master, text="Scale Percentage:", bg="#1E1E1E", fg=self.label_color)
        self.scale_label.grid(row=2, column=0)

        # Entries
        self.source_entry = tk.Entry(master, width=50, bg=self.entry_bg, fg=self.label_color)
        self.source_entry.grid(row=0, column=1)

        self.destination_entry = tk.Entry(master, width=50, bg=self.entry_bg, fg=self.label_color)
        self.destination_entry.grid(row=1, column=1)

        self.scale_entry = tk.Entry(master, bg=self.entry_bg, fg=self.label_color)
        self.scale_entry.grid(row=2, column=1)

        # Buttons
        self.source_button = tk.Button(master, text="Browse", command=self.browse_source, bg=self.button_bg, fg=self.button_fg)
        self.source_button.grid(row=0, column=2, pady=(5, 10), padx=(20, 10))

        self.destination_button = tk.Button(master, text="...", command=self.browse_destination, bg=self.button_bg, fg=self.button_fg)
        self.destination_button.grid(row=1, column=2, pady=(5, 10))

        self.resize_button = tk.Button(master, text="Resize Image", command=self.resize_image, bg=self.button_bg, fg=self.button_fg)
        self.resize_button.grid(row=3, column=1, pady=(30, 0))

        # Information Text
        self.info_text = tk.Label(master, text=f"Please select the source image that you want to resize and type the name of output image,\n specify the scale percentage, and click 'Resize Image' to proceed.\n", bg="#1E1E1E", fg=self.label_color, padx=10, pady=10)
        # github bottom
        self.info_text.grid(row=4, column=0, columnspan=3, pady=(0, 55))
        self.info_text = tk.Label(master, text="https://github.com/anonfaded/image-resizer", bg="#1E1E1E", fg=self.github, padx=10, pady=10)
        self.info_text.grid(row=4, column=0, columnspan=3, padx=(5, 5))

    def browse_source(self):
        filename = filedialog.askopenfilename()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, filename)

    def browse_destination(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png")
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, filename)

    def resize_image(self):
        # Get source, destination, and scale percentage
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        scale_percent_str = self.scale_entry.get()

        errors = []

        # Check if scale percentage is a valid integer
        if not scale_percent_str.isdigit():
            errors.append("Scale Percentage must be a valid integer.")

        # Check if destination is empty
        if not destination:
            errors.append("Output Image Name cannot be empty.")

        # Check if source file exists
        if not os.path.isfile(source):
            errors.append("Source file does not exist.")

        if errors:
            messagebox.showerror("Error", "\n".join(errors))
            return

        # Load the source image
        src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
        if src is None:
            messagebox.showerror("Error", "Failed to load source image.")
            return

        # Calculate new dimensions
        new_width = int(src.shape[1] * int(scale_percent_str) / 100)
        new_height = int(src.shape[0] * int(scale_percent_str) / 100)

        # Resize the image
        output = cv2.resize(src, (new_width, new_height))

        # Get the extension of the source image
        _, extension = os.path.splitext(source)

        # Save the resized image with the same extension as the source image
        cv2.imwrite(destination + extension, output)

        messagebox.showinfo("Image Resizer", "Image resized successfully!")

def main():
    root = tk.Tk()
    app = ImageResizerApp(root)

    # Fix the window size
    root.resizable(False, False)


    root.mainloop()

if __name__ == "__main__":
    main()
