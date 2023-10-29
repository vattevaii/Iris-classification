import sys


def read_language_info(file_path):
    language_info = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) == 3:
                        language_name, iso_code, char_set = parts
                        language_info.append((language_name, iso_code, char_set))
                    else:
                        print(f"Invalid line in the file: {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return language_info


def print_languages_in_alphabetic_order(language_info):
    sorted_info = sorted(language_info, key=lambda x: x[0])
    if len(sorted_info) == 0:
        print("No languages in this file")
    else:
        print("Languages in this file:")
    for language_name, iso_code, char_set in sorted_info:
        print(f"{language_name}")


def print_languages_with_code(language_info, code):
    matching_languages = [language for language in language_info if code == language[1]]
    for language_name, iso_code, char_set in matching_languages:
        print(f"{language_name}")
    if len(matching_languages) == 0:
        print(f"Code {code} not present in this file")


def print_languages_with_set(language_info, char_set):
    matching_languages = [language for language in language_info if char_set == language[2]]
    for language_name, iso_code, char_set in matching_languages:
        print(f"{language_name}")
    if len(matching_languages) == 0:
        print(f"Character set {char_set} not present in this file")


def main():
    if len(sys.argv) < 3:
        print("Usage: python filename.py option argument_file")
        return


    option = sys.argv[1]
    argument_file = sys.argv[2]
    if len(sys.argv) == 4:
        argument_file = sys.argv[3]
    language_info = read_language_info(argument_file)


    if option == "-a":
        print_languages_in_alphabetic_order(language_info)
    elif option == "-c":
        code = sys.argv[2]
        print_languages_with_code(language_info, code)
    elif option == "-s":
        char_set = sys.argv[2]
        print_languages_with_set(language_info, char_set)
    elif option == "-v":
        print("NAME SURNAME / STUDENT_ID / DATA_OF_COMPLETITION")
    else:
        print("Invalid option. Use -a, -c, -v or -s.")


if __name__ == "__main__":
    main()
