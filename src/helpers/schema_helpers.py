"""Module that defines schema helpers"""


def remove_whitespace_make_lowercase(data, exclude):
    """Removes whitespaces from input data and
    change input data to lowercase
    """
    for field in data.keys():
        if isinstance(data.get(field), str) and field != exclude:
            data[field] = data.get(field).strip().lower()
    return data
