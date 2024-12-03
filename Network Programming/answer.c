#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#define PORT 80
int main(int argc, char const *argv[])
{ 
    int cliport, server_fd, new_socket; long valread;
    char *ip;
    struct sockaddr_in address, cliaddr;
    
    //server response //3 marks
    char *server_response = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: 90\n\n<!DOCTYPE HTML><HTML><body><h1>Home Page</h1></body></HTML>";
    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
        { perror("In socket"); exit(EXIT_FAILURE); }
    //creating address
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = htonl(INADDR_ANY);
    address.sin_port = htons(PORT);

    memset(address.sin_zero, '\0', sizeof address.sin_zero);
    //binding socket with address
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address))<0)
        { perror("In bind"); exit(EXIT_FAILURE); }
    if (listen(server_fd, 10) < 0)
        { perror("In listen"); exit(EXIT_FAILURE); }
        int addrlen = sizeof(cliaddr);
    while(1)
    {
        printf("\n+++++++ Waiting for new connection ++++++++\n\n");
        if (new_socket = accept(server_fd, (struct sockaddr *)&cliaddr, (socklen_t*)&addrlen)<0) //2 marks
            { perror("Accept error"); exit(EXIT_FAILURE); }
        printf("haha");
        char buffer[30000] = {0};
        valread = read( new_socket , buffer, 30000);
        printf("%s\n",buffer );
        write(new_socket , server_response , strlen(server_response));
        ip = inet_ntoa(cliaddr.sin_addr);
        // This function may also used inet_ntop (AF_INET, &cliaddr.sin_addr, ip, sizeof(ip));
        cliport = ntohs(cliaddr.sin_port);
        close(new_socket); return 0; 
    }
}