# PRD — Sistema de Classificação para Playoffs da NBA

## 1. Visão geral

O **NBA Classificação Playoff** é uma aplicação Python determinística que recebe os
dados de uma equipe e determina sua situação na classificação da conferência,
considerando uma seed de 1 a 15.

O projeto é acadêmico e utiliza uma versão simplificada das regras de
classificação da NBA. Não há integração com APIs, bancos de dados ou serviços
externos.

## 2. Objetivo

Permitir que uma equipe seja classificada em uma das seguintes situações:

- `PLAYOFFS`: seeds de 1 a 6;
- `PLAY_IN`: seeds de 7 a 10;
- `ELIMINADO`: seeds de 11 a 15.

Antes da classificação, os dados recebidos são validados.

## 3. Entrada

A função principal recebe:

| Campo | Tipo | Regra |
|---|---|---|
| `wins` | `int` | Deve ser inteiro e não negativo |
| `losses` | `int` | Deve ser inteiro e não negativo |
| `seed` | `int` | Deve ser inteiro entre 1 e 15 |

## 4. Regras de negócio

### RN01 — Tipos de dados

`wins`, `losses` e `seed` devem ser valores inteiros.

Valores booleanos não são aceitos, apesar de `bool` ser uma subclasse de `int`
em Python.

Entrada inválida gera `TypeError`.

### RN02 — Vitórias

O número de vitórias deve ser maior ou igual a zero.

Valor negativo gera `ValueError`.

### RN03 — Derrotas

O número de derrotas deve ser maior ou igual a zero.

Valor negativo gera `ValueError`.

### RN04 — Temporada com jogos

A soma de vitórias e derrotas deve ser maior que zero.

Uma equipe sem jogos disputados gera `ValueError`.

### RN05 — Seed

A seed deve estar entre 1 e 15, inclusive.

- `seed < 1` → `ValueError`;
- `1 <= seed <= 15` → válida;
- `seed > 15` → `ValueError`.

### RN06 — Classificação para Playoffs

Se `seed` estiver entre 1 e 6, o resultado será `PLAYOFFS`.

### RN07 — Classificação para Play-In

Se `seed` estiver entre 7 e 10, o resultado será `PLAY_IN`.

### RN08 — Eliminação

Se `seed` estiver entre 11 e 15, o resultado será `ELIMINADO`.

## 5. Saída

A função retorna uma string contendo uma das categorias:

```text
PLAYOFFS
PLAY_IN
ELIMINADO
```

## 6. Particionamento de Equivalência

### Seed

- Partição inválida inferior: `seed < 1`
- Partição Playoffs: `1 <= seed <= 6`
- Partição Play-In: `7 <= seed <= 10`
- Partição Eliminado: `11 <= seed <= 15`
- Partição inválida superior: `seed > 15`

### Vitórias

- inválida: `wins < 0`
- válida: `wins >= 0`

### Derrotas

- inválida: `losses < 0`
- válida: `losses >= 0`

### Jogos disputados

- inválida: `wins + losses == 0`
- válida: `wins + losses > 0`

## 7. Análise de Valor Limite

Os principais limites testados serão:

| Regra | Abaixo | Limite | Acima |
|---|---:|---:|---:|
| Vitórias | -1 | 0 | 1 |
| Derrotas | -1 | 0 | 1 |
| Seed mínima | 0 | 1 | 2 |
| Playoffs/Play-In | 6 | 7 | 8 |
| Play-In/Eliminação | 10 | 11 | 12 |
| Seed máxima | 15 | 16 | — |

Também serão testados valores representativos nos extremos das classes.

## 8. Error Guessing

Serão considerados cenários de erro que podem ocorrer em entradas reais:

- `None`;
- strings em vez de inteiros;
- `float` em vez de inteiro;
- `bool`;
- números negativos;
- equipe com 0 vitórias e 0 derrotas;
- seed 0;
- seed 16.

## 9. Critérios de aceitação

O projeto será considerado aprovado quando:

1. Todas as regras RN01–RN08 estiverem implementadas.
2. Os testes unitários estiverem escritos com Pytest.
3. Os testes utilizarem padrão AAA.
4. Houver testes parametrizados.
5. Houver cobertura de EP, BVA e Error Guessing.
6. Todos os testes passarem.
7. A cobertura de linhas e branches do módulo `app` atingir 100%.
8. O projeto puder ser executado utilizando `uv`.
