#include <stdio.h>
const int ECONOMICA = 1;
const int EXECUTIVA = 2;
const int CHEGOU_NO_LIMITE = 0;
const int SUCESSO = 1;
const int SAIR = 0;
const char ADICIONA_ECONOMICA = 'a';
const char ADICIONA_EXECUTIVA = 'b';
const char FALHA = 'c';

void MostraMenu(double valorTotal) {
  printf("Informe o tipo de passageiro (1 - Economica || 2 - Executiva):\n");

  if (valorTotal > 80)
    printf("Atencao! Valor total da viagem chegou a 80 reais, se deseja sair do sistema informa a opcao 0");
}

int validaQtdClientes(int qtdClientesEconomica, int qtdClientesExecutiva, int desejaAdicionarQual) {

  if (qtdClientesEconomica == 6 && desejaAdicionarQual == ECONOMICA) {
    return CHEGOU_NO_LIMITE;
  }

  if (qtdClientesExecutiva == 4 && desejaAdicionarQual == EXECUTIVA) {
    return CHEGOU_NO_LIMITE;
  }

  return SUCESSO;
}

char CadastroCliente(int qtdClientesEconomica, int qtdClientesExecutiva, double valorTotal) {
  int tipoCliente;

  MostraMenu(valorTotal);
  scanf("%d", &tipoCliente);

  switch (tipoCliente) {
    case SAIR: {
      return SAIR;
    }

    case ECONOMICA: {
      if (validaQtdClientes(qtdClientesEconomica, qtdClientesExecutiva, ECONOMICA) == CHEGOU_NO_LIMITE) {
        printf("Atencao! Economica chegou no limite!\n");
        break;
      }
      return ADICIONA_ECONOMICA;
    }

    case EXECUTIVA: {
      if (validaQtdClientes(qtdClientesEconomica, qtdClientesExecutiva, EXECUTIVA) == CHEGOU_NO_LIMITE) {
        printf("Atencao! Executiva chegou no limite!\n");
        break;
      }

      return ADICIONA_EXECUTIVA;
    }
  }

  return FALHA;
}

void MostraDadosFinais(int qtdClientesEconomica, int qtdClientesExecutiva, double valorTotal) {
  printf("Quantidade de clientes em econômica: %d\n", qtdClientesEconomica);
  printf("Quantidade clientes em executiva: %d\n", qtdClientesExecutiva);
  printf("Quantidade total de clientes: %d\n", qtdClientesEconomica + qtdClientesExecutiva);
  printf("Valor total da viagem: %.2f\n", valorTotal);
}

int main(void) {
  int qtdClientesEconomica = 0;
  int qtdClientesExecutiva = 0;
  int sairDoSistema = 0;
  double valorTotal = 0;

  do {
    switch (CadastroCliente(qtdClientesEconomica, qtdClientesExecutiva, valorTotal)) {
      case ADICIONA_ECONOMICA:{ 
        qtdClientesEconomica++;
        valorTotal += 10;
      } break;

      case ADICIONA_EXECUTIVA:{
         qtdClientesExecutiva++; 
         valorTotal += 20;
      } break;

      case SAIR: sairDoSistema++; break;

      default: break;
    }

    if (qtdClientesEconomica + qtdClientesExecutiva == 10)
      printf("Quantidade de clientes chegou no limite!\n");

  } while (qtdClientesEconomica + qtdClientesExecutiva < 10 || sairDoSistema > 0);

  MostraDadosFinais(qtdClientesEconomica, qtdClientesExecutiva, valorTotal);
  return 0;
}