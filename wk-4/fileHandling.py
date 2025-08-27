# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
# Outcomes 🎉

# Write to file 
# file = open('wk-4/assignmentFile.txt', 'w')
# file.write('Hi Admin!, This na my Assignment txt file\n')
# file.close()


try:
    # Ask the user for filename
    filename = input("Enter the filename to read: ")

    # Open file for reading
    file = open(filename, 'r')
    content = file.read()  # Read the content
    print("Original Content:\n", content)
    file.close()

    # Modify the content (convert to uppercase)
    modified_content = content.upper()
    print("\nModified Content:\n", modified_content)

    # Write modified content into a new file
    new_file = open('modified_' + filename, 'w')
    new_file.write(modified_content)
    new_file.close()

    print("\nFile modified successfully and saved as: modified_" + filename)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

finally:
    try:
        file.close()
    except:
        pass

