#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define MAX_USERS    3
#define MAXBUF       512
int main(int argc, char **argv ) {
	char buf[MAXBUF+1];
	int rc, i, target, next, max, sfd, cfd[MAX_USERS+1], clen[MAX_USERS+1];
	struct sockaddr_in srv, cli[MAX_USERS+1];
	fd_set readfds;
	
	// create a socket
	if( (sfd = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) { 
		perror("Socket creation error"); 
		exit(1);
	}
	
	// server address
	srv.sin_family = AF_INET; 
	srv.sin_addr.s_addr = INADDR_ANY;
	srv.sin_port = htons(atoi(argv[1]));
	
	// bind
	if( bind(sfd, (struct sockaddr*)&srv, sizeof(srv)) <0 ){ 
		perror("Binding error");
		exit(1);
	}
	
	// listen
	if( listen(sfd, MAX_USERS) < 0 ){
		perror("Listening error");
		exit(1);
	}
	
	// init
	max = sfd+1;
	next=0;
	for(i=0;i<MAX_USERS+1;i++) cfd[i]=0;
	
	while(1) {
		FD_ZERO(&readfds);
	
		FD_SET(sfd,&readfds);
		for(i=0;i<next;i++)
			if(cfd[i])
				FD_SET(cfd[i], &readfds);
printf("FD_SET init, max: %d\n", max);	
		select(max,&readfds,0,0,0);
printf("FD_SET select\n");	
	
		if(FD_ISSET(sfd, &readfds)) {
			if(next<MAX_USERS) {
				clen[next] = sizeof(cli[next]);
				cfd[next] = accept(sfd, (struct sockaddr*)&cli[next], &clen[next]);
				if(max <= cfd[next]) max = cfd[next] + 1;
				next++;
printf("add client: %d\n", next);
			} else {
				target = -1;
				for( i=0 ; i<MAX_USERS ; ++i )
					if( !cfd[i] ) {
						target = i;
						break;
					}
				if( target < 0 ) {
					clen[next] = sizeof(cli[next]);
					cfd[next] = accept(sfd, (struct sockaddr*)&cli[next], &clen[next]);
					close(cfd[next]);
					cfd[next] = 0; 
				} else {
					clen[target] = sizeof(cli[target]);
					cfd[target] = accept(sfd, (struct sockaddr*)&cli[target], &clen[target]);
					if(max <= cfd[target]) max = cfd[target] + 1;
				}
			}
		}
		for( i=0 ; i<next ; ++i ) {
			if( FD_ISSET(cfd[i], &readfds) ) {
				rc=read(cfd[i],buf,MAXBUF);
				buf[rc] = '\0';
				buf[MAXBUF] = '\0';
	
				if(rc) {
printf("From %d: %s\n", i, buf );
				} else {
printf("From %d: close\n", i );
					close(cfd[i]);
					cfd[i] = 0;
				}
			}
		}
	}
	for(i=0;i<next;i++)
		if(cfd[i]) {
			close(cfd[i]);
			cfd[i] = 0;
		}
	close(sfd);

	return 0;
}
