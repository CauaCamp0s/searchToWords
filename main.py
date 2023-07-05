import requests
from bs4 import BeautifulSoup


def pesquisaSite_palavrasChaves(lista_palavraChave, url_list):
    for url in url_list:
        print(f"Procurando palavras em {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
            soup = BeautifulSoup(response.text, "html.parser")

            # Procurar palavras-chave na página
            for keyword in lista_palavraChave:
                if keyword.lower() in soup.get_text().lower():
                    print(f"Palavra encontrada: {keyword}")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


# Lista de palavras-chave que serão procuradas
pesquisa_palavrasChaves = ["palavra", "palavra", "palavra"]

# Lista de URLs que você deseja pesquisar
pesquisa_urls = [
    "https://www.globo.com.br",
    "https://exemplo.com.br",
]

# Chamar a função para pesquisar as palavras-chave nos sites
pesquisaSite_palavrasChaves(
    pesquisa_palavrasChaves, 
    pesquisa_urls
)

