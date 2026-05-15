# Automação de Consolidação de Planilhas e Disparo SMTP (ETL)

## Descrição
Script desenvolvido em Python para automação de ponta a ponta de rotinas de back-office. O sistema atua como um pipeline de dados que realiza a ingestão de múltiplos relatórios descentralizados, processa as métricas de negócio e, de forma autônoma, despacha o documento consolidado para a diretoria utilizando o protocolo de rede SMTP.

## Arquitetura e Fluxo de Dados
O pipeline foi estruturado nas seguintes etapas:
- **Extract (Extração):** Varredura automatizada do diretório de origem para mapeamento dos arquivos `.xlsx`.
- **Transform (Transformação):** Agregação de dados e cálculo de volumetria utilizando a biblioteca Pandas.
- **Load (Carregamento):** Geração de um novo arquivo executivo padronizado.
- **Delivery (Distribuição):** Montagem de envelope digital (MIME) com anexo binário e disparo autenticado de e-mail via servidor SMTP corporativo.

## Pré-requisitos
- Python 3.x
- Pandas
- OpenPyXL
- Bibliotecas nativas: `os`, `smtplib`, `email.mime`

## Configuração do Ambiente e Segurança
1. Clone o repositório em sua máquina local.
2. Instale as dependências via terminal:
   ```bash
   pip install pandas openpyxl
