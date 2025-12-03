#include <stdio.h>
#include <stdbool.h>

void ValidarMaior(int num, int *maior);

int main(void)
{
    int num = -1, maior = 0;

    while(num != 0)
    {
        printf("Número: ");
        scanf("%d", &num);

        ValidarMaior(num, &maior);
    }

    printf("O maior é: %d\n", maior);
}

void ValidarMaior(int num, int *maior)
{
    if(num > *maior)
    {
        *maior = num;
    }
}
