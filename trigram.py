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


trigrams = zip(document,document[1:],document[2:])
transitions = defaultdict(list)
starts=[]
for prev,current,nexte in trigrams:
    if prev==".":
       starts.append(current)
    transitions[(prev,current)].append(nexte)
#print transitions

def generate_using_trigrams():
    current =random.choice(starts)
    prev ="."
    result=[current]
    while True:
        next_word_candidates = transitions[(prev,current)]
        next_word = random.choice(next_word_candidates)

        prev, current = current, next_word
        result.append(current)
        if current == ".":
            return " ".join(result)

print generate_using_trigrams()