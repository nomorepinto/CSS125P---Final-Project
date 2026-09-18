def write_no_spaces(filename):
    #Inform user that spaces are being removed from the file.
    print("Removing Spaces from file:", filename)

    """Read the file named by filename and write NO_SPACES.txt as one line with spaces removed.

    Returns True on success, False if the file cannot be read or written.
    """
    if not filename or not isinstance(filename, str):
        print("ERROR: filename must be a non-empty string.")
        return False

    # Check if the file exists and can be read
    try:
        with open(filename, "r", encoding="utf-8") as source:
            contents = source.read()
    # Throw error message if file not found.
    except FileNotFoundError:
        print(f"ERROR: file not found: {filename}")
        return False

    # Remove spaces from the contents of the file.
    no_spaces = "".join(contents.split())

    # Write the contents without spaces to a new file named NO_SPACES.txt
    with open("NO_SPACES.txt", "w", encoding="utf-8") as output:
        output.write(no_spaces)

    # Success message to inform user that spaces have been removed successfully.
    print("Spaces removed successfully.\n\n")
    return True
