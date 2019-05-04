"""Library for preprocessing. Extracted code from nodebooks."""

import re

START_SYMBOL='<s>'
STOP_SYMBOL='</s>'

def tokenize(l):
  for b in l.rstrip().split(' '):
    for c in re.split(r'(\W+)', b):
      if c != '':
        yield(c)

def tokenize_num(l):
  for b in l.rstrip().split(' '):
    if b != '':
      yield(b)

def get_vocabs(*files):
  vocab_set = set()

  for filename in files:
    with open(filename, 'r') as f:
      for l in f:
        vocab_set.update(tokenize(l))

  if "" in vocab_set:
    vocab_set.remove("")
    
  return list(vocab_set | set([START_SYMBOL, STOP_SYMBOL]))

def generate_mapping_from_vocabs(filename, vocab):
  with open(filename, 'w') as f:
    for i, v in enumerate(vocab):
      f.write(f"{v}\t{i}\n")

def load_mapping_from_vocabs(file, convert_to_int=True):
  mapping = {}
  with open(file, 'r') as f:
    for l in f:
      k, v = l.rstrip().split('\t')
      if convert_to_int:
        mapping[k] = int(v)
      else:
        mapping[k] = v
  return mapping

def transform_data(mapping, file):
  seqs = []
  with open(file, 'r') as f:
    for l in f:
      line_mapping = [mapping[t] if t in mapping else t for t in tokenize(l) ]
      seqs.append(line_mapping)
  
  return seqs

def writing_seq_idx(filename, seqs):
  with open(filename, 'w') as f:
    for l in seqs:
      f.write(" ".join(l) + "\n")