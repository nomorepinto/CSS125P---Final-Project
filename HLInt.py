import file_writer
import sys

def main(filename):
    file_writer.write_no_spaces(filename)

if __name__ == "__main__":
    arg = sys.argv[1]
    if not arg.endswith(".HL"):
        print("ERROR: filename must end with .HL")
        sys.exit(1)
    main(arg)