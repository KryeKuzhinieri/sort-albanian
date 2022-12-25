import re

COMPOUND_LETTERS = {
    "dh": "ð",
    "gj": "ɟ",
    "ll": "ɫ",
    "nj": "ɲ",
    "rr": "r̪",
    "sh": "ʃ",
    "th": "θ",
    "xh": "d͡ʒ",
    "zh": "ʒ",
}

ALPHABET = [
    "a", "b", "c", "ç", "d", "ð", "e",
    "ë", "f", "g", "ɟ", "h", "i", "j",
    "k", "l", "ɫ", "m", "n", "ɲ", "o",
    "p", "q", "r", "r̪", "s", "ʃ", "t",
    "θ", "u", "v", "x", "d͡ʒ", "y", "z",
    "ʒ"
]

string_alphabet = "".join(ALPHABET)


def replace_compound_characters(words, to_ipa=True, capitalize=False):
    formated_words = []
    for w in words:
        formated_w = w.lower()
        for k, v in COMPOUND_LETTERS.items():
            formated_w = re.sub(k, v, formated_w) if to_ipa else re.sub(v, k, formated_w)
        formated_w = formated_w.capitalize() if capitalize else formated_w
        formated_words.append(formated_w)
    return formated_words


def sort_albanian(words):
    formated_words = replace_compound_characters(words)
    sorted_words = sorted(
        formated_words,
        key=lambda word: [string_alphabet.index(c) for c in word]
    )
    formated_words = replace_compound_characters(
        words=sorted_words,
        to_ipa=False,
        capitalize=True,
    )
    return formated_words
