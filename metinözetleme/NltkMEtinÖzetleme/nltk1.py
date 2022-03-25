import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import time

start = time.time()
metin = """What really divides the parties

So what is the gap between Labour and the Tories nowadays?

One Starbucks, one Rymans and one small Greek cafe as it happens. Both parties have now completed their moves to new headquarters, with Labour creating its election hub just three doors away from the Tories' new headquarters in Victoria Street, just down the road from the Commons. That should make things a little easier if and when the crack-of-dawn election press conferences kick off. Unlike 2001, there should be no need for colleagues to have taxis gunning their engines outside, or to buy scooters, to get themselves between the tightly-timetabled events.

And, to all intents and purposes, we already appear to be in that general election campaign. Certainly the press conference hosted by election co-ordinator Alan Milburn, in the rather compact new conference room - still smelling of new carpet and with the garish New Labour coffee mugs as yet unstained - had all the hallmarks of an election event.

"Welcome to the unremittingly New Labour media centre," he said. And I'll bet he hadn't checked that one with Gordon Brown. Along with Work and Pensions Secretary Alan Johnson and Minister for Work Jane Kennedy, he then went on to tear into the Tory plans to scrap the New Deal welfare-to-work scheme, which they claimed would lead to an increase of almost 300,000 in unemployment. And they ridiculed the claims made on Monday by Michael Howard that he could save £35 billion of Labour waste and inefficiency to spend on public services while also offering £4 billion of tax cuts. Labour has come up with a figure of £22 billions worth of efficiency savings so, understandably perhaps, believe Mr Howard must be planning cuts to squeeze the extra £13 billion. These figures, based on the two parties' own detailed studies, will be battered to within an inch of their lives during the campaign. Wednesday was just the start.
"""
cumlelistesi = nltk.sent_tokenize(metin)
stopwords = nltk.corpus.stopwords.words('english')
frekans = {}

for kelime in nltk.word_tokenize(metin):
    if kelime not in stopwords:
        if kelime not in frekans.keys():
            frekans[kelime] = 1
        else:
            frekans[kelime] += 1
    max_frekans = max(frekans.values())
for kelime in frekans.keys():
    frekans[kelime] = (frekans[kelime]/max_frekans)
cummle_skoru = {}
for sent in cumlelistesi :
    for kelime in nltk.word_tokenize(sent.lower()):
        if kelime in frekans.keys():
            if len(sent.split(' ')) < 30:
                if sent not in cummle_skoru.keys():
                    cummle_skoru[sent] = frekans[kelime]
                else:
                    cummle_skoru[sent] += frekans[kelime]

import heapq
özet_cumle = heapq.nlargest(3, cummle_skoru, key=cummle_skoru.get)

özet = ' '.join(özet_cumle)
print(özet)
end1 = time.time()
süre=end1 - start
print("Özetleme süresi",süre)
 
satırlar=metin.splitlines()#satırlarına ayırma
b=0#keimesatisinı tutmak için değişken
for i in satırlar:
    kelimeler=i.split()
    for a in kelimeler:
        b=b+1
print(b)

ösatırlar=özet.splitlines()#satırlarına ayırma
c=0#keimesatisinı tutmak için değişken
for i in ösatırlar:
    kelimeler=i.split()
    for a in kelimeler:
        c=c+1
print(c)
        

özet_oran=100-((c/b)*100)
print("Nltk Özetleme yüzdesi:",özet_oran)




