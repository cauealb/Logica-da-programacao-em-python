#include <stdio.h>
#include <stdbool.h>

bool ParOuImpar(int n);

int main(void)
{
    int num;

    printf("Digite um número: ");
    scanf("%d", &num);

    if(ParOuImpar(num))
    {
        printf("PAR\n");
        return 0;
    }

    printf("IMPAR\n");
    return 0;
}

bool ParOuImpar(int n)
{
    return n % 2 == 0;
}
