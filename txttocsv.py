import json
import csv


f = open('soln3.csv','a',encoding='utf-8')
csvWriter = csv.writer(f)
headers=['full_text']
csvWriter.writerow(headers)

for inputFile in ['streamingpartfinal.txt']:#all the text-file names you want to convert to Csv in the sae folder as this code
    tweets = []
    for line in open(inputFile, 'r'):
        tweets.append(json.loads(line))

    print('number of tweets',len(tweets))
    count_lines=0
    for tweet in tweets:
        try:
            csvWriter.writerow([tweet['full_text']])
            count_lines+=1
        except Exception as e:
            print(e)
    print(count_lines)