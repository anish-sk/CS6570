#include <stdio.h>

int main(){
	char buf[256];
	while(1){
		fgets(buf, 256, stdin);
		printf(buf);
	}
}
