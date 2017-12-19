
import time
import sys, os
import socket
import argparse
from pathlib import Path

from random import randint

# Valeur maximale engendrée
MAX_INT = 10000
# Temps d'attente maximale
ATTENTE_MAX = 3

def main(argv=None):
	"""Programme produisant des flux de données via une socket"""

	# On accepte des arguments
	parser = argparse.ArgumentParser(description='Simulateur de flux.')
	parser.add_argument('--host', dest='host',
                   help='IP de la machine (default: localhost)')
	parser.add_argument('--port', dest='port', type=int,
                   help='Port de la socket (défaut 9000)')
	parser.add_argument('--source', dest='source', 
                   help='Source des données: fichier ou répertoire')
	args = parser.parse_args()
	
	if args.host is not None:
		host = args.host
	else:
		host = "localhost"
	if args.port is not None:
		port = args.port
	else:
		port = 9000
	if args.source is not None:
		source = args.source
		if os.path.exists(source):
			if os.path.isdir(source):
				data_mode = "dir"
				print("Le chemin " + source + " est un répertoire. Je vais envoyer les fichiers.")
				files = []
				for file in os.listdir(source):
					if os.path.isfile(os.path.join(source, file)):
						files.append(file)
				nb_files = len(files)
			elif os.path.isfile(source):
				data_mode = "file"
				f = open(source, "r")
				lines = f.readlines()
				nb_lines = len(lines)
				f.close()
				print("Le chemin " + source + " est un fichier. Je vais envoyer les lignes.")
		else:
			sys.exit ("Le chemin " + source + " n'existe pas. Vérifiez SVP.")
	else:
		# On va engendrer des données aléatoirement
		data_mode = "random"
		
	# Creation de la socket sur laquelle on écrit
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind((host, port))

	# La socket se met en attente de connexion
	serversocket.listen(1)

	i_file = 0
	i_line = 0
	while True:
		print ("J'attends une connexion sur " + host + ":" + str(port) + "...")
		connection, client_address = serversocket.accept()

		# Connexion recue !
		try:
			print ("J'ai reçu une connexion de  " + str(client_address))
			
			# On boucle 
			while True:
				# On envoie des données
				attente = randint(0, ATTENTE_MAX)
				print ("Attente " + str(attente) + " secondes ")
				time.sleep( attente)
				
				if data_mode == "random":
					val = randint(0, MAX_INT)
					message = str(val) + "\n"
				elif data_mode == "dir":
					i_file = i_file+1
					if i_file == nb_files:
						i_file = 0
					message = Path(os.path.join(source, files[i_file])).read_text().replace("\n", "") +"\n"
				elif data_mode == "file":
					i_line = i_line+1
					if i_line == nb_lines:
						i_line = 0
					message = lines[i_line]
					
				print("Envoi de " + message)
				connection.send(message.encode())
		except:
			# Nettoyage de la connexion
			print("Cette connextion est terminée.")
			connection.close()

if __name__ == "__main__":
	main()