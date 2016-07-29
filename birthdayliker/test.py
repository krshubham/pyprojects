import facebook

token = input("Paste your Facebook access token over here: ")

graph = facebook.GraphAPI(token)

me = graph.get_object('me')

myfeed = graph.get_connections('me','feed')

posts = myfeed['data']


words = ['bday','hbd','bday','birthday','HBD']
for post in posts:
	try:
		for i in words:
			if(i in post['message']):
				print("Yes")
	except KeyError:
		#this means that its a story
		#Let's grab the id of the story
		id = str(post['id'])
		story = graph.get_object(id)
		for i in words:
			try:
				if(i in story['message']):
					graph.put_like(id)
				else:
					continue
			except KeyError:
				continue
