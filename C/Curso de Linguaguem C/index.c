#include <stdio.h>
#include <math.h>

int main(void)
{
    float altura, peso, imc;

    printf("Altura: ");
    scanf("%f", &altura);

    printf("Peso: ");
    scanf("%f", &peso);

    imc = peso / (altura * altura);

    if(imc < 18.5)
    {
        printf("Abaixo do peso.");
    }
    else if(imc < 25)
    {
        printf("Peso ideal.");
    }
    else if(imc < 30)
    {
        printf("Sobrepeso.");
    }
    else if(imc < 40)
    {
        printf("Obesidade.");
    }
    else
    {
        printf("Obesidade mórbida.");
    }

    printf("\n");
    printf("%f", imc);
    return 0;
}
