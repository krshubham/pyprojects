import facebook

graph = facebook.GraphAPI('EAAC1bqIXC1YBAPFIJqrxS0psLCSoWZA4ElhkkhgI7FlQEj0qqc15JGZBogK2DTXqHpm8OjnhhSJE3xOG48J55Fxb1f32xOrZAEHPeZAonCcsqP62vQF3oRiqusAhVFksgYBGPliRD30IzKw1sVv824e0B2AQBmsZD')

me = graph.get_object('me')

print(me)

myphotos = graph.get_connections('me','photos')

for i in myphotos['data']:
	print(graph.get_connections(str(i['id']),'caption'))