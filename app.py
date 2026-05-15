"""
Script de automação: Pipeline ETL e Disparo de Relatório Executivo.
Objetivo: Realizar a ingestão de múltiplos relatórios descentralizados em Excel,
          calcular a volumetria consolidada e realizar o disparo automatizado
          do relatório final via protocolo SMTP.
"""

import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# --- CONFIGURAÇÕES DE DIRETÓRIO E CREDENCIAIS ---
DIRETORIO_ORIGEM = "relatorios_filiais"
ARQUIVO_SAIDA = "relatorio_consolidado.xlsx"

EMAIL_REMETENTE = "seu_email@gmail.com"
SENHA_APPLICATIVO = "suaasenhaappgerada"
EMAIL_DESTINATARIO = "email_do_chefe@exemplo.com"

# --- ETAPA 1: PIPELINE ETL (PROCESSAMENTO DE DADOS) ---
print("=== INICIANDO PIPELINE DE DADOS (ETL) ===")
total_chamados_empresa = 0

arquivos_filiais = os.listdir(DIRETORIO_ORIGEM)

for arquivo in arquivos_filiais:
    print(f"Ingestão de dados: {arquivo}")
    caminho_arquivo = f"{DIRETORIO_ORIGEM}/{arquivo}"
    
    df_filial = pd.read_excel(caminho_arquivo)
    total_chamados_empresa += df_filial["Chamados_Resolvidos"].sum()

print("--- Processamento dos relatórios concluído ---")

# Geração e salvamento do arquivo consolidado
df_consolidado = pd.DataFrame({"Total_Geral_Empresa": [total_chamados_empresa]})
df_consolidado.to_excel(ARQUIVO_SAIDA, index=False)
print(f"Arquivo '{ARQUIVO_SAIDA}' gerado com sucesso na bancada.")


# --- ETAPA 2: COMUNICAÇÃO AUTOMATIZADA (SMTP) ---
print("\n=== INICIANDO PROCESSO DE DISPARO DE E-MAIL ===")

# Montagem do envelope
envelope = MIMEMultipart()
envelope["From"] = EMAIL_REMETENTE
envelope["To"] = EMAIL_DESTINATARIO
envelope["Subject"] = "Relatório Consolidado de Volumetria - Fechamento"

corpo_email = (
    "Prezados,\n\n"
    "O pipeline de dados processou com sucesso as planilhas das filiais.\n"
    "O relatório executivo consolidado segue anexo a este e-mail.\n\n"
    "Atenciosamente,\n"
    "Automação de Dados"
)
envelope.attach(MIMEText(corpo_email, "plain"))

# Ingestão do anexo binário
print(f"Anexando arquivo: {ARQUIVO_SAIDA}")
with open(ARQUIVO_SAIDA, "rb") as arquivo_fisico:
    anexo = MIMEApplication(arquivo_fisico.read(), Name=ARQUIVO_SAIDA)

anexo["Content-Disposition"] = f'attachment; filename="{ARQUIVO_SAIDA}"'
envelope.attach(anexo)

# Conexão e envio através do servidor
print("Conectando ao servidor SMTP do Google...")
try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, SENHA_APPLICATIVO)
    servidor.send_message(envelope)
    print("SUCESSO: E-mail e relatório entregues ao destinatário!")
except Exception as erro:
    print(f"ERRO CRÍTICO NO DISPARO: {erro}")
finally:
    servidor.quit()
    print("=== PROCESSO FINALIZADO ===")