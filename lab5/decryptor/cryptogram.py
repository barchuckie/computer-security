class Cryptogram:
    def __init__(self, data):
        self.chars = []
        tmp = str(data).split(' ')

        for c in tmp:
            self.chars.append(chr(int(c, 2)))

    def char_at(self, index):
        if index < len(self.chars):
            return self.chars[index]
        else:
            return '*'
