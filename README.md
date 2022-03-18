# Github action playing ground

## Encrypted Secrets
Secrets are encrypted environmental variables such as tokens, access_keys for
github action to access. There are three levels to store secrets. In preceding order they are:
- Organization-level: can be accessed by multiple repos in organization
- repository-level: available for a specific repo only
- environment-level: same with repo-level with additional required reviewers to control access 

The lowest level have precedence when secrets are duplicated accross levels.

To make secret available to action, set the secret as input or environment variable in workflow

## Dependent Jobs 
All jobs in a workflow run parallal by default. If jobs are inter-dependent, you can sepecify
dependencies of a job by using `needs` keyword. If a job fails, all dependent jobs will be 
skipped; however can keep a job coninue by using `if` conditional statement.

```yml
jobs:
  setup:
    name: Setting up
    runs-on: ubuntu-latest
    steps:
      - name: Setting actions up
        run: echo 'Oh well! here we are setting up'

  build:
    needs: setup
    name: Building
    runs-on: ubuntu-latest
    steps:
      - name: Building actions
        run: echo 'What are we building really! 😕'

  test:
    needs: build
    name: Testing
    runs-on: ubuntu-latest
    steps:
      - name: Testing actions
        run: echo 'Finally! testing nothing'
```


# CircleCi Notes

## Green build

