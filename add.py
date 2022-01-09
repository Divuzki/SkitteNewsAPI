import requests
from django.contrib.auth import get_user_model
User = get_user_model()
url = 'https://newsapi.org/v2/everything?q=techcrunch&apiKey=b7de039e294740bb84d8dff8c2bbf97d'
headers = {'Accept': 'application/json'}
auth = ('username', 'userpass')
response = requests.get(url, headers=headers, auth=auth)

with open('outputfile.json', 'wb') as outf:
    outf.write(response.content)

import json
from core.models import Post
user = User.objects.first()
with open('outputfile.json') as f:
    posts_json = json.load(f)
for post in posts_json:
    post = Post(user=user,source=post['source'],author=post['author'],title=post['title'], description=post['description'],content=post['content'],urlToImage=post['urlToImage'],urlToPost=post['url'])
    post.save()