from os import listdir
from os.path import isfile, join
from datetime import  date, datetime
import frontmatter
import json

def processArticle(path):
    post = frontmatter.load(path)
    obj = {}
    obj['readTime'] = str(len(post.content.split()) / 250) + " minutes"
    obj['words'] = len(post.content.split())
    for key in post.keys():
        obj[key] = post[key]
    return obj

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

if __name__ == '__main__':
    index = [] # article meta info

    # get mardown file names in directory
    articles = [f for f in listdir('./') if isfile(join('./', f)) and f[-3:] == '.md']

    for article in articles:
        index.append(processArticle(article))
    with open('index.json', 'w') as outfile:
        json.dump(index, outfile, default=json_serial)



# title
# publish date - needs to be number (for sort/orderby)
# date updated
# thumbnail image
# tags -> most common unusual words?
# total words -> time to read // 250wpm Read time is based on the average reading speed of an adult (roughly 275 WPM). We take the total word count of a post and translate it into minutes. Then, we add 12 seconds for each inline image. Boom, read time.
