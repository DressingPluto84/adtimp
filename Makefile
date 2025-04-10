create: server.c client.c
	gcc -Wall -g -o server server.c
	gcc -Wall -g -o client client.c
