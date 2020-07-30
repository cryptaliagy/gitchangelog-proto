import json
import os

with open('package.json', 'r') as f:
    data = json.loads(f)
data['version'] = os.environ.get('VERSION')
with open('package.json', 'w') as f:
    json.dump(data, f)
