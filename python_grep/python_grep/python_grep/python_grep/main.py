import sys, os, re


def grep_file(regular_expression, file, count, not_option, ignore_case):
    print("FILE : ",file)
    if os.path.exists(file):
        file_descriptor = open(file, 'r')
        lines = file_descriptor.readlines()
        count_number_appearances = 0
        is_match_in_a_file = False
        for line in lines:
            if ignore_case:
                if regular_expression.lower() in line.lower():
                    print(line)
            if bool(re.match(regular_expression, line)) and not ignore_case:
                print(line)
                is_match_in_a_file = True
            if count and bool(re.match(regular_expression, line)) or regular_expression.lower() in line.lower() and ignore_case:
                count_number_appearances = count_number_appearances + 1
        file_descriptor.close()
        if not_option:
            if is_match_in_a_file:
                print("There is a match in this file for the this regular expression ")
            else:
                print("There is no match in this file for the this regular expression")
        if count:
            print("Number of appearances: ", count_number_appearances)
    else:
        print("File ", file, " doesn't exist ! ")


def grep_for_dir(regular_expression, director, count, not_option, ignore_case):
    if os.path.exists(director):
        content_dir = os.listdir(director)
        for component in content_dir:
            path_component = os.path.join(director, component)
            if os.path.isfile(path_component):
                grep_file(regular_expression, path_component, count, not_option, ignore_case)
            else:
                if os.path.isdir(path_component):
                    grep_for_dir(regular_expression, path_component, count, not_option, ignore_case)
    else:
        print("Directory ", director, " doesn't exist ! ")


def print_help_function():
    print("USAGE : python grep.py [REGULAR_EXPRESSION] [FILE|DIRECTOR] .. [OPTIONS]")


def main_function():
    if len(sys.argv) < 3:
        print_help_function()
        exit(0)
    else:
        isNotOption = False
        isIgnoreCase = False
        isCountOption = False
        if "-NOT" in sys.argv:
            isNotOption = True
        if "-ignoreCase" in sys.argv:
            isIgnoreCase = True
        if "-count" in sys.argv:
            isCountOption = True
        if os.path.isfile(sys.argv[2]):
            grep_file(sys.argv[1], sys.argv[2], isCountOption, isNotOption, isIgnoreCase)
        else:
            grep_for_dir(sys.argv[1], sys.argv[2], isCountOption, isNotOption, isIgnoreCase)


main_function()
