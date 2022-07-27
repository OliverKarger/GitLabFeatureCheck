## What is this?
This simple Tool fetches the Information about a specified "Feature Flag" from GitLab. <br>
- API Key and Instance URL are stored in a Config File
- Project ID and Feature Tag Name are passed as args

## Usage

`python(3) main.py <configfile> <project id> <feature flag name>`<br>
`gfc.exe <configfile> <project id> <feature flag name>`

## Config File
```
[GitLab]
InstanceUrl=<gitlb url>
PersonalAccessToken=<personal access token with api access>
```
