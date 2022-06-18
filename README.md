# GitHubAPI

## Install Repository using pip

### Windows
```
pip install Py-Github-9045
```

### Linux/Ubuntu/MacOS
```
python3 pip3 install Py-Github-9045
```

## Usage

### Import Section
```python
from GitHubAPI.main import GithubAPI
```

### Initialization
```python
# create object of class.
gh = GithubAPI(GITHUB_TOKEN, "henishpatel9045", "demo", "demo@gmail.com", "This is demo repo.", True)
```

### Create New Repository
```python
# Create New Repository.
gh.create_new_repo()
```

### Create New Repository using public template repository.
```python
# Create new repository from template repository.
# demo-template repository must be public template repository.
gh.create_repo_from_template("henishpatel9045", "demo-template")
```

### Create New file with content.
```python
# Create new file with content
# demo repository must be created in username
gh.update_file("js.config", "This is just demo file creation.")
```

### Add Environment variable in repository.
```python
# Create environment variables in repository.
gh.add_environment_variable("USER_PASSWORD", "1234567890*")
```

## Sample Code
```python
from GitHubAPI.main import GithubAPI
import os

# It is best to store your token in environment variable.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# create object of class.
gh = GithubAPI(GITHUB_TOKEN, "henishpatel9045", "demo", "demo@gmail.com", "This is demo repo.", True)


# Create New Repository.
gh.create_new_repo()

# Create new repository from template repository.
# demo-template repository must be public template repository.
gh.create_repo_from_template("henishpatel9045", "demo-template")

# Create new file with content
# demo repository must be created in username
gh.update_file("js.config", "This is just demo file creation.")

# Create environment variables in repository.
gh.add_environment_variable("USER_PASSWORD", "1234567890*")
```
