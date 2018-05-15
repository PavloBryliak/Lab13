from pathlib import Path
from linkedstack import LinkedStack


class PalindromADT:

    def __init__(self):
        self.words = []
        self.palindroms = []

    def read(self, path):
        path = Path(path)
        path.parent.mkdir(exist_ok=True)
        f = open(path)
        self.words = list(map(lambda x: x.strip(), f.readlines()))

    @staticmethod
    def _is_palindrom(word):
        word = word.lower()
        ls = LinkedStack()
        for i, c in enumerate(word):
            if i < len(word) // 2:
                ls.push(c)
            elif i >= (len(word) - 1) // 2 + 1:
                if c != ls.pop():
                    return False
        return True

    def process(self):
        self.palindroms = list(filter(PalindromADT._is_palindrom, self.words))

    def write(self, path):
        new_words = list(map(lambda x: x + "\n", self.palindroms))
        with open(path, "w") as f:
            f.writelines(new_words)


if __name__ == "__main__":
    pl = PalindromADT()
    pl.read("words.txt")
    pl.process()
    pl.write("new_words.txt")
