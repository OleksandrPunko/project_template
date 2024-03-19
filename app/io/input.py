def input_text_from_console():
    """
    A function for entering text from the console.
    """
    text = input("Enter text: ")
    return text

def read_text_from_file(filename):
    """
    A function to read text from a file using Python's built-in capabilities.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found")
        return None

def read_text_from_file_with_pandas(filename):
    """
    A function for reading text from a file using the pandas library.
    """
    import pandas as pd
    try:
        data = pd.read_csv(filename, header=None)
        text = ' '.join(data.iloc[:, 0].astype(str))
        return text
    except FileNotFoundError:
        print("File not found")
        return None
