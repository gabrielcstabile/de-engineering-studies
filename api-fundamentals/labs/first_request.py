import requests

url = "https://www.google.com"

# Cria a variável response e atribui a ela o retorno do método get da lib requests 
response = requests.get(url)

# Exibe na tela o status code da nossa request
print(response)

# .text é um atributo — retorna o corpo da resposta já armazenado como string
# print(response.text)

'''
Coloca todo o texto armazenado no response.text no arquivo pagina_google.html
Isso melhora a formatação do retorno e reduz significativamente o nº de caracteres utilizados
Além de permitir a abertura do arquivo em um browser.
'''

with open('pagina_google.html', 'w') as arquivo:
    arquivo.write(response.text)