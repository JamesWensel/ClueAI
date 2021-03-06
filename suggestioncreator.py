# -*- coding: utf-8 -*-
"""SuggestionCreator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sslqIRkMdBCoIJL8VopFjeuYfldmyg-c
"""

import random 
flip = random.randint(0,1)
print(flip)

class CreateSuggestion():
  def __init__(self, cards=[]):
    self.people = ['Rev Green', 'Colonel Mustard', 'Professor Plum', 'Mrs. Peacock',
      'Miss Scarlett', 'Mrs. White']
    self.weapons = ['Candlestick', 'Dagger', 'Lead Pipe', 'Revolver',
      'Rope', 'Wrench']
    self.rooms = ['Ballroom', 'Billiard Room', 'Conservatory', 'Dining Room',
      'Hall', 'Kitchen', 'Library', 'Lounge', 'Study']

    self.personKnown = False
    self.weaponKnown = False
    self.roomKnown = False

    self.cards_and_center = {
        'People': [],
        'Weapons': []
    }

    for i in cards: 
      if i in self.people: 
        self.options['People'] += [i]
      elif i in self.weapons:
        self.options['Weapons'] += [i]
    
  def generate_suggestion(self, room, known, dontHave, unknown, unsolved):
    for i in known['Center']:
      if i in self.people:
        self.personKnown = True
      elif i in self.weapons:
        self.weaponKnown = True
      elif i in self.rooms:
        self.roomKnown = True
   
    scores = {}

    for cur in unknown:
      if cur in self.rooms:
        continue
      temp = 0
      for j in dontHave:
        if cur in dontHave[j]:
          temp += 1
      for j in unsolved: 
        if cur in unsolved[j]['suggestion']:
          temp += 1
      scores[cur] = temp
    
    per = unknown[0]
    pscore = 0
    weap = unknown[0]
    wscore = 0

    for i in scores:
      if i in self.people and scores[i] > pscore:
        per = i
        pscore = scores[i]
      elif i in self.weapons and scores[i] > wscore:
        weap = i
        wscore = scores[i]

    for i in unknown: 
      if i in self.people and pscore == 0:
        per = i
      elif i in self.weapons and wscore == 0:
        weap = i
    
    if room not in known and not self.roomKnown: 
      if self.personKnown or not self.weaponKnown and pscore < wscore and len(self.cards_and_center['People']) > 0:
        per = self.cards_and_center['People'][0]
      if self.weaponKnown or not self.personKnown and pscore >= wscore and len(self.cards_and_center['Weapons']) > 0:
        weap = self.cards_and_center['Weapons'][0]
    
    return [per, weap, room]

    def card_to_show(self, sug):

