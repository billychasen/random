
from urllib2 import urlopen
import cjson

def is_music(entry):
    for c in entry['category']:
        if c['term'].lower() == 'music':
            return True
    return False

def call_the_tubes(count=50, skip=0, vids="all"):
    if not skip:
        skip = 1
    # This is YouTube's API call.  It took some searching around on their docs to figure out
    # It's located here.  I'm using v2 of it. https://developers.google.com/youtube/
    url = 'https://gdata.youtube.com/feeds/api/videos?orderby=viewCount&time=all_time&max-results=%s&start-index=%s&v=2&alt=json' % (count, skip)
    res = cjson.decode(urlopen(url).read())
    for r in res['feed']['entry']:
        if vids == "all" or (vids == "music" and is_music(r)) \
                or (vids == "other" and not is_music(r)):        
            print "%s,%s,%s" % (r['media$group']['yt$duration']['seconds'], 
                                r['yt$statistics']['viewCount'], r['media$group']['media$player']['url'])

if __name__=='__main__':
    # I arbitrarily decided on 1,000ish points as that's around when their API
    # would start getting angry at me
    for i in xrange(0,20):
        # change all to other or music to only select those datapoints
        call_the_tubes(50, (i*50) + (i*1), vids="all")
