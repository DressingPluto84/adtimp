#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>
            
#define MAXCLIENT 3
            
void* readAndWriteThread(void* arg);
void* writeToAll(char* buf);

pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static pthread_t myThreads[MAXCLIENT];
static int myClients[MAXCLIENT];

struct sockInf{
    struct sockaddr_in ssa;
    int rfd;
    char name[32];
};

int main(int argc, char* argv[]) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(54484);
    struct in_addr local;
    local.s_addr = INADDR_ANY;
    addr.sin_addr = local;

    int binding = bind(sock, (struct sockaddr *) &addr, sizeof(addr));
    if (binding == -1) {
	perror("bind");
	exit(1);
    }

    int lis = listen(sock, 10);
    if (lis == -1) {
	perror("Listen");
	exit(1);
    }

    struct sockaddr_in connected;
    socklen_t sizeAddr = sizeof(connected);

    static int currClients = 0;

    while (currClients < MAXCLIENT) {
        int realfd = accept(sock, (struct sockaddr *) &connected, &sizeAddr);
        myClients[currClients] = realfd;

	char clstr[INET_ADDRSTRLEN];
	inet_ntop(AF_INET, &(connected.sin_addr), clstr, INET_ADDRSTRLEN);
	printf("Connected Client IP %s\n", clstr);

	char buf_name[32];
	int name_len = read(realfd, buf_name, 32);
	buf_name[name_len] = '\0';
	struct sockInf *s = malloc(sizeof(struct sockInf));
	s->ssa = connected;
	s->rfd = realfd;
	strcpy(s->name, buf_name);
	
	int pcre = pthread_create(&(myThreads[currClients]), NULL, readAndWriteThread, (void *) s);
	
	if (pcre != 0) {
	   perror("thread create");
	   exit(1);
	}	


	currClients += 1;
    }

    for (int i = 0; i < MAXCLIENT; i++) {
	if (pthread_join(myThreads[i], NULL) != 0) {
	    perror("join pthread");
	    exit(1);
	}	
    }

    return 0;
}


void* readAndWriteThread(void* arg) {
    int sock = ((struct sockInf*) arg)->rfd;

    char buffer[512];
    char buf2[550];
    int n;
    
    while ((n = read(sock, &buffer, 512)) > 0) {
	strcat(buf2, ((struct sockInf*) arg)->name);
	strcat(buf2, ": ");
	buffer[n] = '\0';
	strcat(buf2, buffer);
        writeToAll(buf2);
	for (int i = 0; i < 550; i++) {
	    buf2[i] = '\0';
	}
    }    
    
    close(sock);
    return (void *) NULL;
}

void* writeToAll(char* buf) {
    printf("%s\n", buf);
    pthread_mutex_lock(&mtx);
    for (int i = 0; i < MAXCLIENT; i++) {
	if (!pthread_equal(myThreads[i], pthread_self())) {
	    write(myClients[i], buf, strlen(buf));
        }
    }
    pthread_mutex_unlock(&mtx);
    return (void *) NULL;
}
