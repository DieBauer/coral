from httpMethods import *

# Create the graph (profiling cities)
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"httpbroadcast"}}})
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"stats", "params":{"field": "amount"}, "group":{"by":"city"}}}})
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"zscore", "params":{"by":"city", "field": "amount","score" : 1.0}}}})

patch('/api/actors/1',  {"data": {"type": "actors", "id": "1", "attributes": {"input":{"trigger":{"in":{"type":"external"}}}}}})
patch('/api/actors/2',  {"data": {"type": "actors", "id": "2", "attributes": {"input":{"trigger":{"in":{"type":"actor", "source":1}}}}}})
patch('/api/actors/3',  {"data": {"type": "actors", "id": "3", "attributes": {"input":{"trigger":{"in":{"type":"actor", "source":1}},"collect":{"stats":{"type":"actor", "source":2}}}}}})