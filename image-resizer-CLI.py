import cv2
import os
from tkinter import Tk, filedialog
from colorama import init, Fore

def resize_image(source, destination, scale_percent):
    # Load the source image
    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
    if src is None:
        print(Fore.RED + "Error: Failed to load source image.")
        return False

    # Calculate new dimensions
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Resize the image
    output = cv2.resize(src, (new_width, new_height))

    # Get the extension of the source image
    _, extension = os.path.splitext(source)

    # Save the resized image with the same extension as the source image
    cv2.imwrite(destination + extension, output)

    print(Fore.GREEN + "Image resized successfully!")
    return True

def select_image():
    print(Fore.GREEN + "Please select the source image.")
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Open file dialog
    return file_path

def main():
    init()  # Initialize colorama

    # Prompt the user if they want to open the file opener
    open_file_opener = input(Fore.GREEN + "Do you want to open the file opener to select an image? (y/n): ")

    # If the user confirms, select source image using file dialog
    if open_file_opener.lower() == 'y':
        source = select_image()
    else:
        # If the user doesn't want to open the file opener, ask for the source image path directly
        print(Fore.GREEN + "Enter the path of the source image: ", end="")
        source = input().strip()

    # Check if source image was provided
    if not source:
        print(Fore.RED + "Error: No source image provided. Please provide a valid path.")
        return

    # Check if the source file exists
    if not os.path.isfile(source):
        print(Fore.RED + "Error: Source file does not exist.")
        return

    # Ask for destination filename (without extension)
    print(Fore.GREEN + "Enter the name of the output image (without extension): ", end="")
    destination = input().strip()

    # Append source file's extension to the destination filename
    _, source_filename = os.path.split(source)
    destination += os.path.splitext(source_filename)[1]

    # Ask for scale percentage
    print(Fore.GREEN + "Enter the scale percentage (e.g., 50 for 50%): ", end="")
    scale_percent_str = input().strip()

    # Check if scale percentage is a valid integer
    while not scale_percent_str.isdigit():
        print(Fore.RED + "Error: Scale percentage must be a valid integer.")
        print(Fore.GREEN + "Enter the scale percentage (e.g., 50 for 50%): ", end="")
        scale_percent_str = input().strip()

    # Convert scale percentage to integer
    scale_percent = int(scale_percent_str)

    # Resize the image
    resize_image(source, destination, scale_percent)

if __name__ == "__main__":
    main()
