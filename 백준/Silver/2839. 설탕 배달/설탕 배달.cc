#include<stdio.h>

int main(void) {
	int N, count=0, a;
	scanf("%d", &N);

	
	while (1) {
		if (N % 5 == 0) {
			a = N / 5;
			count += a;
			break;
		}
		N -= 3;
		count++;
		
	}

	if (N < 0) {
		printf("%d", -1);
	}
	else {
		printf("%d", count);
	}



	return 0;
}