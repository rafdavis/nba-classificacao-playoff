"""Testes unitários das regras de classificação."""

import pytest

from app.classificacao import ELIMINADO, PLAY_IN, PLAYOFFS, classificar_equipe


@pytest.mark.unit
@pytest.mark.parametrize(
    ("seed", "esperado"),
    [
        (1, PLAYOFFS),
        (2, PLAYOFFS),
        (5, PLAYOFFS),
        (6, PLAYOFFS),
        (7, PLAY_IN),
        (8, PLAY_IN),
        (10, PLAY_IN),
        (11, ELIMINADO),
        (12, ELIMINADO),
        (14, ELIMINADO),
        (15, ELIMINADO),
    ],
)
def test_classificacao_por_particao_de_equivalencia(seed: int, esperado: str) -> None:
    vitorias = 50
    derrotas = 32

    resultado = classificar_equipe(vitorias, derrotas, seed)

    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    ("seed", "esperado"),
    [
        (1, PLAYOFFS),
        (6, PLAYOFFS),
        (7, PLAY_IN),
        (10, PLAY_IN),
        (11, ELIMINADO),
        (15, ELIMINADO),
    ],
)
def test_valores_limite_da_seed(seed: int, esperado: str) -> None:
    vitorias = 1
    derrotas = 0

    resultado = classificar_equipe(vitorias, derrotas, seed)

    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize("seed", [0, -1, 16, 100])
def test_seed_invalida_e_rejeitada(seed: int) -> None:
    vitorias = 1
    derrotas = 0

    with pytest.raises(ValueError, match="seed deve estar entre 1 e 15"):
        classificar_equipe(vitorias, derrotas, seed)


@pytest.mark.unit
@pytest.mark.parametrize("vitorias", [-1, -10])
def test_vitorias_negativas_sao_rejeitadas(vitorias: int) -> None:
    derrotas = 10
    seed = 5

    with pytest.raises(ValueError, match="vitorias não pode ser negativo"):
        classificar_equipe(vitorias, derrotas, seed)


@pytest.mark.unit
@pytest.mark.parametrize("derrotas", [-1, -10])
def test_derrotas_negativas_sao_rejeitadas(derrotas: int) -> None:
    vitorias = 10
    seed = 5

    with pytest.raises(ValueError, match="derrotas não pode ser negativo"):
        classificar_equipe(vitorias, derrotas, seed)


@pytest.mark.unit
def test_equipe_sem_jogos_e_rejeitada() -> None:
    vitorias, derrotas, seed = 0, 0, 5

    with pytest.raises(ValueError, match="pelo menos um jogo"):
        classificar_equipe(vitorias, derrotas, seed)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("vitorias", "derrotas", "seed", "esperado"),
    [
        (0, 1, 1, PLAYOFFS),
        (1, 0, 6, PLAYOFFS),
        (0, 1, 7, PLAY_IN),
        (1, 0, 10, PLAY_IN),
        (0, 1, 11, ELIMINADO),
        (1, 0, 15, ELIMINADO),
        (1, 1, 5, PLAYOFFS),
    ],
)
def test_zero_e_valido_para_vitorias_ou_derrotas(
    vitorias: int, derrotas: int, seed: int, esperado: str
) -> None:

    resultado = classificar_equipe(vitorias, derrotas, seed)

    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    ("campo", "vitorias", "derrotas", "seed"),
    [
        ("vitorias", "50", 32, 1),
        ("derrotas", 32, "32", 1),
        ("seed", 50, 32, "1"),
        ("vitorias", 50.0, 32, 1),
        ("derrotas", 50, 32.0, 1),
        ("seed", 50, 32, 1.0),
        ("vitorias", True, 32, 1),
        ("derrotas", 50, False, 1),
        ("seed", 50, 32, True),
        ("vitorias", None, 32, 1),
        ("derrotas", 50, None, 1),
        ("seed", 50, 32, None),
    ],
)
def test_tipos_invalidos_sao_rejeitados(
    campo: str, vitorias: int, derrotas: int, seed: int
) -> None:
    mensagem_esperada = f"{campo} deve ser um inteiro"

    with pytest.raises(TypeError, match=mensagem_esperada):
        classificar_equipe(vitorias, derrotas, seed)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("vitorias", "derrotas", "seed", "excecao", "mensagem"),
    [
        ("x", -1, 0, TypeError, "vitorias deve ser um inteiro"),
        (-1, -1, 0, ValueError, "vitorias não pode ser negativo"),
        (1, -1, 0, ValueError, "derrotas não pode ser negativo"),
        (0, 0, 0, ValueError, "pelo menos um jogo"),
        (1, 0, 0, ValueError, "seed deve estar entre 1 e 15"),
    ],
)
def test_ordem_de_validacao_com_varias_entradas_invalidas(
    vitorias: int, derrotas: int, seed: int, excecao: type[Exception], mensagem: str
) -> None:

    with pytest.raises(excecao, match=mensagem):
        classificar_equipe(vitorias, derrotas, seed)