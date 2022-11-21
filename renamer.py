import subprocess

PREFIX = 'lc_'


def process_string(input_file_name):
    """
    Function to take the string and return the processed string, to use in file names.

    :param input_file_name: 1480. Running Sum of 1d Array
    :return: slc_1480_running_sum_of_1d_array.py
    """
    file_name_lower_letters = input_file_name.lower()
    split_on_point = file_name_lower_letters.rsplit(". ")
    number = split_on_point[0]
    only_letters = split_on_point[1].split()
    underscored_file_name = "_".join(only_letters)
    joined_file_name = PREFIX + number + "_" + underscored_file_name + ".py"
    return joined_file_name


def main():
    file_name_input = input("Your file name: ")
    joined_file_name = process_string(file_name_input)
    print(joined_file_name)
    subprocess.run("pbcopy", universal_newlines=True, input=joined_file_name)  # Copy to clipboard.


if __name__ == "__main__":
    main()
