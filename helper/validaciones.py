from ast import arg, arguments
from datetime import date


def valid_ci(ci: str) -> str:
    if not isinstance(ci, str):
        raise Exception(
            "El carnet de identidad solo acepta caracteres de texto")
    if not len(ci) == 11:
        raise Exception("El carnet de identidad debe tener 11 caracteres")
    try:
        int(ci)
    except:
        raise Exception("El carnet de identidad debe tener solo dígitos")
    return ci


def valid_str(atributo: str, valor: str, min_len: None | int = None, max_len: None | int = None) -> str:
    if not isinstance(valor, str):
        raise Exception(f"{atributo}: solo acepta caracteres de texto")
    if min_len is not None and len(valor) < min_len:
        raise Exception(
            f"{atributo}: debe contener al menos {min_len} caracteres")

    if max_len is not None and len(valor) > max_len:
        raise Exception(
            f"{atributo}: debe contener como maximo {max_len} caracteres")

    return valor


def valid_int(atributo: str, valor: int, min: None | int = None, max: None | int = None) -> int:
    if not isinstance(valor, int):
        raise Exception(
            f"{atributo}: solo acepta caracteres numericos enteros")
    if min is not None and valor < min:
        raise Exception(
            f"{atributo}: debe ser mayor que {min}")
    if max is not None and valor > max:
        raise Exception(
            f"{atributo}: debe ser menor que {max}")
    return valor


def valid_float(atributo: str, valor: float, min: None | float = None, max: None | float = None) -> float:
    if not isinstance(valor, int):
        raise Exception(
            f"{atributo}: solo acepta caracteres numericos float")
    if min is not None and valor < min:
        raise Exception(
            f"{atributo}: debe ser mayor que {min}")
    if max is not None and valor > max:
        raise Exception(
            f"{atributo}: debe ser menor que {max}")
    return valor


def valid_date(atributo: str, valor: date, min: None | date = None, max: None | date = None) -> date:
    if not isinstance(valor, date):
        raise Exception(
            f"{atributo}: debe ser una fecha valida")
    if min is not None and valor < min:
        raise Exception(
            f"{atributo}: debe ser mayor que {min}")
    if max is not None and valor > max:
        raise Exception(
            f"{atributo}: debe ser menor que {max}")
    return valor


def valid_sexo(valor: str) -> str:
    if not isinstance(valor, str):
        raise Exception("El sexo debe contener solo caracteres de texto")
    if not (valor == "Masculino" or valor == "Femenino"):
        raise Exception(
            'Solo se acepta que el sexo sea "Masculino" o "Femenino"')
    return valor
