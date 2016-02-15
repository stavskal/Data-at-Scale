import sys,json
import re, operator

def main():
	count=0
	tweet_file=open(sys.argv[1])
	scores={}
	i=0
	for line in tweet_file:
		score=0
		js = json.loads(line)
		a=js.keys()
		if 'entities' in js.keys():
			hasht=js['entities']['hashtags']
			for i in range(0,len(hasht)):
				count += 1
				if 'text' in hasht[i].keys():
					temphash=hasht[i]['text'].encode('ascii','ignore')
					if temphash in scores:
						scores[temphash] += 1
					else:
						scores[temphash] = 1

	#sorted_hashtags= sorted(scores.items(), key=operator.itemgetter(1),reverse=True)
	sorted_hash = [(item[0],item[1]) for item in scores.items()]
	sorted_by_val = sorted(sorted_hash, key =lambda tup: tup[1], reverse=True)
	i=0	
	while(i<10):
		print sorted_by_val[i][0], sorted_by_val[i][1]
		i+=1



if __name__ == '__main__':
    main()
