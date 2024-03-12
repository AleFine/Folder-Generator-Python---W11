import os
from tkinter import Tk, filedialog
def select_path():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory(initialdir="C:/", title="Select destination folder")
    return path

def create_folders(path, num_folders):
    try:
        if not path:
            print("No path selected. Exiting program.")
            return
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(num_folders):
            folder_name = f"WEEK {i + 1}"
            #folder_name = input(f"Enter name for folder {i + 1}: ")
            new_path = os.path.join(path, folder_name)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                print(f"Folder '{folder_name}' created successfully in {path}")
            else:
                print(f"Folder '{folder_name}' already exists in {path}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    path = select_path()
    if not path:
        exit()
    #num_folders = 15
    num_folders = int(input("Enter the number of folders you want to create: "))
    create_folders(path, num_folders)

