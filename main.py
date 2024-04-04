from app.io.input import *
from app.io.output import *


def main():
    console_text = input_text()
    file_text = read_from_file("data/input.txt")
    pandas_text = read_with_pandas("data/input_pandas.txt")

    print_to_console(console_text)
    write_to_file("data/output.txt", file_text)
    write_with_pandas("data/output_pandas.txt", pandas_text)


if __name__ == "__main__":
    main()