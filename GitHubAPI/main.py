import requests
import base64
from nacl import encoding, public	

def encrypt(public_key: str, secret_value: str):
	public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
	sealed_box = public.SealedBox(public_key)
	encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
	return base64.b64encode(encrypted).decode("utf-8")


class GithubAPI:
  headers = {"Authorization": "","Accept": "application/vnd.github.v3+json"}
  baseURL = "https://api.github.com/"
  payload = ""
  
  repo_owner = ""
  repo_name = ""
  repo_description = ""
  email = ""
  is_repo_private = False
    
  
  def __init__(self, token, repo_owner, repo_name, email, repo_description="", is_private=False):
    self.GITHUB_TOKEN = token
    self.headers["Authorization"] = "token " + self.token;
    self.repo_owner = repo_owner
    self.repo_name = repo_name
    self.repo_description = repo_description
    self.email = email
    self.is_repo_private = is_private
    
  def create_repo_from_template(self, template_owner, template_repo):
    self.payload = '{"owner": "' + self.repo_owner + '", "name": "' + self.repo_name + '", "description": "' + self.repo_description + '", "include_all_branches": false, "private": ' + str(self.is_repo_private).lower() + '}'
    url = self.baseURL + f"repos/{template_owner}/{template_repo}/generate"
    return requests.post(url, data=self.payload, headers=self.headers).json()
  
  def create_new_repo(self):
    self.payload = '{"name": "'+self.repo_name+'", "description": "'+self.repo_description+'", "private": '+str(self.is_repo_private).lower()+'}'
    url = self.baseURL + "user/repos"
    return requests.post(url, data=self.payload, headers=self.headers).json()
  
  # NEW FILE REQUIRED 
  # NOT WORK ON EXISTING FILE
  def update_file(self, path, content, message="", ):    
    self.payload = '{"message":"' + message + '","content":"' +  base64.b64encode(content.encode("ascii")).decode("ascii") + '"}'
    url = self.baseURL + f"repos/{self.repo_owner}/{self.repo_name}/contents/{path}"
    return requests.put(url, data=self.payload, headers=self.headers).json()
  
  def get_public_key(self):
    self.payload = '{"owner": "'+self.repo_owner+'", "repo": "'+self.repo_name+'"}'
    url = self.baseURL + f"repos/{self.repo_owner}/{self.repo_name}/actions/secrets/public-key"	
    return requests.get(url, data=self.payload, headers=self.headers).json()
  
  def add_environment_variable(self, key, value):
    tmp = dict(self.get_public_key(self.repo_owner, self.repo_name))
    enc_value = encrypt(tmp.get("key"), value)
    self.payload = '{"encrypted_value":"' + enc_value + '","key_id":"' + tmp.get("key_id") +'"}'
    url = self.baseURL + f"repos/{self.repo_owner}/{self.repo_name}/actions/secrets/{key}"	
    return requests.put(url, data=self.payload, headers=self.headers).json()
