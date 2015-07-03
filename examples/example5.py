from httpMethods import *

post('/api/actors', {"data": {"type":"actors", "attributes": {"type": "httpbroadcast"}}})
post('/api/actors', {"data": {"type":"actors", "attributes": {"type": "linearregression", "params": {"intercept": 0.1, "weights":{"salary": 0.43, "age": 1.8 }}}}})

patch('/api/actors/1',  {"data": {"type":"actors", "id": "1", "attributes": {"input":{"trigger":{"in":{"type":"external"}}}}}})
patch('/api/actors/2',  {"data": {"type":"actors", "id": "2", "attributes": {"input":{"trigger":{"in":{"type":"actor", "source":1}}}}}})
