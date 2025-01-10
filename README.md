# 🔍 Pesquisa de Palavras-Chave em Sites

Este projeto é um script em Python que permite buscar palavras-chave específicas em uma lista de URLs. Ele utiliza as bibliotecas **requests** e **BeautifulSoup** para acessar as páginas da web e analisar seu conteúdo.

---

## 🚀 Funcionalidades

- **Busca de palavras-chave**: Verifica se as palavras especificadas aparecem no conteúdo textual das páginas.
- **Análise de múltiplos sites**: Suporte para uma lista de URLs a serem pesquisadas.
- **Mensagens informativas**: Exibe o status da pesquisa para cada URL, bem como palavras-chave encontradas.
- **Tratamento de erros**: Garante que erros de conexão ou solicitações inválidas sejam tratados adequadamente.

---

## 📋 Pré-requisitos

Antes de executar o código, certifique-se de que você tenha o seguinte instalado:

- Python 3.6 ou superior.
- As bibliotecas **requests** e **BeautifulSoup4**. Para instalá-las, use o comando:

   ```bash
   pip install requests beautifulsoup4
## 🛠️ Como Usar
Clone o repositório ou copie o script para o seu ambiente local.

Personalize as listas de palavras-chave e URLs:

No código, edite as variáveis pesquisa_palavrasChaves e pesquisa_urls para incluir as palavras e os sites desejados.
python
Copiar código
pesquisa_palavrasChaves = ["exemplo1", "exemplo2"]
pesquisa_urls = ["https://site1.com", "https://site2.com"]
Execute o script: Execute o script no terminal ou no seu IDE preferido:

bash
Copiar código
python nome_do_arquivo.py
## 🖥️ Estrutura do Código
Função pesquisaSite_palavrasChaves:

Recebe uma lista de palavras-chave e uma lista de URLs.
Acessa cada URL, verifica a presença das palavras-chave no conteúdo textual e imprime os resultados.
Tratamento de Exceções:

Lida com problemas de conexão e outros erros inesperados durante a execução.
## 🌟 Exemplo de Saída
plaintext
Copiar código
Procurando palavras em https://www.globo.com.br...
Palavra encontrada: exemplo1
Palavra encontrada: exemplo2
Procurando palavras em https://site2.com...
Erro ao acessar https://site2.com: 404 Client Error: Not Found for url: https://site2.com
## 💡 Melhorias Futuras
Suporte para salvar os resultados em um arquivo CSV ou JSON.
Adicionar suporte a cabeçalhos personalizados para evitar bloqueios de bots.
Implementar uma interface gráfica para facilitar o uso.
Permitir buscas em idiomas específicos.
## 📄 Licença
Este projeto é livre para uso e modificação. Contribuições são bem-vindas!

Salve este conteúdo como `README.md` no repositório do script.
