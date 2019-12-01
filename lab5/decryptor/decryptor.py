import operator

from cryptogram import Cryptogram


def create_letters_freq():
    letters_freq = {
        'a': 89, 'i': 82, 'o': 78, 'e': 77, 'z': 56, 'n': 55, 'r': 47, 'w': 47, 's': 43, 't': 40, 'c': 40, 'y': 38,
        'k': 35, 'd': 33, 'p': 31, 'm': 28, 'u': 25, 'j': 23, 'l': 21, 'b': 15, 'g': 14, 'h': 11, 'f': 3, 'q': 1,
        'v': 1, 'x': 1, ' ': 100, ',': 16, '.': 12, '-': 12, '"': 11, '!': 10, '?': 8, ':': 10, ';': 10, '(': 10,
        ')': 10
    }
    # Big letters - 1% frequency
    for i in range(65, 91):
        letters_freq[chr(i)] = 10  #letters_freq[chr(i).lower()] /

    # Numbers - 1% frequency
    for i in range(48, 58):
        letters_freq[chr(i)] = 10

    return letters_freq


class Decryptor:
    def __init__(self, letters_freq_table):
        self.cryptograms = []
        self.letters_freq = letters_freq_table

    def get_cryptograms_from_file(self, data_file):
        self.cryptograms.clear()
        with open(data_file, 'r') as file:
            for line in file:
                self.cryptograms.append(Cryptogram(line))

    def _find_key(self):
        key = []
        longest = 0

        for crypt in self.cryptograms:
            if len(crypt.chars) > longest:
                longest = len(crypt.chars)

        for i in range(0, longest):
            possible_key = {}
            matching_cryptograms = []

            for crypt in self.cryptograms:
                if i < len(crypt.chars):
                    matching_cryptograms.append(crypt)

            for crypt in matching_cryptograms:
                for possible in self.letters_freq.keys():
                    tmp = ord(crypt.char_at(i)) ^ ord(possible)
                    freq_points = self.letters_freq[possible]

                    if tmp not in possible_key.keys():
                        possible_key[tmp] = freq_points
                    else:
                        possible_key[tmp] = possible_key.get(tmp) + freq_points

            tmp_sorted = sorted(possible_key.items(), key=operator.itemgetter(1), reverse=True)
            possible_key = dict(tmp_sorted)

            best_possible = ord(' ')
            best_counter = 0

            for possible in possible_key.keys():
                counter = 0

                for crypt in matching_cryptograms:
                    if (chr(ord(crypt.char_at(i)) ^ possible)) in self.letters_freq.keys():
                        counter += 1

                if counter > best_counter:
                    best_counter = counter
                    best_possible = possible

            key.append(best_possible)

        return key

    def write_output(self, output_filename):
        key = self._find_key()
        with open(output_filename, 'w') as file:
            for crypt in self.cryptograms:
                for i in range(0, len(crypt.chars)):
                    file.write(chr(ord(crypt.char_at(i)) ^ key[i]))
                file.write('\n')

    def decrypt(self, input_file, output_file):
        self.get_cryptograms_from_file(input_file)
        self.write_output(output_file)
