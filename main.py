import requests
from lxml import html
import pandas as pd

url = "https://pokemondb.net/pokedex/stats/gen1" # Site escolhido

response = requests.get(url)
response.raise_for_status()

tree = html.fromstring(response.text)

nomes_pokemon = tree.xpath("//table[contains(@class, 'data-table')]/tbody/tr/td[2]/a/text()") # Captura os nomes dos Pokémon 

if nomes_pokemon:
    df = pd.DataFrame({'1a Gen': nomes_pokemon})
    print(df)
    df.to_excel("pokedex_gen1.xlsx", index=False)
    print("Pokédex da primeira geração salva com sucesso!")
else:
    print("Nenhum nome encontrado.")
