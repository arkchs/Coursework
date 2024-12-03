//multicast sender--------------------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define MULTICAST_IP "224.0.0.1"
#define PORT 8080

int main() {
    int sock;
    struct sockaddr_in multicast_addr;
    char *message = "Hello, Multicast Group!";

    // Create UDP socket
    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Set up multicast address
    memset(&multicast_addr, 0, sizeof(multicast_addr));
    multicast_addr.sin_family = AF_INET;
    multicast_addr.sin_port = htons(PORT);
    multicast_addr.sin_addr.s_addr = inet_addr(MULTICAST_IP);

    // Send message to multicast group
    if (sendto(sock, message, strlen(message), 0, (struct sockaddr *)&multicast_addr, sizeof(multicast_addr)) < 0) {
        perror("Multicast message failed");
        close(sock);
        exit(EXIT_FAILURE);
    }

    printf("Multicast message sent: %s\n", message);

    close(sock);
    return 0;
}





//multicast receiver--------------------------------------------------------------------------------------------


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define MULTICAST_IP "224.0.0.1"
#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock;
    struct sockaddr_in local_addr;
    struct ip_mreq multicast_request;
    char buffer[BUFFER_SIZE];

    // Create UDP socket
    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Bind socket to local address and port
    memset(&local_addr, 0, sizeof(local_addr));
    local_addr.sin_family = AF_INET;
    local_addr.sin_port = htons(PORT);
    local_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sock, (struct sockaddr *)&local_addr, sizeof(local_addr)) < 0) {
        perror("Bind failed");
        close(sock);
        exit(EXIT_FAILURE);
    }

    // Join the multicast group
    multicast_request.imr_multiaddr.s_addr = inet_addr(MULTICAST_IP);
    multicast_request.imr_interface.s_addr = INADDR_ANY;

    if (setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP, &multicast_request, sizeof(multicast_request)) < 0) {
        perror("Failed to join multicast group");
        close(sock);
        exit(EXIT_FAILURE);
    }

    // Receive multicast messages
    printf("Listening for multicast messages...\n");
    while (1) {
        memset(buffer, 0, BUFFER_SIZE);
        int bytes_received = recvfrom(sock, buffer, BUFFER_SIZE, 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("Receive failed");
            break;
        }
        printf("Received multicast message: %s\n", buffer);
    }

    close(sock);
    return 0;
}



//normal tcp server

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addr_len = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    // Create socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }

    // Bind the socket to the specified IP and port
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("Listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Server is listening on port %d\n", PORT);

    // Accept incoming connections
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addr_len)) < 0) {
        perror("Accept failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Connection established with client\n");

    // Echo loop: read from client and send back the same data
    while (1) {
        memset(buffer, 0, BUFFER_SIZE);
        int bytes_read = read(new_socket, buffer, BUFFER_SIZE);
        if (bytes_read <= 0) {
            printf("Client disconnected\n");
            break;
        }

        printf("Received: %s\n", buffer);

        // Send the data back to the client
        send(new_socket, buffer, bytes_read, 0);
    }

    close(new_socket);
    close(server_fd);
    return 0;
}



//normal tcp client 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char buffer[BUFFER_SIZE] = {0};
    char message[BUFFER_SIZE];

    // Create socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation error");
        exit(EXIT_FAILURE);
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        perror("Invalid address/Address not supported");
        close(sock);
        exit(EXIT_FAILURE);
    }

    // Connect to the server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection failed");
        close(sock);
        exit(EXIT_FAILURE);
    }

    printf("Connected to the server\n");

    // Communication loop
    while (1) {
        printf("Enter message: ");
        fgets(message, BUFFER_SIZE, stdin);

        // Remove newline character
        message[strcspn(message, "\n")] = 0;

        // Exit if user types "exit"
        if (strcmp(message, "exit") == 0) {
            printf("Closing connection\n");
            break;
        }

        // Send message to server
        send(sock, message, strlen(message), 0);

        // Receive and print the echoed message
        int bytes_read = read(sock, buffer, BUFFER_SIZE);
        buffer[bytes_read] = '\0';
        printf("Echoed from server: %s\n", buffer);
    }

    close(sock);
    return 0;
}





