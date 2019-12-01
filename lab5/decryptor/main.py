from decryptor import *


def main():
    dec = Decryptor(create_letters_freq())
    dec.decrypt('data.txt', 'output_test.txt')


if __name__ == '__main__':
    main()
