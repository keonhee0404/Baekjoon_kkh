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
		i++;
		while (j < i)
		{
			printf("*");
			j++;

		}
		j = 0;
		printf("\n");
		

	}


	return 0;

}