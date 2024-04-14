import os
import subprocess
from colorama import init, Fore
from tkinter import Tk, filedialog
import cv2

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



def select_image():
    root = Tk()
    root.withdraw()  # Hide the main window

    print("Select an image file...")
    filename = filedialog.askopenfilename()
    if not filename:
        print(Fore.RED + "Error: No image selected.")
        return None

    return filename

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

def main():
    init()  # Initialize colorama

    # Clear the terminal
    clear_terminal()



    while True:
        # Get source image path
        source = select_image()
        if not source:
            break

        # Get output image name
        destination = ""
        destination = input(Fore.GREEN + "Enter the output image name: ").strip()
        while not destination:
            
            if not destination:
                clear_terminal()
                print(Fore.RED + "Error: Output image name cannot be empty.")
                destination = input(Fore.GREEN + "Enter the output image name: ").strip()
            
                
                
        
        # Get scale percentage
        while True:
            clear_terminal()
            scale_percent_str = input(Fore.GREEN + "Enter the scale percentage: ").strip()
            if not scale_percent_str.isdigit():
                clear_terminal()
                print(Fore.RED + "Error: Scale Percentage must be a valid integer.")
                scale_percent_str = input(Fore.GREEN + "Enter the scale percentage: ").strip()
                continue
            else:
                scale_percent = int(scale_percent_str)
                break

        # Resize the image
        success = resize_image(source, destination, scale_percent)
        if not success:
            continue

        break  # Exit the loop if successful

if __name__ == "__main__":
    main()
