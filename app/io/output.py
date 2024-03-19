def output_to_console(text):
    """
    A function for outputting text to the console.
    """
    print(text)


def output_to_file(filename, text):
    """
    Function for writing text to a file.

     Parameters:
         filename (str): The name of the file to write the text to.
         text (str): The text to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(text)


def main():
    # Example of using functions
    output_text = "This is an example of text that can be output to the console or written to a file."

    # Output to the console
    output_to_console(output_text)

    # Writing to a file
    output_to_file("output.txt", output_text)


if __name__ == "__main__":
    main()
