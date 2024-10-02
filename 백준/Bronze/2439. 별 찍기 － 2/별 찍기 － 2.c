#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int i, j, r;
	i = 0;
	j = 0;
	

	scanf("%d", &r);
	while (i < r)
	{
		while (j < r-i-1)
		{
			printf(" ");
			j++;
		}
		j = 0;
		while (j <=i)
		{
			printf("*");
			j++;
			
		}
	
		j = 0;
		printf("\n");
		
		i++;
	}


	return 0;

}