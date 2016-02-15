import sys,json



states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}



def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
        term,score = line.split('\t')
        scores[term] = int(score)
    #print(scores.items())

    state_sentiment={}
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        score=0
        js = json.loads(line)
        if 'user' and 'text' in js.keys():
                words = js['text'].split(' ')
                for word in words:
                        word = word.encode('utf8')
                        if word in scores:
                                score += scores[word]
                loc=js['user']
                if 'location' in loc and loc['location']!=None:
                        location = loc['location'].split(',')
                        for item in location:
                                if item in states:
                                        if item not in state_sentiment:
                                                state_sentiment[item] = score
                                        else:
                                                state_sentiment[item] += score
                                                print(state_sentiment)

if __name__ == '__main__':
    main()
