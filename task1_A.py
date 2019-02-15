import string

fout = open("Book1.txt",'r')
fout = fout.read()
words = fout.split("\n")

def unique_words():
  unique_words = []
  if words in fout:
    if words not in fout:
      unique_words[word] = 1
    else:
      unique_word[word] += 1

def count_the_article():
  str1 = []
  fout = open("Book1.txt",'r')
  r = fout.readlines()
  for line in r:
    str2 = line.lower().strip(string.punctuation + string.whitespace)
    str1 += str2
  total = {}
  for word in  str1:
    total[word] = total.get(word, 0) + 1
  words_t = len(str1)
  words_d = len(total.keys())
  print("Total Words : " + str(words_d))

def sorted_words():
  sorted_words = []
  fout = open("Book2.txt",'r')
  r=fout.readlines()
  r.sort(key=len)
  print(r)

def character_word_count(words):
  char_word_count = dict()
  for word in words:
    if word not in char_word_count:
      char_word_count[word] = 1
    else:
      char_word_count[word] += 1
  print(char_word_count)


def starts_with_vow():
  t = ("a", "e" ,"i", "o", "u")
  
print(count_the_article())
sorted_words()
unique_words()

character_word_count(words)