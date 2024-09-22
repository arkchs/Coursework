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
    struct sockaddr_in servaddr;

    sockfd = socket(AF_INET,SOCK_STREAM, 0);
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);
    connect(sockfd,(SA *)&servaddr,sizeof(servaddr));
    while(1){
        memset(buff,'.',sizeof(buff));
        printf("Enter your message to the server:");
        fgets(buff, sizeof(buff), stdin);
        send(sockfd,buff,sizeof(buff),0);
        memset(buff,'.',sizeof(buff));
        recv(sockfd, buff,sizeof(buff),0);
        if(strcmp(buff,"exit")==0){
            break;
        }
        printf("From server to client: %s",buff);
    }
}