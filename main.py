import config
import requests
import json
from datetime import datetime, timedelta

now = datetime.now()
output = 'data.csv'
open(output, 'w')
fcsv = open(output, 'a+')
print >> fcsv, "date,events"

for d in reversed(range(364)):
    date_after = (now - timedelta(days=(d + 1))).strftime("%Y-%m-%d")
    date_current = (now - timedelta(days=d)).strftime("%Y-%m-%d")
    date_before = (now - timedelta(days=(d - 1))).strftime("%Y-%m-%d")

    headers = {'PRIVATE-TOKEN': config.privatetoken}

    params = (('before',date_before),('after',date_after),('per_page', '99'))

    response = requests.get(config.gitlaburl,headers=headers,params=params)

    result = str((len(response.json())))

    print >> fcsv, date_current, ",", result
