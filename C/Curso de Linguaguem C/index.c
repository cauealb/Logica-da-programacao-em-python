#include <stdio.h>

int main(void)
{
    int num;
    printf("Digite o número: ");
    scanf("%d", &num);

    int cont = 0;
    for(int i = 1; i <= num; i++)
    {
        cont += i;
    }

    printf("Soma total: %d", cont);
    return 0;
}
