import sys

def open_file(location):
    with open(location, "r") as f:
        input_file_content = (f.readlines())
    return input_file_content


def get_multiplied_lines(input_file_content):
    multiplied_lines = {}
    for i in input_file_content:
        digits_from_line = i.split(" ")
        valid_line = (len(digits_from_line) == 3)  # skip the line if it is not like "5 8 31"
        if valid_line:
            multiplied_lines.update(count_multiplies(digits_from_line))
    return multiplied_lines


def count_multiplies(line_digits):
    digit_one = int(line_digits[0])
    digit_two = int(line_digits[1])
    upper = int(line_digits[2])
    result = []
    for i in range (1, upper):
        if i % digit_one == 0 or i % digit_two == 0:
            result.append(i)
    result_str = ' '.join([str(i) for i in result])
    return {f"{upper}:{result_str}": len(result)}  # length will be used for sorting


def remove_lens(sorted_lines_with_lens):
    no_lengths = []
    for i in range(len(sorted_lines_with_lens)):  # tuples are immutable, have to create a separate list
        no_lengths.append(sorted_lines_with_lens[i][0])
    return no_lengths


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("2 arguments for input and should be there, try again")
        exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_file_content = open_file(input_file)
    multiplied_lines = get_multiplied_lines(input_file_content)
    sorted_lines_with_lens = sorted(multiplied_lines.items(), key=lambda x: x[1])
    sorted_lines_only_values = remove_lens(sorted_lines_with_lens)

    with open(output_file, "w") as f:
        f.write(("\n".join(sorted_lines_only_values)))  # another option is to write in a "for i in sorted_lines_only_values" loop
