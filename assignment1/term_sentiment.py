import sys,json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    newscores = {}
    for line in sent_file:
    	term,score = line.split('\t')
    	scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
    	score=0
    	pos=0
    	neg=0
    	js = json.loads(line)
    	if 'text' in js.keys():
    		words = js['text'].split(' ')
    		exist = [i for i in words if i in scores]

    		# if not all words already have a score
    		if len(exist)<len(words):
	    		#count number of positive and negative words in tweet
	    		for word in words:
	    			word = word.encode('utf8')
	    			if word in scores:
	    				if scores[word]>0:
	    					pos += 1
	    				elif scores[word]<0:
	    					neg += 1

	    		for word in words:
	    			word = word.encode('utf8')
	    			if word not in scores:
	    				if word not in newscores:
	    					newscores[word]=0
	    					if neg>0:
	    						newscores[word]+=float(pos)/neg
	    					else:
	    						newscores[word]+=pos
	    				else:
	    					if neg>0:
	    						newscores[word]+=float(pos)/neg
	    					else:
	    						newscores[word]+=pos
	    				print word , newscores[word]		
	    				




if __name__ == '__main__':
    main()
