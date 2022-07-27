import configparser
from sys import argv
import requests

def read_config():
  try:
    cp = configparser.RawConfigParser()
    file = argv[1]
    cp.read(file)
    config = {
      "url": cp.get('GitLab', 'InstanceUrl'),
      "token": cp.get('GitLab', 'PersonalAccessToken'),
      "project": argv[2],
      "featureFlagName": argv[3]
    }
    return config
  except:
    print("<read_config> Internal Application Error")
    return {}

def make_request(config):
  try:
    reqUrl = f"{config['url']}/api/v4/projects/{config['project']}/feature_flags/{config['featureFlagName']}"
    headers = { "PRIVATE-TOKEN": f'{config["token"]}' }

    data = requests.get(reqUrl, headers=headers)
    
    if data.status_code == 404:
      print("ERROR - 404 Not Found!")
    if data.status_code == 403:
      print("ERROR - 403 Unauthorized")
    if data.status_code == 500:
      print("ERROR - 500 Internal Server Error")
    return data.json()
  except:
    print("<make_request> Internal Application Error")
    
def parse(result):
  try:
    if result["active"]:
      print(1)
    else:
      print(0) 
  except:
    print("<parse> Internal Application Error")

config = read_config()
response = make_request(config)
parse(response)