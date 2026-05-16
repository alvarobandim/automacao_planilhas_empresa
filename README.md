# Automação de Back-office - Pipeline ETL e Reporte via E-mail

Sistema de automação desenvolvido em Python para otimizar rotinas de Back-office e Controladoria. O script atua como um agente de integração que realiza a leitura de múltiplas fontes de dados (planilhas de filiais), aplica lógicas de consolidação e despacha um relatório executivo automatizado via protocolo SMTP.

## Arquitetura da Automação

O projeto soluciona o gargalo de consolidação manual de dados corporativos através do seguinte fluxo:

1. Extraction (Extração): Leitura programática de arquivos de dados estruturados em disco (extensões `.xlsx` ou `.csv`).
2. Transformation (Transformação): Uso da engine de manipulação de dados para limpeza, agrupamento e sumarização das métricas das filiais em um único dataset consolidado.
3. Loading & Delivery (Carga e Entrega): Formatação dos dados processados em um corpo de e-mail em HTML e roteamento automatizado para os stakeholders utilizando integração nativa com servidores SMTP.

## Stack Tecnológica

- Linguagem: Python 3
- Data Manipulation: Pandas e Openpyxl (Processamento e I/O de planilhas)
- Networking / Mensageria: `smtplib` e `email.mime` (Protocolos de envio de e-mail seguro com TLS/SSL)

## Instruções de Execução Local

1. Realize o clone do repositório:
```bash
git clone [https://github.com/seu_usuario/nome_do_seu_repositorio.git](https://github.com/seu_usuario/nome_do_seu_repositorio.git)
```

2. Instale a engine de processamento de dados:
```bash
pip install pandas openpyxl
```

3. Configure as credenciais de disparo:
No arquivo de script principal, insira o seu e-mail de remetente e a Senha de Aplicativo gerada pelo provedor (ex: Google App Passwords).

4. Execute o pipeline:
```bash
python automacao_relatorio.py
```