#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int num;

    printf("Número: ");
    scanf("%d", &num);

    if (num <= 0)
    {
        return 0;
    }

    int total = 1;
    for(int i = num; i >= 1; i--)
    {
        if(i == 1)
        {
            printf("%d = ", i);
        }
        else
        {
            printf("%d x ", i);
        }
        total *= i;
    }

    printf("%d\n", total);
    return 0;
}
