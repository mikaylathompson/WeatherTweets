# Compile a data set of storm tweets.  
# Save the text, the geolocation, and the time for each.

import json, sys
from TwitterAPI import TwitterAPI

storm_words = ["storm", "rain", "thunder", "lightning","thunderstorm",
                "downpour","cloudburst","raining", "thundering","downpouring","storming"]
save_file = "storm_texts_08-08.json"



def isUsefulTweet(tweet):
    text = tweet['text'].lower()
    if "hpa" in text or "baro" in text or "mph" in text or "nws" in text:
        return False
    if (tweet['coordinates'] is None):
        return False
    if (tweet['place']['country'] != "United States"):
        return False
    return True

auth_file = open('auth_data.json','r')
auth = json.load(auth_file)
auth_file.close()
api = TwitterAPI(auth['apikey'], auth['apisecret'],
        auth['accesstoken'],auth['accesssecret'])
r = api.request('statuses/filter', {'track':storm_words})

assert(r.stream)

count = 0

with open(save_file, 'a') as output:
    try:
        output.write("[")
        for item in r.get_iterator():
            if isUsefulTweet(item):
                count += 1
                idata = {}
                idata['text'] = item['text']
                idata['coords'] = item['coordinates']['coordinates']
                idata['geo']= item['geo']['coordinates']
                idata['place'] = item['place']['full_name']
                idata['country'] = item['place']['country']
                idata['location'] = item['user']['location']
                idata['time'] = item['created_at']
                if (count > 1):
                    output.write(",\n")
                output.write(json.dumps(idata))
                print item['text']
                print item['place']['full_name']
                print
    except KeyboardInterrupt:
        output.write("]")
        print "\n", count, "items added to file."
        sys.exit()

