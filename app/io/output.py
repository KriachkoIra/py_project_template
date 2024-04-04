def print_to_console(text):
    """
    Function to print text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)

def write_to_file(file_path, data):
    """
    Function to write data to a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file to be written.
        data (str): The data to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"Error writing to file: {e}")

def write_with_pandas(file_path, data):
    """
    Function to write data to a file using the pandas library.

    Args:
        file_path (str): The path to the file to be written.
        data (pandas.DataFrame): The DataFrame to be written to the file.
    """
    try:
        data.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error writing to file with pandas: {e}")
