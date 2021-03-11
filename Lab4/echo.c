#include <stdio.h>

int main(){
	char buf[30];
	while(1){
		fgets(buf, 30, stdin);
		printf(buf);
	}
}
