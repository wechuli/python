import re


phone_regex = re.compile(r"^\d{1,2}:\d{2}$")
def is_valid_time(input):
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False
