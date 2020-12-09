from threading import Thread, Semaphore
import random
import names # pip install names
from time import sleep

def agregar(list_user):
	for x in range(10):
		semaforo.acquire()
		list_user[x] = names.get_first_name()
		print("Agregar", list_user[x], "a indice", x)
		semaforo.release()
		sleep(0.005)

def eliminar(list_user):
	for x in range(10):
		index = random.randint(0,9)
		semaforo.acquire()
		try:
			del list_user[index]
			print("ELIMINAR Indice", index, "-> eliminado")
		except:
			print("ELIMINAR Indice", index, "-> error al eliminar")
		semaforo.release()
		sleep(0.005)

def modificar(list_user):
	for x in range(10):
		index = random.randint(0,9)
		semaforo.acquire()
		try:
			name_curr = list_user[index]
			list_user[index] = names.get_first_name()
			print("MODIFICAR Indice", index, "-> modificado de", name_curr, "a", list_user[index])
		except:
			print("MODIFICAR Indice", index, "-> error al modificar")
		semaforo.release()
		sleep(0.005)

def buscar(list_user):
	for x in range(10):
		index = random.randint(0,9)
		semaforo.acquire()
		try:
			print("BUSCAR Indice", index, "-> encontrado con usuario", list_user[index])
		except:
			print("BUSCAR Indice", index, "-> error al encontrar usuario")
		semaforo.release()
		sleep(0.005)

def leer_todo(list_user):
	print(list_user)

if __name__ == '__main__': # main del programa
	semaforo = Semaphore(1) # semaforo
	index = random.randint(1,10) # creacion de indice aleatorio
	list_user = {} # indice : nombre

	hilo1 = Thread(target = agregar, args=(list_user,))
	hilo2 = Thread(target = eliminar, args=(list_user,))
	hilo3 = Thread(target = modificar, args=(list_user,))
	hilo4 = Thread(target = buscar, args=(list_user,))
	hilo1.start()
	hilo2.start()
	hilo3.start()
	hilo4.start()

	hilo1.join()
	hilo2.join()
	hilo3.join()
	hilo4.join()

	leer_todo(list_user)