//normal udp server

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_socket;
    struct sockaddr_in server_addr, client_addr;
    char buffer[BUFFER_SIZE];
    socklen_t addr_len = sizeof(client_addr);

    // Create a UDP socket
    if ((server_socket = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configure server address structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Accept connections from any IP
    server_addr.sin_port = htons(PORT);

    // Bind the socket to the specified port and address
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("UDP Server is running on port %d\n", PORT);

    // Server loop to receive and respond to messages
    while (1) {
        memset(buffer, 0, BUFFER_SIZE);

        // Receive message from client
        int bytes_received = recvfrom(server_socket, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_len);
        if (bytes_received < 0) {
            perror("Receive failed");
            break;
        }

        printf("Received message: %s\n", buffer);

        // Echo the message back to the client
        const char *response = "Message received!";
        sendto(server_socket, response, strlen(response), 0, (struct sockaddr *)&client_addr, addr_len);
    }

    close(server_socket);
    return 0;
}


//normal udp client

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "127.0.0.1" // Replace with the server's IP if running on different machines
#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int client_socket;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];
    socklen_t addr_len = sizeof(server_addr);

    // Create a UDP socket
    if ((client_socket = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configure server address structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);

    // Client loop to send messages
    while (1) {
        printf("Enter message to send (type 'exit' to quit): ");
        fgets(buffer, BUFFER_SIZE, stdin);

        // Remove newline character
        buffer[strcspn(buffer, "\n")] = 0;

        // Exit the loop if the user types 'exit'
        if (strcmp(buffer, "exit") == 0) {
            printf("Exiting...\n");
            break;
        }

        // Send the message to the server
        sendto(client_socket, buffer, strlen(buffer), 0, (struct sockaddr *)&server_addr, addr_len);

        // Receive the server's response
        int bytes_received = recvfrom(client_socket, buffer, BUFFER_SIZE, 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("Receive failed");
            break;
        }

        buffer[bytes_received] = '\0'; // Null-terminate the received data
        printf("Server response: %s\n", buffer);
    }

    close(client_socket);
    return 0;
}



//broadcasting server 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define BROADCAST_IP "192.168.1.255" // Replace with your subnet's broadcast IP
#define PORT 8080
#define MESSAGE "Broadcast message from server!"

int main() {
    int server_socket;
    struct sockaddr_in broadcast_addr;
    int broadcast_enable = 1;

    // Create UDP socket
    if ((server_socket = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Enable broadcast option
    if (setsockopt(server_socket, SOL_SOCKET, SO_BROADCAST, &broadcast_enable, sizeof(broadcast_enable)) < 0) {
        perror("Failed to enable broadcast option");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Configure broadcast address
    memset(&broadcast_addr, 0, sizeof(broadcast_addr));
    broadcast_addr.sin_family = AF_INET;
    broadcast_addr.sin_port = htons(PORT);
    broadcast_addr.sin_addr.s_addr = inet_addr(BROADCAST_IP);

    printf("Broadcast server is running...\n");

    // Send broadcast messages in a loop
    while (1) {
        if (sendto(server_socket, MESSAGE, strlen(MESSAGE), 0, (struct sockaddr *)&broadcast_addr, sizeof(broadcast_addr)) < 0) {
            perror("Broadcast failed");
            break;
        }
        printf("Broadcast message sent: %s\n", MESSAGE);
        sleep(3); // Broadcast every 3 seconds
    }

    close(server_socket);
    return 0;
}



//broadcasting client

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int client_socket;
    struct sockaddr_in client_addr;
    char buffer[BUFFER_SIZE];
    socklen_t addr_len = sizeof(client_addr);

    // Create UDP socket
    if ((client_socket = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configure client address
    memset(&client_addr, 0, sizeof(client_addr));
    client_addr.sin_family = AF_INET;
    client_addr.sin_port = htons(PORT);
    client_addr.sin_addr.s_addr = INADDR_ANY;

    // Bind the socket to the port
    if (bind(client_socket, (struct sockaddr *)&client_addr, sizeof(client_addr)) < 0) {
        perror("Bind failed");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    printf("Broadcast client is listening on port %d...\n", PORT);

    // Listen for broadcast messages
    while (1) {
        memset(buffer, 0, BUFFER_SIZE);
        int bytes_received = recvfrom(client_socket, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_len);
        if (bytes_received < 0) {
            perror("Receive failed");
            break;
        }

        buffer[bytes_received] = '\0'; // Null-terminate the received data
        printf("Received broadcast message: %s\n", buffer);
    }

    close(client_socket);
    return 0;
}



//chat appl tcp

//tcp server

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    char buffer[BUFFER_SIZE];
    socklen_t addr_len = sizeof(client_addr);

    // Create TCP socket
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configure server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Accept connections from any IP
    server_addr.sin_port = htons(PORT);

    // Bind the socket to the address and port
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_socket, 1) < 0) {
        perror("Listen failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Chat server is running on port %d...\n", PORT);

    // Accept a client connection
    if ((client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &addr_len)) < 0) {
        perror("Client accept failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Client connected!\n");

    // Communication loop
    while (1) {
        memset(buffer, 0, BUFFER_SIZE);

        // Receive message from client
        int bytes_received = recv(client_socket, buffer, BUFFER_SIZE, 0);
        if (bytes_received <= 0) {
            printf("Client disconnected.\n");
            break;
        }

        printf("Client: %s", buffer);

        // Echo the message back to the client
        send(client_socket, buffer, bytes_received, 0);
    }

    close(client_socket);
    close(server_socket);
    return 0;
}



//tcp client

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "127.0.0.1" // Replace with the server's IP if running on different machines
#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int client_socket;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];

    // Create TCP socket
    if ((client_socket = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configure server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);

    // Connect to the server
    if (connect(client_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection to server failed");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    printf("Connected to chat server!\n");

    // Communication loop
    while (1) {
        memset(buffer, 0, BUFFER_SIZE);

        // Input message to send
        printf("You: ");
        fgets(buffer, BUFFER_SIZE, stdin);

        // Send the message to the server
        send(client_socket, buffer, strlen(buffer), 0);

        // Exit if the user types "exit"
        if (strncmp(buffer, "exit", 4) == 0) {
            printf("Exiting chat...\n");
            break;
        }

        // Receive the server's response
        int bytes_received = recv(client_socket, buffer, BUFFER_SIZE, 0);
        if (bytes_received <= 0) {
            printf("Server disconnected.\n");
            break;
        }

        printf("Server: %s", buffer);
    }

    close(client_socket);
    return 0;
}



