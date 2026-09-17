import re
from language_spec import RESERVED_WORDS, SYMBOLS

def generate_res_sym(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        return False

    found_words = []
    found_symbols = []

    for word in RESERVED_WORDS:
        pattern = r"\b" + word + r"\b"
        if re.search(pattern, code, re.IGNORECASE):
            found_words.append(word)

    for symbol in SYMBOLS:
        if symbol in code:
            found_symbols.append(symbol)

    with open("RES_SYM.TXT", "w", encoding="utf-8") as out_file:
        out_file.write("RESERVED WORDS:\n")
        for word in found_words:
            out_file.write(word + "\n")
            
        out_file.write("SYMBOLS:\n")
        for symbol in found_symbols:
            out_file.write(symbol + "\n")