import configparser
from sys import argv
import requests

cp = configparser.RawConfigParser()
file = argv[1]
cp.read(file)

url = cp.get('GitLab', 'InstanceUrl')
token = cp.get('GitLab', 'PersonalAccessToken')
project = cp.get('Project', 'Id')
featureFlagName = cp.get('Project', 'FeatureFlag')

reqUrl = f"{url}/api/v4/projects/{project}/feature_flags/{featureFlagName}"
headers = { "PRIVATE-TOKEN": f'{token}' }

data = requests.get(reqUrl, headers=headers)
json = data.json()

if json["active"]:
  print(1)
else:
  print(0) 
