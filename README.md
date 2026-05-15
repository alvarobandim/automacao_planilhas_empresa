# Automação de Consolidação de Planilhas (ETL)

## Descrição
Script desenvolvido em Python para automação de rotinas de back-office. O sistema realiza a ingestão de múltiplos relatórios descentralizados (formato .xlsx), processa as métricas de negócio e exporta um documento consolidado para análise gerencial.

## Arquitetura e Fluxo de Dados
O pipeline foi estruturado nas seguintes etapas (ETL):
- **Extract (Extração):** Varredura automatizada do diretório `relatorios_filiais` para mapeamento dos arquivos de origem.
- **Transform (Transformação):** Agregação de dados e cálculo de volumetria utilizando a biblioteca Pandas.
- **Load (Carregamento):** Geração do arquivo de saída `relatorio_consolidado.xlsx` na raiz do projeto.

## Pré-requisitos
- Python 3.x
- Pandas
- OpenPyXL

## Configuração do Ambiente
1. Clone o repositório em sua máquina local.
2. No terminal, instale as dependências necessárias executando:
   ```bash
   pip install pandas openpyxl