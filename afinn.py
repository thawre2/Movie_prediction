

import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
a=0.0
b=0.0
c=0.0

# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = 'AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))

# Word splitter pattern
pattern_split = re.compile(r"\W+")
def sentiment(text):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)

    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
    else:
        sentiment = 0

    return sentiment
	
if __name__ == '__main__':
    total=0
    pv=0
    nv=0
    nt=0
    rate=0.0



    ## Open the file with read only permit
    f = open('dilwale.json')
    ## Read the first line
    line = f.readline()
    ## If the file is not empty keep reading line one at a time
    ## till the file is empty
    while line:
        total=total+1
        if(sentiment(line))>0:
            pv += 1
            print( (sentiment(line), line))
        elif ((sentiment(line)) < 0):
            nv += 1
            print( (sentiment(line), line))
        else:
            nt += 1

        line = f.readline()
    f.close()
  
    pvage=(pv)*100/(total-nt)
    rate=(pvage)*5.0/100.0

    print("***********************************Status***********************************************")
    print("Number of positive comments/tweets:- " , pv)

    print("Number of negative comments/tweets:- " , nv)
    print("total comments/ tweets are:- ", (total-nt))

    print((pvage))
    print("Rating:",rate)





  #