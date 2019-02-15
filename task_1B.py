import string
def common():
    fin = open('Book1.txt')
    line = fin.readline()
    s1 = set()
    for line in fin:
        word = line.strip()
        word = word.split()
        punctuation = string.punctuation
        for words in word:
            words = words.strip(punctuation)
            s1.add(words)
    fin = open('Book2.txt')
    line = fin.readline()
    s2 = set()
    for line in fin:
        word = line.strip()
        word = word.split()
        punctuation = string.punctuation
        for words in word:
            words = words.strip(punctuation)
            s2.add(words)
    fin = open('Book3.txt')
    line = fin.readline()
    s3 = set()
    for line in fin:
        word = line.strip()
        word = word.split()
        punctuation = string.punctuation
        for words in word:
            words = words.strip(punctuation)
            s3.add(words)
    sfinal = set()
    sfinal = s1 & s2 & s3
    print(sfinal)
common()



