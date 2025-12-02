#include <stdio.h>
#include <math.h>

int main(void)
{
    int num = 0;
    double raiz;

    printf("Digite um número: ");
    scanf("%d", &num);

    raiz = sqrt(num);

    printf("Dobro: %d.\n", num * 2);
    printf("Triplo: %d.\n", num * 3);
    printf("Raiz quadrada: %lf.\n", raiz);

    return 0;
}
