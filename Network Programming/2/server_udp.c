#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define PORT 8080
#define MAXLINE 1024

int main(){
    int sockfd;
    char buffer[MAXLINE];
    char *msg;
    struct sockaddr_in servaddr, clientaddr;
    sockfd = socket(AF_INET,SOCK_DGRAM,0); 
    if(sockfd<0){
        perror("socket creation failed");
        exit(EXIT_FAILURE);   
    }

    memset(&servaddr,0, sizeof(servaddr));
    memset(&clientaddr,0, sizeof(clientaddr));
    

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);



    if(bind(sockfd, (const struct sockaddr *) &servaddr, sizeof(servaddr))<0){
        perror("socket bind failed");
        exit(EXIT_FAILURE);
    }

    int len; int n;
    len = sizeof(clientaddr);
    n = recvfrom(sockfd, (char *)buffer, MAXLINE, MSG_WAITALL, ( struct sockaddr *) &clientaddr,&len);

    buffer[n] = '\0';
	printf("Client : %s\n", buffer);
    printf("Enter you message:\n");
    fgets(msg, MAXLINE ,stdin);
	sendto(sockfd,(const char *)msg, strlen(msg),MSG_CONFIRM, (const struct sockaddr *) &clientaddr, len);
	printf("Hello message sent.\n");
	return 0;
}