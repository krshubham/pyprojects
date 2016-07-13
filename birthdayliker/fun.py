import facebook

graph = facebook.GraphAPI('EAAC1bqIXC1YBAPFIJqrxS0psLCSoWZA4ElhkkhgI7FlQEj0qqc15JGZBogK2DTXqHpm8OjnhhSJE3xOG48J55Fxb1f32xOrZAEHPeZAonCcsqP62vQF3oRiqusAhVFksgYBGPliRD30IzKw1sVv824e0B2AQBmsZD')

me = graph.get_object('me')

print(me)

feed = graph.get_connections('me','photos')

print(feed['data'])

# for i in range(len(feed['data'])):
# 	try:
# 		print(feed['data'][i]['message'])
# 		print('')
# 	except KeyError:
# 		print(feed['data'][i]['story'])
# 		print('')