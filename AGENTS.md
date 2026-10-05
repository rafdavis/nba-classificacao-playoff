# AGENTS.md — Regras de contexto do projeto

## Regras obrigatórias

- Utilizar Python 3.12 ou superior.
- Utilizar Type Hints.
- Manter a lógica de negócio determinística.
- Não utilizar APIs, banco de dados ou serviços externos.
- Não alterar regras de negócio sem atualizar o `PRD.md`.
- Evitar efeitos colaterais na camada de domínio.
- Manter as funções pequenas e legíveis.

## Testes

- Utilizar Pytest.
- Utilizar `@pytest.mark.unit`.
- Utilizar `@pytest.mark.parametrize` quando houver cenários semelhantes.
- Seguir o padrão AAA: Arrange, Act, Assert.
- Cobrir Particionamento de Equivalência (EP).
- Cobrir Análise de Valor Limite (BVA).
- Cobrir Error Guessing.
- Testar caminhos verdadeiros e falsos das condições.
- O objetivo é 100% de cobertura de linhas e branches no pacote `app`.

## Documentação

Toda alteração relevante nas regras deve ser refletida em:

1. `PRD.md`;
2. testes;
3. implementação;
4. quando aplicável, `README.md`.

## Qualidade

Não criar testes artificiais apenas para aumentar a cobertura.
Cada cenário deve possuir uma justificativa relacionada a uma regra ou técnica
de teste.
