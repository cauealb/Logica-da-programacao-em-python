#include <stdio.h>

int main()
{
    int idade = 19;
    char resposta;

    printf("Valor inicial da idade é: %d.\n\n", idade);
    printf("Esse valor está certo (S/N): ");
    scanf("%c", &resposta);

    printf("\n\n");
    if (resposta == 'N')
    {
        printf("Digite a idade correta: ");
        scanf("%d", &idade);

        printf("\n\n");
        printf("Sua idade agora é %d. \n", idade);
    }

    return 0;
}
