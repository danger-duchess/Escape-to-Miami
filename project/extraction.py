from bs4 import BeautifulSoup as bs
import requests
import csv
import random

# webpages we can use
webpage1 = 'https://www.google.com/search?client=firefox-b-1-d&q=florida'  # pretty much all coronavirus articles
webpage2 = 'https://www.usatoday.com/story/news/nation/2019/12/09/florida-man-headlines-2019-meme-florida-man-challenge-birthday/2629205001/'


# function to read in nonessential words from csv file 'nonessentials.csv'
def read_csv():
    nonessn = []

    # nonessentials can be stored in this csv file
    with open('nonessentials.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for i in row:
                nonessn.append(i)
    return nonessn


# function to return the text extracted from the website
def parse_website(webpage, need_val):
    # extract html data from website
    html = requests.get(webpage)
    page_data = html.content

    # finding text
    parser = bs(page_data, 'html.parser')
    act_txt = parser.find_all(text=need_val)
    return act_txt


# function to return a list of the sentences to choose scenarios from
def get_words(act_txt, nonessn):
    choices = []

    # get the list of words to choose from for scenarios
    for t in act_txt:
        if t.parent.name not in nonessentials and '{}'.format(t) not in nonessn:
            choices.append('{} '.format(t))
    return choices


# function to get rid of \n characters in the middle of sentences
def strip_string(choices):
    fin_choices = []
    for i in choices:
        fin_choices.append(i.replace('\n', ""))
    return fin_choices


# read in list of nonessential items
nonessentials = read_csv()

actual_text1 = parse_website(webpage1, True)
actual_text2 = parse_website(webpage2, True)

# clean up choices
final_choices1 = [i for i in strip_string(get_words(actual_text1, nonessentials)) if len(i) >= 15]

final_choices2 = [i for i in strip_string(get_words(actual_text2, nonessentials)) if len(i) >= 15]
del(final_choices2[0:11])
del(final_choices2[-3:])

# create master list of choices
final_choices = final_choices1 + final_choices2
print(final_choices)

# create random scenario
scenario = "Oh no!  " + random.choice(final_choices2)
