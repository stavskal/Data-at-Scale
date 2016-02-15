import sys,json
import re

def main():
	count=0
	tweet_file=open(sys.argv[1])
	scores={}
	i=0
	for line in tweet_file:
		score=0
		js = json.loads(line)
		a=js.keys()
		if 'text' in js.keys():
			words = js.get('text','').encode('ascii','ignore')
			words = words.split()
			for word in words:
				count += 1
				#word = word.encode('utf8')
				word = word.rstrip()
				if word in scores:
					scores[word] += 1
				else:
					scores[word] = 1

	for item in scores.keys():
		print"%s %s" % (item , float(scores[item])/count)		



if __name__ == '__main__':
    main()
