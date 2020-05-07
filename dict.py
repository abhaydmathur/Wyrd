def check(word):
    with open('words_alpha.txt') as f:
        datafile = f.readlines()
        for line in datafile:

            line = line[:-1]
            if word == line:
                return True
    return False

if __name__ == "__main__":
    print(check('kow'))