# AI_USAGE.md — Relatório de Transparência sobre Uso de IA

Este arquivo registra como a IA foi utilizada na ATV1 de Qualidade e Teste de
Software (QTS), para que quem avalia o projeto consiga identificar as
contribuições da ferramenta, as decisões tomadas e as verificações realizadas.

## 1. Ferramenta utilizada

| Item | Informação |
|---|---|
| Ferramenta | ChatGPT (OpenAI) |
| Forma de uso | Utilizado como assistente de programação, redação técnica e revisão |

## 2. Como a IA foi empregada

| Atividade | Uso da IA |
|---|---|
| Definição do domínio | Sugestão do problema (classificação de equipes da NBA por seed) e simplificação das regras |
| Especificação | Apoio na estruturação do `PRD.md` (regras RN01–RN08, EP, BVA, Error Guessing e critérios de aceitação) |
| Regras de contexto | Apoio na redação do `AGENTS.md` |
| Documentação | Apoio na redação do `README.md` |

## 3. Como foi feita a auditoria

A validação seguiu estes passos:

1. **Rastreabilidade**: cada regra RN01–RN08 do `PRD.md` foi comparada com a
   implementação e com pelo menos um teste.
2. **Execução da suíte**: `uv run pytest -v` (todos os testes devem passar).
3. **Cobertura**: `uv run pytest --cov=app --cov-branch --cov-report=term-missing`.
4. **Revisão dos testes**: conferência de que cada caso tem justificativa em
   uma técnica (EP, BVA ou Error Guessing) e de que as asserções verificam o
   valor esperado exato, e não apenas "algum resultado válido".

## 4. Resultado verificado

| Métrica | Resultado |
|---|---|
| Testes | 50 passando, 0 falhando |
| Cobertura de linhas (`app`) | 100% |
| Cobertura de branches (`--cov-branch`) | 100% (12 de 12) |
| Python | 3.12 |
| Gerenciador | `uv` (`pyproject.toml` e `uv.lock`) |
