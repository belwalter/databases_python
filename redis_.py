# -*- coding: utf-8 -*-



import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


#for i in range (65, 91):
#    r.set(chr(i),random.randint(1000,9999))

#for i in range (65, 91):
#    print(int(r.get(chr(i))))


#print(r.lrange('newusers', 0, -1))
#print(r.keys())
#dic = {"a": "abcd"}

#r.set("diccionario", dic)

#dic = dic(r.get("diccionario"))

#r.georadius("va-universidad", -32.400000, -58.200000, 400, unit="km", withdist=True, withcoord=True, withhash=True)

"""
claves = r.keys()

for clave in claves:
    try:    
        print(r.get(clave))
    except:
        print(r.lrange(clave, 0, -1))
"""

#r.delete(1)
