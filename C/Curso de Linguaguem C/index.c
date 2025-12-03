#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    float media;
    int num, maior, menor;
    int cont = 1;
    bool parar = false;

    while(parar == false)
    {
        printf("Digite o número %d: ", cont);
        scanf("%d", &num);

        if(num == 0)
        {
            parar = true;
            continue;
        }

        if(cont == 1)
        {
            menor = num;
            maior = num;
        }

        if(num < menor)
        {
            menor = num;
        }

        if (num > maior)
        {
            maior = num;
        }

        cont++;
    }

    printf("O maior será o %d e o menor será %d.\n", maior, menor);
    return 0;
}
