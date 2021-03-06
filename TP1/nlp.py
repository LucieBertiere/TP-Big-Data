# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nVibkpQJE05Vf1lV3XoS39cGlrOWfTJy
"""

class Sentence :
  def __init__(self, text):
    # text of the sentence
    self.text = text
    # the sentence is splitted into a list of words
    self.word_list = self.text.split()


class Word :

  def __init__(self, sentence):
    # one word
    self.length = 1 
    # length of the sentence
    self.length_sentence = len(sentence.word_list)
    # the word is in the list of words of the sentence (i.e. it is a subclass of the sentence)
    self.word_list = sentence.word_list
    
  def __iter__(self):
    # First place of the word in the sentence, on which we are going to iterate
    self.x=0
    return self  

  def __next__(self):
    # we move the place of the word in the sentence to get the next bigram
    if self.x + 1 < self.length_sentence:
            self.x = self.x + 1
    # if we have reached the end of the sentence we stop the iteration
    elif self.x + 1 >= self.length_sentence :
      raise StopIteration
    # we return the bigram
    return(' '.join(self.word_list[self.x-1:self.x+1]))