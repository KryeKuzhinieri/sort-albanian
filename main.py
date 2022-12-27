from sorter import sort_albanian

TEST_WORDS_1 = [
    "Drenë",
    "Guxim",
    "Erjetë",
    "Ilir",
    "Dedë",
    "Agim",
    "Jetmirë",
    "Symirë",
    "Thëllënëz",
    "Bardhyl",
    "Shpend",
    "Besë",
    "Dhuratë",
    "Çiljetë",
    "Adriatik",
]

TEST_WORDS_2 = [
    "Tingull",
    "Tungjatjeta",
    "Fllad",
    "Përçudnuar",
    "Rrno",
    "Vlerë",
    "Atdhe",
    "Shtojzovalle",
    "Tymnajë",
    "Xixë",
    "Pëgërë",
    "Dashni",
    "Vjosë",
    "Jon",
    "Dimërofsh",
    "Katërçipërisht",
    "Zonjë",
    "Ëndërr",
    "Fisnik",
    "Puhizë",
]

TEST_WORDS_3 = [
    "Thupër",
    "Tytë",

    "Shok",
    "Supë",

    "Dhëmb",
    "Ditë",

    "Gjatë",
    "Gomë",
]


def main(words):
    return sort_albanian(words=words)


if __name__ == '__main__':
    print(f"Original words: {TEST_WORDS_1}.")
    sorted_words = main(words=TEST_WORDS_1)
    print(f"English sorted words: {sorted(TEST_WORDS_1)}.")
    print(f"Albanian sorted words: {sorted_words}.", "\n\n")

    print(f"Original words: {TEST_WORDS_2}.")
    sorted_words = main(words=TEST_WORDS_2)
    print(f"English sorted words: {sorted(TEST_WORDS_2)}.")
    print(f"Albanian sorted words: {sorted_words}.", "\n\n")

    print(f"Original words: {TEST_WORDS_3}.")
    sorted_words = main(words=TEST_WORDS_3)
    print(f"English sorted words: {sorted(TEST_WORDS_3)}.")
    print(f"Albanian sorted words: {sorted_words}.", "\n\n")
