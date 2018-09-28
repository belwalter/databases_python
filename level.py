import plyvel

db = plyvel.DB('/home/walter/db', create_if_missing=True)


dic = {'walter': {'edad':30, 'apellido': 'bel'}}

lista = [1,2,3,'hola']

db.put(b'F', str(dic).encode('utf-8'))
db.put(b'D', str(lista).encode('utf-8'))

key = 'F'
db.put(key.encode(),"hola mundo desde LevelDB".encode())


for key, value in db:
    print ("clave:", key.decode('utf-8'))
    print ("valor:", value.decode('utf-8'))

valor = eval(db.get(b'C').decode('utf-8'))
valor2 = eval(db.get(b'D').decode('utf-8'))
print(valor)
print(valor2)

db.delete(b'F')

db.close()