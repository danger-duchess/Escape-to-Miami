from bs4 import BeautifulSoup as bs
import requests
import csv
import random

need_val = True  # for when a certain attribute is needed

# extract html data from website
webpage = 'https://www.google.com/search?client=firefox-b-1-d&q=florida'
html = requests.get(webpage)
page_data = html.content

# finding text
parser = bs(page_data, 'html.parser')
actual_text = parser.find_all(text=need_val)

# eliminate nonessential text
nonessentials = ['[document]', 'script', 'footer', 'body', 'style', 'div', 'header']

# nonessentials can be stored in this csv file (randomly broke after working fine and I can't figure it out)
"""with open('nonessentials.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for i in row:
            nonessentials.append(i)"""

# get the list of words to choose from for scenarios
choices = []
for t in actual_text:
    if t.parent.name not in nonessentials:
        choices.append('{} '.format(t))
del choices[0:28]
del choices[-13:-1]

scenario = "Oh no!  " + random.choice(choices)

