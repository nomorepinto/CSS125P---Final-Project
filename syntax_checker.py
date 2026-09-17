import re

def check(filename):
    try:
        with open("NO_SPACES.txt", "r", encoding="utf-8") as file:
            code = file.read()
    except FileNotFoundError:
        print("ERROR")
        return

    # 1. Basic Building Blocks
    var = r'[a-zA-Z_]+'
    num = r'\d+(?:\.\d+)?'
    string = r'["“”].*?["“”]'
    
    # 2. Values and Expressions
    expr = rf'(?:{string}|{num}|{var})(?:[+-](?:{num}|{var}))*'
    
    # 3. Statement Rules (Removed the inline (?i) flags)
    decl_stmt = rf'{var}:(?:integer|double);'
    assign_stmt = rf'{var}(?::=|=){expr};'
    output_stmt = rf'output<<{expr};'
    
    base_stmt = rf'(?:{decl_stmt}|{assign_stmt}|{output_stmt})'
    
    # 4. If Statements (Removed the inline (?i) flag)
    condition = rf'{var}(?:<|>|==|!=)(?:{num}|{var})'
    if_stmt = rf'if\({condition}\){base_stmt}'
    
    # 5. Master Validation
    valid_stmt = rf'(?:{base_stmt}|{if_stmt})'
    program_pattern = rf'^({valid_stmt})+$'

    # Added re.IGNORECASE as a parameter here instead
    if re.fullmatch(program_pattern, code, re.IGNORECASE):
        print("NO ERROR(S) FOUND")
    else:
        print("ERROR")