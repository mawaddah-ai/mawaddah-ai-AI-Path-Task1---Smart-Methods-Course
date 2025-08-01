import os

print("Current working directory:", os.getcwd())

file_path = "C:\\Users\\mawad\\PycharmProjects\\Linux_Task\\pythonProject\\test_file.txt"


if not os.path.exists(file_path):
    print("The file does not exist.")
else:
    try:
        os.chmod(file_path, 0o775)
        print(f"Permissions of {os.path.abspath(file_path)} have been changed to rwxrwxr-x (775)")
    except Exception as e:
        print(f"chmod failed on Windows: {e}")

    os.system(f"icacls \"{file_path}\"")
