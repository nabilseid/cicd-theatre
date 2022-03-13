# Github action playing ground

## Encrypted Secrets
Secrets are encrypted environmental variables such as tokens, access_keys for
github action to access. There are three levels to store secrets. In preceding order they are:
- Organization-level: can be accessed by multiple repos in organization
- repository-level: available for a specific repo only
- environment-level: same with repo-level with additional required reviewers to control access 

The lowest level have precedence when secrets are duplicated accross levels.

To make secret available to action, set the secret as input or environment variable in workflow



