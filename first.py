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
    for i in range(len(sorted_lines_with_lens)):
        no_lengths.append(sorted_lines_with_lens[i][0])
    return no_lengths


if __name__ == "__main__":
    # verifications: skip if no file, if no arguments
    # take as arguments
    filename = "C:\\testing_ass\\input.txt"
    multiplied_lines = {}
    with open(filename, "r") as f:
        input_file_content = (f.readlines())
    for i in input_file_content:
        digits_from_line = i.split(" ")
        valid_line = (len(digits_from_line) == 3)  # skip the line if it is not "5 8 31"
        if valid_line:
            multiplied_lines.update(count_multiplies(digits_from_line))
    sorted_lines_with_lens = sorted(multiplied_lines.items(), key=lambda x: x[1])
    sorted_lines_only_values = remove_lens(sorted_lines_with_lens)
    print(sorted_lines_only_values)
