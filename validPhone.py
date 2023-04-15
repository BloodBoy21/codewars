import re
def valid_phone(phone):
    regex = r"^\(\d{3}\)\s\d{3}-\d{4}$"
    pattern = re.compile(regex)
    return bool(pattern.search(phone))
