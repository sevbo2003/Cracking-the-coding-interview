import subprocess

PREFIX = 'lc_'


def process_string(input_file_name: str, difficulty_level: str) -> str:
    """
    Generates the proper naming for files.

    Example usage:
    :param input_file_name: 1480. Running Sum of 1d Array
    :param difficulty_level: e
    :return: lc_e_running_sum_of_1d_array.py
    """

    file_name_lower_letters = input_file_name.lower()
    split_on_point = file_name_lower_letters.rsplit(". ")
    only_letters = split_on_point[1].split()
    underscored_file_name = "_".join(only_letters)
    joined_file_name = PREFIX + difficulty_level.lower() + '_' + underscored_file_name + ".py"
    return joined_file_name


def main():
    file_name_input = input("Your file name: ")
    difficulty_level = input("Difficulty leve (E, M, H): ")
    joined_file_name = process_string(file_name_input, difficulty_level)
    print(joined_file_name)
    subprocess.run("pbcopy", universal_newlines=True, input=joined_file_name)  # Copy to clipboard.


if __name__ == "__main__":
    main()
