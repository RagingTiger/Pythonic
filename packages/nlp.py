# standard modules
import re
from typing import Iterator


# globals
WSP_REGEX = re.compile('[^A-Za-z]+')


# functions
def tokenize(text: str, regex: re.Pattern = WSP_REGEX) -> Iterator:
    """Takes a large body of text and returns a clean list of words."""
    # get words
    raw_words = text.split()

    # now clean words
    for word in raw_words:
        # strip unwanted chars
        clean = regex.sub('', word).lower()

        # check if it is alphabetical
        if clean.isalpha():
            # now yield
            yield clean
