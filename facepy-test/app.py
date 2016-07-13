from facepy import GraphAPI

graph = GraphAPI('EAAC1bqIXC1YBAPFIJqrxS0psLCSoWZA4ElhkkhgI7FlQEj0qqc15JGZBogK2DTXqHpm8OjnhhSJE3xOG48J55Fxb1f32xOrZAEHPeZAonCcsqP62vQF3oRiqusAhVFksgYBGPliRD30IzKw1sVv824e0B2AQBmsZD')

me = graph.get('me')

feed = graph.get('me/inbox')

feed_data = feed['data']

print(feed_data)
