import facebook

token = "EAACEdEose0cBAOgplgLYsWNZBHedsy7LIvifFgZCV2txee2rZASuo6veIO9GzyqGcmZB4ZCyLRqxlNC8ZC91iaXW9P5neekgKNQ9AYvuVUWDc2q9HVnKikxVrbaBTDXdZBASb9k9hZAwmFEcmQyRkfCq5ULLp05XPoV6ZCsq6opQZAuAZDZD"

graph = facebook.GraphAPI(token)

me = graph.get_object('me')

friends = graph.get_connections('me','friends')

myfeed = graph.get_connections('me','feed')

posts = myfeed['data'][0]['id']

words = ['bday','hbd','bday','birthday','HBD']

print(posts['likes']['paging']['cursors']['after'])

feedLink = feeds['paging']['next'].replace('https://graph.facebook.com/', '')

gr