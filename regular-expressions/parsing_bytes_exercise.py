import re

bytes_regex = re.compile(r'\b[01]{8}\b')


def parse_bytes(bytes_string):
    return bytes_regex.findall(bytes_string)
