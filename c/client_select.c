#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define MAX_BUF 1024
int main(int argc, char* argv[])
{
	int sockd,cli,state,cli_len,words;
	struct sockaddr_in serv_name;
	char buf[MAX_BUF],dis[MAX_BUF];
	fd_set readfds;
	FILE* fp;
	if (argc < 3){
		printf("Usage> %s ip_address port_number\n", argv[0]);
		exit(1);
	}

	/* create a socket */
	if ( (sockd = socket(AF_INET, SOCK_STREAM, 0)) < 0 ){
		perror("Socket creation");
		exit(1);
	}

	/* server address */ 
	serv_name.sin_family = AF_INET;
	inet_aton(argv[1], &serv_name.sin_addr);
	serv_name.sin_port = htons(atoi(argv[2]));

	/* connect to the server */
	if( state = connect(sockd, (struct sockaddr*)&serv_name, sizeof(serv_name) )<0 ){
 		perror("Connection error");
		exit(1);
	}

	FD_ZERO(&readfds);

	while(1){
		FD_ZERO(&readfds);
		FD_SET(0,&readfds);
		FD_SET(sockd, &readfds);

		select(sockd+1,&readfds,0,0,0);

		// read from stdin
		if(FD_ISSET(0, &readfds)){
			words=read(0,buf,MAX_BUF);
			buf[words-1]='\0';
			write(sockd,buf,strlen(buf));
		}

		// server response
		if(FD_ISSET(sockd, &readfds)){
			words=read(sockd,buf,MAX_BUF);

			// connection closed
			if(words==0) {
				printf("Connection break!!\n");
				break;
			}
			buf[words]='\0';
			write(0,buf,strlen(buf));
		}
	}
	close(sockd);
	return 0;
}
