'''Using python-twiiter module for streaming all MoS tweets'''

import twitter

api = twitter.Api(consumer_key='the_key',
                      consumer_secret='secret_key',
                      access_token_key='access_token',
                      access_token_secret='secret_access_token')

print(api.VerifyCredentials())
#{"id": 16133, "location": "Philadelphia", "name": "bear"}

#Generate search query from here: https://twitter.com/search-advanced.
results = api.GetSearch(raw_query="=from%3ASarcasmMother") 

print results