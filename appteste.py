import streamlit as st
import pandas as pd
import pygsheets
import os

credenciais = pygsheets.authorize(service_account_file=os.getcwd()+'/cred.json')
planilhamp = 'https://docs.google.com/spreadsheets/d/1f9QdwJYAFs0pljHZLGSyCpw5j2Ig-WjZeqevqI3lMRE/'
status = credenciais.open_by_url(planilhamp)
aba = status.worksheet_by_title('TESTE01')
plmp = aba.get_all_values()
df = pd.DataFrame(plmp)

st.title('Conexão teste')
st.write(df)