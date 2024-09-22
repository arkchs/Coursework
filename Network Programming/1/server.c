#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
int main() {
    char str[100];
    int listen_fd, comm_fd;
    struct sockaddr_in servaddr;
    //socket id for passively listening for any connection requests
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(10000);
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);


    bind(listen_fd, (struct sockaddr *)&servaddr, sizeof(servaddr));
    listen(listen_fd, 10);
    comm_fd = accept(listen_fd, (struct sockaddr *)NULL, NULL);
    // while (1) {
        // printf("%d",comm_fd);
        while(1){
            bzero(str, 100);
            recv(comm_fd, str, 100, 0);
            if (strncmp("exit", str, 4) == 0) { 
                printf("Server Exit...\n");
                close(comm_fd);
                exit(0); 
            }
            printf("From Client: %s", str);
            bzero(str, 100);
            fgets(str,100,stdin);     
            send(comm_fd, str, strlen(str), 0);	
        }

    // }

    return 0;
}
