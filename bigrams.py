from bs4 import BeautifulSoup
import requests
import re
import random
from collections import defaultdict
url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
html=requests.get(url).text
soup=BeautifulSoup(html,'html5lib')

def fix_unicde(text):
    return text.replace(u"\u2019","'")

content = soup.find("div","article-body")
regex = r"[\w']+|[\.]"
document=[]

for paragraph in content("p"):
    words=re.findall(regex,fix_unicde(paragraph.text))
    document.extend(words)


bigrams = zip(document,document[1:])
transitions = defaultdict(list)
for prev,current in bigrams:
    transitions[prev].append(current)

def generate_using_bigrams():
    current ="."
    result=[]
    while True:
        next_word_candidates = transitions[current]
        current = random.choice(next_word_candidates)
        result.append(current)
        if current == ".":
            return " ".join(result)


print generate_using_bigrams()