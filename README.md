# Projeto Dundie Rewards

[![CI](https://github.com/HenriqueCCdA/dundie-rewards/actions/workflows/main.yml/badge.svg)](https://github.com/HenriqueCCdA/dundie-rewards/actions/workflows/main.yml)

Nós fomos contratados pela Dunder Mifflin, grande fabricante de papéis para desenvolver um sistema de recomprensas para seus colaboradores.

Michael, o gerente da empresa quer aumentar a motivação dos funcionários oferecendo um sistema de pontos que os funcionários podem acumular de acordo com as suas metas atigindas, bonus oferecidos pelo gerente e os funcionários podem também troar pontos ente si.

O funcionário pode um vez a cada ano resgatar seus pontos em um cartão de cŕedito para gastar onde quiserem.

Acordamos em contrato que o MVP (Minimu Viabel Product) será uma versão para ser executada no terminal e que no futuro teá também as interfaces UI, web e API.

Os dados dos funcionários atuais serão fornecidos em um arquivo que pode ser no formato .csv ou json e este mesmo arqvuio poderá ser usado para versões futuras. `Nome, Depto, Cargo, Email`

---
## Installation

```
pip install seu_nome
```

```py
pip install -e `.[dev]`
```

# Usage

```
dundie load assets/people.csv
```
