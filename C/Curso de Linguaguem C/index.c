#include <stdio.h>

int main(void)
{
    float nota1, nota2, nota3, media, soma;

    printf("Nota 1: ");
    scanf("%f", &nota1);

    printf("Nota 2: ");
    scanf("%f", &nota2);

    printf("Nota 3: ");
    scanf("%f", &nota3);

    soma = nota1 + nota2 + nota3;
    media = soma / 3;
    printf("Media: %.2f\n", media);

    return 0;
}
