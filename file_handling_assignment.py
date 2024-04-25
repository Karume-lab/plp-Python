try:
    with open("my_file.txt", "r+") as file:
        file.write("1 My name is - what \n")
        file.write("2 My name is - who \n")
        file.write("3 Chiki chiki, Slim Shady \n")
        file.seek(0)
        text = file.read()
        print(text)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
finally:
    print("Execution completed.")
