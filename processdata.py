"""Library for preprocessing. Extracted code from nodebooks."""

import re

START_SYMBOL='<s>'
STOP_SYMBOL='</s>'

def tokenize(l):
  for b in l.rstrip().split(' '):
    for c in re.split(r'(\W+)', b):
      if c != '':
        yield(c)

def get_vocabs(*files):
  vocab_set = set()

  for filename in files:
    with open(filename, 'r') as f:
      for l in f:
        vocab_set.update(tokenize(l))

  if "" in vocab_set:
    vocab_set.remove("")
    
  return list(vocab_set | set([START_SYMBOL, STOP_SYMBOL]))

def generate_mapping_from_vocabs(vocab):
  with open('data/loglinear/vocab_mapping.txt', 'w') as f:
    for i, v in enumerate(vocab):
      f.write(f"{v}\t{i}\n")