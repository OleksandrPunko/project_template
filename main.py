from app.io import input
from app.io import output

def main():
    # Example of using functions
    output_text = "This is an example of text that can be output to the console or written to a file."

    # Output to the console
    output.output_to_console(output_text)

    # Writing to a file using built-in Python capabilities
    output.output_to_file("output_builtin.txt", output_text)

    # Reading text from console
    input_text = input.input_text_from_console()

    # Output the text from console to console
    output.output_to_console(input_text)

    # Writing text from console to file using built-in Python capabilities
    output.output_to_file("output_from_console_builtin.txt", input_text)

    # Reading text from a file using built-in Python capabilities
    file_text = input.read_text_from_file("example_file.txt")

    # Output the text from the file to console
    output.output_to_console(file_text)

    # Writing text from a file to another file using built-in Python capabilities
    output.output_to_file("output_from_file_builtin.txt", file_text)


if __name__ == "__main__":
    main()
