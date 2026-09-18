import file_writer           #file_writer module for writing files without spaces
import syntax_checker        #syntax_checker module for checking syntax
import lexer                 #lexer module for generating reserved words and symbols
import sys                   #sys module for accessing command line arguments (e.g. exit 1)

def main(filename):
    # Title Block
    print("====================================")
    print("HL Interpreter")
    print("====================================")

    # Write the contents of the specified file to a new file without spaces using the file_writer module.
    file_writer.write_no_spaces(filename)

    # Generate reserved words and symbols from the specified file using the lexer module.
    lexer.generate_res_sym(filename)

    # Check the syntax of the specified file using the syntax_checker module.
    syntax_checker.check(filename)

# Check if the script is being run as the main program. If so, retrieve the filename argument from the command line.
if __name__ == "__main__":
    arg = sys.argv[1]
    if not arg.endswith(".HL"):
        print("ERROR: filename must end with .HL")
        sys.exit(1)
    main(arg)