# Manga Downloader
Projeto usado para estudo que é capaz de baixar mangás do site Union Mangas através de um CLI .

> **OBS** O site Union Mangas aplicou uma proteção contra DDoS da CloudFire e o projeto não está mais funcionando :cry:

## Bibliotecas utilizadas

- beautifulsoup4
- requests
- click
- tqdm
- jinja2

## Requisitos

- Python 3.5
- Pipenv

## Como instalar


1º Clone o repositório e entre na pasta do projeto
```sh
git clone https://github.com/CleysonPH/manga-downloader.git
cd maga-downloader
```

2º Instale as dependências com o Pipenv
```sh
pipenv install
```

## Como utilizar esse projeto

Inicie o ambiente virtual

```sh
pipenv shell
```

### Baixar um capítulo especifico de um mangá

```sh
python mangadownloader.py --manga 'nome_do_manga' --chapter numero_do_capitulo
```

Exemplo:

Baixar o capítulo 5 de Kimetsu no Yaiba
```sh
python mangadownloader.py --manga 'kimetsu no yaiba' --chapter 5
```

### Baixar todos os capítulos de um mangá

```sh
python mangadownloader.py --manga 'nome_do_manga' --all
```

Exemplo:

Baixar todos os capítulos de One Piece
```sh
python mangadownloader.py --manga 'one piece' --all
```

### Baixar o último capítulo lançando de um mangá

```sh
python mangadownloader.py --manga 'nome_do_manga' --last
```

Exemplo:

Baixar o último capítulo lançado de Solo Leveling
```sh
python mangadownloader.py --manga 'solo leveling' --last
```