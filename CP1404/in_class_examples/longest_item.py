def get_longest_line(filename):
    file_object = open(filename, mode='r')
    longest_line_number = 0
    max_length = 0
    for index, line in enumerate(file_object):
        if len(line) > max_length:
            max_length = len(line)
            longest_line_number = index+1
    file_object.close()
    return longest_line_number, max_length


print(get_longest_line("get_longest_item_file"))
