#include <stdio.h> 
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <unistd.h> 
#define MAX 80 
#define PORT 8080 
#define SA struct sockaddr 


void func(int connfd) 
{ 
	char buff[MAX]; 
	int n; 
	
	while(1) { 
		bzero(buff, MAX);//turning all the values in the buffer to be zero
		read(connfd, buff, sizeof(buff)); //accept the value from the user
		printf("From client: %s\t To client : ", buff);
		bzero(buff, MAX); //erase the buffer
		n = 0; 
		while ((buff[n++] = getchar()) != '\n');//incrementally accept the character from the user into the buffer
		write(connfd, buff, sizeof(buff));
		if (strncmp("exit", buff, 4) == 0) { 
			printf("Server Exit...\n"); 
			break; 
		} 
	} 
} 


int main() 
{ 
	int sockfd, connfd, len; 
	struct sockaddr_in servaddr, clientaddr; 

	
	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	// if (sockfd == -1) { 
	// 	printf("socket creation failed...\n"); 
	// 	exit(0); 
	// } 
	// else
	// 	printf("Socket successfully created..\n");
	bzero(&servaddr, sizeof(servaddr)); 
	servaddr.sin_family = AF_INET; 
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
	servaddr.sin_port = htons(PORT); 
	int bind_works = bind(sockfd, (SA*)&servaddr, sizeof(servaddr));
	// if ((bind_works) != 0) { 
	// 	printf("socket bind failed...\n"); 
	// 	exit(0); 
	// } 
	// else
	// 	printf("Socket successfully binded..\n");
	int listen_works= listen(sockfd, 10); 	
	// if ((listen_works) != 0) {
	// 	printf("Listen failed...\n"); 
	// 	exit(0); 
	// } 
	// else
	// 	printf("Server listening..\n"); 
	// len = sizeof(cli);
	connfd = accept(sockfd, (SA*)&clientaddr, &len); 
	// if (connfd == -1) { 
	// 	printf("server accept failed...\n"); 
	// 	exit(0); 
	// } 
	// else
	// 	printf("server accept the client...\n"); 
	func(connfd); 
	close(sockfd); 
}
