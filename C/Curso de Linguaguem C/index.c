#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    float media;
    int total = 0;
    int cont = 0;
    int num = -1;
    bool parar = false;

    while(parar == false)
    {
        printf("Digite o número: ");
        scanf("%d", &num);

        if (num == 0)
        {
            parar = true;
            continue;
        }

        total += num;
        cont++;
    }

    if (cont == 0)
    {
        media = 0;
    }
    else
    {
        media = (float) total / cont;
    }

    printf("A média é %.2f", media);
    return 0;
}
