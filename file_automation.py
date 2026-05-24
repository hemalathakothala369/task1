# Python File Handling & Automation Project

# Import required modules
import os
import shutil

try:
    # -------------------------------
    # CREATE AND WRITE TO A FILE
    # -------------------------------

    # Open a text file in write mode
    file = open("sample.txt", "w")

    # Write data into file
    file.write("Hello, this is Alfido Tech Internship Task.\n")
    file.write("Learning Python File Handling.")

    # Close the file
    file.close()

    print("File created and data written successfully.")

    # -------------------------------
    # READ FILE CONTENT
    # -------------------------------

    file = open("sample.txt", "r")

    # Read file content
    content = file.read()

    print("\nFile Content:")
    print(content)

    file.close()

    # -------------------------------
    # RENAME FILE
    # -------------------------------

    os.rename("sample.txt", "renamed_sample.txt")

    print("\nFile renamed successfully.")

    # -------------------------------
    # CREATE NEW FOLDER
    # -------------------------------

    folder_name = "BackupFolder"

    # Create folder if not exists
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # -------------------------------
    # MOVE FILE TO FOLDER
    # -------------------------------

    shutil.move("renamed_sample.txt", folder_name)

    print("File moved successfully.")

    # -------------------------------
    # DELETE FILE
    # -------------------------------

    file_path = folder_name + "/renamed_sample.txt"

    os.remove(file_path)

    print("File deleted successfully.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Some error occurred:", e)