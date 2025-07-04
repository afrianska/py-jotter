from pathlib import Path


def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exitst.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ["lorem.txt", "alice.txt", "loki.txt", "jenny.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)
