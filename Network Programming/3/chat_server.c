#include <stdio.h> 
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <unistd.h> 
#define PORT 8080
#define MAX 80
#define SA struct sockaddr
void main(){

    int sockfd; 
    char buff[MAX];
    struct sockaddr_in servaddr, clientaddr;

    sockfd = socket(AF_INET,SOCK_STREAM, 0);
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);
    bind(sockfd,(SA *)&servaddr,sizeof(servaddr));
    listen(sockfd,10);
    //accept returns a connection file descriptor which is nothing but the main identifier for the
    int connfd = accept(sockfd,(SA*)&clientaddr, sizeof(struct sockaddr_in));
    while(1){
        memset(buff,'.',sizeof(buff));
        recv(connfd, buff,sizeof(buff),0);
        if(strcmp(buff,"exit")==0){
            break;
        }
        printf("From client to server: %s",buff);
        printf("Enter your message to the client");
        fgets(buff, sizeof(buff), stdin);
        send(connfd,buff,sizeof(buff),0);
    }
    close(connfd);
}