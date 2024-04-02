# Open a file named "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as file:
    # Write three lines of text to the file
    file.write("Hello, this is line 1.\n")
    file.write("12345\n")
    file.write("Python File Handling Assignment\n")

# Open the file in read mode ('r')
with open("my_file.txt", "r") as file:
    # Read and display the contents of the file
    for line in file:
        print(line.strip())

# Open the file in append mode ('a')
with open("my_file.txt", "a") as file:
    # Append three additional lines of text to the existing content
    file.write("Appending line 1.\n")
    file.write("67890\n")
    file.write("Additional content for file.\n")

try:
    # Perform file operations that may raise exceptions
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
finally:
    print("File handling operation completed.")

