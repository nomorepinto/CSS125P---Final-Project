def write_no_spaces(filename):
    """Read the file named by filename and write NO_SPACES.txt as one line with spaces removed.

    Returns True on success, False if the file cannot be read or written.
    """
    if not filename or not isinstance(filename, str):
        print("ERROR: filename must be a non-empty string.")
        return False

    try:
        with open(filename, "r", encoding="utf-8") as source:
            contents = source.read()
    except FileNotFoundError:
        print(f"ERROR: file not found: {filename}")
        return False

    no_spaces = "".join(contents.split())

    with open("NO_SPACES.txt", "w", encoding="utf-8") as output:
        output.write(no_spaces)

    return True
