# pokemon-gen1-scraper

Este é o meu primeiro projeto de web scraping, focado na coleta dos **nomes** dos Pokémon da primeira geração (Gen 1) do site [pokemondb.net](https://pokemondb.net/pokedex/stats/gen1). O objetivo principal é extrair esses dados de forma automatizada usando Python e salvá-los em um formato fácil de usar para análises futuras ou a criação de outras ferramentas relacionadas a Pokémon.

## 🚀 Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **requests:** Biblioteca HTTP para fazer requisições web.
* **lxml:** Biblioteca para processamento eficiente de XML e HTML.
* **pandas:** Biblioteca para manipulação e análise de dados, utilizada para criar e exportar o arquivo Excel.

## ✨ Funcionalidades

* Coleta automatizada dos **nomes** de todos os Pokémon da primeira geração.
* Extração de dados diretamente do site [pokemondb.net](https://pokemondb.net/pokedex/stats/gen1).
* Salvamento dos nomes coletados em um arquivo Excel (`pokedex_gen1.xlsx`).

## 🛠️ Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina (versão 3.x recomendada). Você pode baixá-lo em [python.org](https://www.python.org/).

### Instalação

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SeuUsuario/pokemon-gen1-scraper.git](https://github.com/SeuUsuario/pokemon-gen1-scraper.git)
    ```
    (Lembre-se de substituir `SeuUsuario` pelo seu nome de usuário do GitHub)
2.  Navegue até o diretório do projeto:
    ```bash
    cd pokemon-gen1-scraper
    ```
3.  Instale as dependências necessárias:
    ```bash
    pip install requests lxml pandas
    ```

### Execução

Para executar o scraper e coletar os nomes dos Pokémon, utilize o seguinte comando no terminal:
```bash
python main.py
```
Após a execução bem-sucedida, um arquivo chamado pokedex_gen1.xlsx será criado na raiz do projeto, contendo a lista dos nomes dos Pokémon da primeira geração.

🤝 Contribuição
Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para:

Fazer um "fork" do repositório.
Criar uma nova "branch" (git checkout -b feature/NomeDaSuaFeature).
Fazer suas alterações e "commitar" (git commit -m 'Adiciona nova feature').
Fazer um "push" para a "branch" (git push origin feature/NomeDaSuaFeature).
Abrir um "Pull Request".

✨ Agradecimentos
Gostaria de expressar meu agradecimento ao Renan Zanello (https://www.linkedin.com/in/renan-zanollo/) pela inspiração e pela sugestão inicial de utilizar web scraping com XPath e Pandas para criar um "banco de dados" em Excel. A ideia dele foi o catalisador para este projeto!

📞 Contato
João Lucas - https://github.com/Joao-Lucas-Code
https://www.linkedin.com/in/joaogomes6/
joao.lgomes1166@gmail.com
