import sys,json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
    	term,score = line.split('\t')
    	scores[term] = int(score)
    #print(scores.items())
    
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
    	score=0
    	js = json.loads(line)
    	if 'text' in js.keys():
    		#print(js.keys())
    		words = js['text'].split(' ')
    		for word in words:
    			word = word.encode('utf8')
    			if word in scores:
    				score += scores[word]
    	print(score)

  #  hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
