def input_text():
    """
    Function to input text from the console.

    Returns:
        str: The text entered by the user.
    """
    text = input("Enter text: ")
    return text

def read_from_file(file_path):
    """
    Function to read data from a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
        None: If the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

def read_with_pandas(file_path):
    """
    Function to read data from a file using the pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the file.
        None: If the file is not found.
    """
    try:
        import pandas as pd
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
