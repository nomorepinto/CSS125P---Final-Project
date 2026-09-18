import re                                            #import the regular expressions module for pattern matching
from language_spec import RESERVED_WORDS, SYMBOLS    #import the reserved words and symbols from the language_spec module

def generate_res_sym(filename):
    # Print a message indicating that reserved words and symbols are being generated from the file.
    print("Generating reserved words and symbols from file:", filename)

    # Try to open the specified file and read its contents. If the file is not found, return False.
    try:
        with open(filename, encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        return False

    # Initialize empty lists to store found reserved words and symbols.
    found_words = []
    found_symbols = []

    # Loop through each reserved word and check if it is present in the code using regular expressions. 
    # If found, add it to the found_words list.

    for word in RESERVED_WORDS:
        pattern = r"\b" + word + r"\b"
        if re.search(pattern, code, re.IGNORECASE):
            found_words.append(word)

    # Loop through each symbol and check if it is present in the code. If found, add it to the found_symbols list.
    for symbol in SYMBOLS:
        if symbol in code:
            found_symbols.append(symbol)

    # Write the found reserved words and symbols to a file named "RES_SYM.TXT".
    with open("RES_SYM.TXT", "w", encoding="utf-8") as out_file:
        out_file.write("RESERVED WORDS:\n")
        for word in found_words:
            out_file.write(word + "\n")
            
        out_file.write("SYMBOLS:\n")
        for symbol in found_symbols:
            out_file.write(symbol + "\n")

    # Print a message indicating that the reserved words and symbols have been generated successfully.
    print("Reserved words and symbols generated successfully.\n\n")