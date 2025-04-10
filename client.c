#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>

void* readThread(void* arg);
void* writeThread(void* arg);

int main(int argc, char* argv[]) {
    if (argc != 2) {
	exit(1);
    }

    int sox = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in ss;
    ss.sin_family = AF_INET;
    ss.sin_port = htons(54484);
    inet_pton(AF_INET, "10.0.0.140", &ss.sin_addr);
    
    int c = connect(sox, (struct sockaddr *) &ss, sizeof(ss));

    if (c < 0) {
	perror("connect");
	exit(1);
    }

    pthread_t reading;
    pthread_t writing;
 
    write(sox, argv[1], sizeof(argv[1]));
    int prv = pthread_create(&reading, NULL, readThread, (void *) sox);
    if (prv != 0) {
	perror("read thread");
	exit(1);
    }

    int pwv = pthread_create(&writing, NULL, writeThread, (void *) sox);

    if (pwv != 0) {
	perror("write thread");
	exit(1);
    }

    pthread_join(reading, NULL);
    pthread_join(writing, NULL);

    close(sox);
    return 0;
}

void* readThread(void* arg) {
    int fd = (int) arg;
    char buffer[512];
    int n;

    while((n = read(fd, buffer, sizeof(buffer))) > 0) {
	buffer[n] = '\0';
	printf("%s", buffer);
	fflush(stdout);
    }
    return (void*) NULL;
}

void* writeThread(void* arg) {
    int fd = (int) arg;
    char buffer[512];
    
    while(1) {
        fgets(buffer, sizeof(buffer), stdin);
	buffer[511] = '\0';
	write(fd, buffer, strlen(buffer));
    }
    return (void *) NULL;
}
