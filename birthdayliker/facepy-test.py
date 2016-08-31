from facepy import GraphAPI


graph = GraphAPI('EAACEdEose0cBALf5o0p85GsmFeo2ZAad1ZBq30QHqWHxzc1BZAMoosFpeANJr6GZBZAXcauZARUfzRXWlnh7ug06O9VOxm4ODenHTeCtGSAquEx3aXr0Sl0a9WzoY5YUJODaxm95s1h4rxbM7RwrX4lUHGhs4LVha7eiZAZBQq1mZAAZDZD')


feed = graph.get('me/feed',limit=5)

paging = feed['paging']

data = feed['data']

for i in feed['data']:
	print i
	print('')