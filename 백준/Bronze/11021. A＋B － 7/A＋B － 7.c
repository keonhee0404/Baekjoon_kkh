#include <stdio.h>
int main(void)
{
	int a,b,c;
	scanf("%d", &a);
	int i;
	for (i = 0; i < a; i++)
	{
		scanf("%d %d", &b, &c);
		printf("Case #%d: %d\n", i + 1, b + c);
	}
		
		return 0;
}

