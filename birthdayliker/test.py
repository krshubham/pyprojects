import facebook

graph = facebook.GraphAPI('EAAC1bqIXC1YBAPFIJqrxS0psLCSoWZA4ElhkkhgI7FlQEj0qqc15JGZBogK2DTXqHpm8OjnhhSJE3xOG48J55Fxb1f32xOrZAEHPeZAonCcsqP62vQF3oRiqusAhVFksgYBGPliRD30IzKw1sVv824e0B2AQBmsZD')

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
