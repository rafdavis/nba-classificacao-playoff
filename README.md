# NBA Classificação Playoff

Sistema determinístico em Python para classificar uma equipe da NBA em:

- `PLAYOFFS`
- `PLAY_IN`
- `ELIMINADO`

O projeto foi desenvolvido com foco em regras de negócio, testes unitários,
Particionamento de Equivalência, Análise de Valor Limite, Error Guessing e
cobertura de código.

## Requisitos

- Python 3.12+
- `uv`

## Instalação

```bash
uv sync
```

## Executar os testes

```bash
uv run pytest -v
```

## Executar cobertura

```bash
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

O objetivo do projeto é atingir 100% de cobertura de linhas e branches no
módulo de negócio.

## Estrutura

```text
nba-classificacao-playoff/
├── app/
│   ├── __init__.py
│   └── classificacao.py
├── tests/
│   ├── __init__.py
│   └── test_classificacao.py
├── PRD.md
├── AGENTS.md
├── AI_USAGE.md
├── README.md
└── pyproject.toml
```

## Regras resumidas

| Seed | Resultado |
|---:|---|
| 1–6 | PLAYOFFS |
| 7–10 | PLAY_IN |
| 11–15 | ELIMINADO |

Vitórias e derrotas devem ser inteiros não negativos e a equipe precisa ter
pelo menos um jogo disputado.

## Observação acadêmica

A classificação é uma simplificação criada para o projeto. O objetivo não é
reproduzir integralmente todas as regras oficiais da NBA, mas demonstrar a
implementação e o teste de regras de negócio determinísticas.