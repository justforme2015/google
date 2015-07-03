#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.



2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def create_dict(filename):
  lines_of_file = open(filename, 'rU')
  words = []
  
  for line in lines_of_file:
    line.strip()
    words.extend(line.split())
  
  counted_words = {}
  for word in words:
    if word.lower() in counted_words:
      counted_words[word.lower()] += 1
    else:
      counted_words[word.lower()] = 1
  return counted_words    

def print_words(filename):
  dict_of_words = create_dict(filename)
  all_words = dict_of_words.keys()
  sorted_all_words = sorted(all_words)
  for word in sorted_all_words:
    print word  + " " + str(dict_of_words[word])

# top_words contains 20 tuples, (word, ferquency)  pairs

def where_min(top_words):
  current_min = ("inf", -1)
  for i in range(min(20, len(top_words))):
    if top_words[i][1] < current_min[0]:
      current_min = (top_words[i][1], i)
  return current_min    


def print_top(filename):
  dict_of_words = create_dict(filename)
  all_words = dict_of_words.keys()
  
  top_words = []
  for word in all_words[:20]:
    top_words.append((word, dict_of_words[word]))

  current_min = where_min(top_words)

  for word in all_words[20:]:
    if dict_of_words[word] > current_min[0]:
      top_words[current_min[1]] = (word, dict_of_words[word])
      current_min = where_min(top_words)

  print sorted(top_words, key=lambda tuple: tuple[1], reverse = True)    




  
  # finds the plcae and value of the least frequency



  









###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
