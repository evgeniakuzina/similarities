from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    lines1 = a.splitlines()
    lines2 = b.splitlines()

    str_common = []

    for line in lines1:
        if line in str_common:
            continue
        if line in lines2:
            str_common.append(line)

    print("This is str_common now:{}".format(str_common))

    return str_common


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    sent1 = sent_tokenize(a)
    sent2 = sent_tokenize(b)

    sent_common = []

    for sentence in sent1:
        if sentence in sent_common:
            continue
        if sentence in sent2:
            sent_common.append(sentence)

    return sent_common


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    def extract_substrings(string, x):
        substring = []
        y = 0

        for i in string:
            if len(string[y:y + int(x)]) < x:
                break
            if string[y:y + int(x)] in substring:
                y += 1
                continue
            else:
                substring.append(string[y:y + int(x)])
                y += 1

        return substring

    substr1 = extract_substrings(a, n)
    substr2 = extract_substrings(b, n)
    substr_common = []

    for substring in substr1:
        if substring in substr_common:
            continue
        if substring in substr2:
            substr_common.append(substring)

    return substr_common
