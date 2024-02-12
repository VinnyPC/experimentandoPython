import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def homepage():
  return 'Essa é a homepage do site'

@app.route('/vendas')
def totalVendas():
  tabela = pd.read_csv('tv,radio,jornal,vendas.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


app.run(host='0.0.0.0')



##tabela = pd.read_csv('tv,radio,jornal,vendas.csv')
##total_vendas = tabela['Vendas'].sum()
##print(total_vendas)