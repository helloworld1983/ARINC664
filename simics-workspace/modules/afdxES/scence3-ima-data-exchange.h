#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <winsock2.h>

extern SOCKET ima_client_socket;
extern SOCKET ima_server_socket;

extern int ima_server_socket_init(int serverPortNum, int clientPortNum);
extern int ima_client_socket_init(int clientPortNum, int serverPortNum);
extern int ima_socket_recv(unsigned char *recvbuf, int size, void *socketfd, int addr_type);
extern int ima_socket_send(unsigned char *sendbuf, int size, void *socketfd, int addr_type);
extern void *get_ima_client_socket(void);
extern void *get_ima_server_socket(void);
