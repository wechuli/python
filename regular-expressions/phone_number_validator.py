import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


def extract_all_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    if match:
        return match
    return None


def is_valid_phone(input):
    phone_regex = re.compile(r'^\b\d{3} \d{3}-\d{4}\b$')
    # match = phone_regex.search(input)
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-8976534"))
print(extract_all_phone("my number is 432 567-8976"))
print(extract_all_phone("my number is 432 567-89736"))
print(is_valid_phone("my number is 432 567-8976"))
print(is_valid_phone("432 567-8976"))
