import config
import requests
import json
from datetime import datetime, timedelta

now = datetime.now()

for d in reversed(range(365)):
    date_after = (now - timedelta(days=(d + 1))).strftime("%Y-%m-%d")
    date_current = (now - timedelta(days=d)).strftime("%Y-%m-%d")
    date_before = (now - timedelta(days=(d - 1))).strftime("%Y-%m-%d")
