import config
import requests
import json
from datetime import datetime, timedelta

now = datetime.now()

for d in reversed(range(365)):
    date_after = (now - timedelta(days=(d + 1))).strftime("%Y-%m-%d")
    date_current = (now - timedelta(days=d)).strftime("%Y-%m-%d")
    date_before = (now - timedelta(days=(d - 1))).strftime("%Y-%m-%d")


    headers = {
        'PRIVATE-TOKEN': config.privatetoken,
    }

    params = (
        ('before',date_before),
        ('after',date_after),
        ('per_page', '99'),
    )

    response = requests.get(config.gitlaburl,headers=headers,params=params)
