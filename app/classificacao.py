"""Regras de negócio da Classificação PlayOff NBA."""

from typing import Final

PLAYOFFS: Final[str] = "PLAYOFFS"
PLAY_IN: Final[str] = "PLAY_IN"
ELIMINADO: Final[str] = "ELIMINADO"


def _validar_inteiro(nome: str, valor: int) -> None:
    """Valida se um campo é um inteiro real, rejeitando bool."""
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(f"{nome} deve ser um inteiro")


def _validar_nao_negativo(nome: str, valor: int) -> None:
    """Valida valores inteiros não negativos."""
    if valor < 0:
        raise ValueError(f"{nome} não pode ser negativo")


def classificar_equipe(vitorias: int, derrotas: int, seed: int) -> str:
    """Classifica uma equipe segundo as regras definidas no PRD.

    Args:
        vitorias: Número de vitórias da equipe.
        derrotas: Número de derrotas da equipe.
        seed: Posição da equipe na conferência, de 1 a 15.

    Returns:
        PLAYOFFS, PLAY_IN ou ELIMINADO.

    Raises:
        TypeError: Se algum argumento não for um inteiro.
        ValueError: Se algum valor violar as regras de negócio.
    """
    _validar_inteiro("vitorias", vitorias)
    _validar_inteiro("derrotas", derrotas)
    _validar_inteiro("seed", seed)

    _validar_nao_negativo("vitorias", vitorias)
    _validar_nao_negativo("derrotas", derrotas)

    if vitorias + derrotas == 0:
        raise ValueError("a equipe deve ter disputado pelo menos um jogo")

    if seed < 1 or seed > 15:
        raise ValueError("seed deve estar entre 1 e 15")

    if seed <= 6:
        return PLAYOFFS

    if seed <= 10:
        return PLAY_IN

    return ELIMINADO