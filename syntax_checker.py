import re        #import the regular expressions module for pattern matching

def check(filename):
    # Print a message indicating that the syntax check is being performed on the file.
    print("Checking syntax for file:", filename)

    # Try to open the specified file and read its contents. 
    try:
        with open("NO_SPACES.txt", "r", encoding="utf-8") as file:
            code = file.read()
            
    # If the file is not found, print an error message and return.
    except FileNotFoundError:
        print("ERROR")
        return

    # 1. Define the regular expression patterns for variables, numbers, and strings.
    var = r'[a-zA-Z_]+'
    num = r'\d+(?:\.\d+)?'
    string = r'["“”].*?["“”]'
    
    # 2. Values and Expressions: Combination of strings, numbers, variables with arithmetic operators.
    expr = rf'(?:{string}|{num}|{var})(?:[+-](?:{num}|{var}))*'
    
    # 3. Statement Rules (Removed the inline (?i) flags): for declaration, assignment, and output statements.
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
    # Syntax check: Use re.fullmatch to check if the entire code matches the program pattern.
    if re.fullmatch(program_pattern, code, re.IGNORECASE):
        print("NO ERROR(S) FOUND")
        
    # Displays error message if not matching.
    else:
        print("ERROR")