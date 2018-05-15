from linkedstack import LinkedStack


class PalindromADT:

    def __init__(self):
        self.words = []
        self.palindroms = []

    def read(self, path, format=lambda x: x.strip()):
        f = open(path)
        self.words = list(map(format, f.readlines()))  # way 1

    @staticmethod
    def _is_palindrom(word):
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
    pl.read("base.lst", format=lambda x: x.split(' ', 1))
    pl.process()
    pl.write("new_ukr_words.txt")