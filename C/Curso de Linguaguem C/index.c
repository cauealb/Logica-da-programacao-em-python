#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int num, pares = 0, impares = 0;

    while(true)
    {
        printf("Digite o número: ");
        scanf("%d", &num);

        if(num == 0)
        {
            break;
        }

        if(num % 2 == 0)
        {
            pares++;
        }
        else
        {
            impares++;
        }

    }

    printf("%d pares\n", pares);
    printf("%d impares\n", impares);
    return 0;
}
