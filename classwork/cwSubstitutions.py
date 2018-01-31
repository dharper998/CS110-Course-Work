import json

def main():
    jsondict = json.loads(open("substitutiondict.json", "r").read())
    article = open('substitutionarticle.txt', 'r')
    articletext = article.read()
    for key in jsondict:
        news = articletext.replace(key, jsondict[key])
    betternews = open("betternews.txt", 'w')
    betternews.write(news)
    betternews.close()
main()
