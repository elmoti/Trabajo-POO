from typing import *


class SignosVitales:
    def __init__(self, temperatura: float, pulso: int, sanguínea_mínima: float, sanguínea_máxima: float):
        self.__temperatura: float = temperatura
        self.__pulso: int = pulso
        self.__sanguínea_mínima: float = sanguínea_mínima
        self.__sanguínea_máxima: float = sanguínea_máxima

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, value: float) -> None:
        self.__temperatura = value

    @property
    def pulso(self) -> int:
        return self.__pulso

    @pulso.setter
    def pulso(self, value: int) -> None:
        self.__pulso = value

    @property
    def sanguínea_mínima(self) -> float:
        return self.__sanguínea_mínima

    @sanguínea_mínima.setter
    def sanguínea_mínima(self, value: float) -> None:
        self.__sanguínea_mínima = value

    @property
    def sanguínea_máxima(self) -> float:
        return self.__sanguínea_máxima

    @sanguínea_máxima.setter
    def sanguínea_máxima(self, value: float) -> None:
        self.__sanguínea_máxima = value

    def __str__(self):
        sv = "Signos Vitales : {}, {}, {}, {}"
        return sv.format(self.temperatura, self.pulso, self.__sanguínea_mínima, self.__sanguínea_máxima)
