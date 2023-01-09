def drop_regex_patterns(texts, regex):
    """ Drop patterns based on regex

    Args:
        texts (str, Series): corpus to be cleaned
        regex (re.Pattern): regex pattern

    Returns:
        list: words without the regex pattern
    """
    if type(texts) == str:
        return regex.sub("", texts).lower()
    else:
        return [regex.sub("", text).lower() for text in texts]


def replace_new_line(texts, regex):
    """Replaces new line character

    Args:
        texts (str, Series): corpus to be cleaned
        regex (re.Pattern): regex pattern

    Returns:
        list: words without the new line character
    """
    if type(texts) == str:
        return regex.sub(" ", texts).lower()
    else:
        return [regex.sub(" ", text).lower() for text in texts]
    