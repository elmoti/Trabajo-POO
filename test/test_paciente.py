from datetime import date
from model.pacientes import Paciente
from unittest import TestCase
from helper.helper_datos import *


class TestDireccion(TestCase):
    def setUp(self) -> None:
        self.datos = Datos()
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[0]
        self.paciente = Paciente(
            ci, nombre, edad, sexo, fecha_nacimiento, direccion)

    def test_getters(self):
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[0]
        self.assertEqual(self.paciente.ci, ci)
        self.assertEqual(self.paciente.nombre, nombre)
        self.assertEqual(self.paciente.edad, edad)
        self.assertEqual(self.paciente.sexo, sexo)
        self.assertEqual(self.paciente.fecha_nacimiento, fecha_nacimiento)
        self.assertEqual(self.paciente.direccion, direccion)

    def test_setter_ci(self):
        with self.assertRaises(Exception) as ci:
            self.paciente.ci = "asdasdasd"
        self.assertEqual(str(ci.exception),
                         "El carnet de identidad debe tener 11 caracteres")
        with self.assertRaises(Exception) as ci:
            self.paciente.ci = "asdasdasdas"
        self.assertEqual(str(ci.exception),
                         "El carnet de identidad debe tener solo dígitos")
        with self.assertRaises(Exception) as ci:
            self.paciente.ci = 123123
            self.assertEqual(
                str(ci.exception), "El carnet de identidad solo acepta caracteres de texto")
        self.paciente.ci = "89031534223"
        self.assertEqual(self.paciente.ci, "89031534223")

    def test_setter_nombre(self):
        with self.assertRaises(Exception) as nombre:
            self.paciente.nombre = 1235
        self.assertEqual(
            str(nombre.exception), "Nombre: solo acepta caracteres de texto")
        with self.assertRaises(Exception) as nombre:
            self.paciente.nombre = "er"
        self.assertEqual(
            str(nombre.exception), "Nombre: debe contener al menos 3 caracteres")
        with self.assertRaises(Exception) as nombre:
            self.paciente.nombre = "er"*100
        self.assertEqual(
            str(nombre.exception), "Nombre: debe contener como maximo 100 caracteres")
        self.paciente.nombre = "Angel Napoles"
        self.assertEqual(self.paciente.nombre, "Angel Napoles")

    def test_setter_edad(self):
        with self.assertRaises(Exception) as edad:
            self.paciente.edad = "asdasd"
        self.assertEqual(
            str(edad.exception), "Edad: solo acepta caracteres numericos enteros")
        with self.assertRaises(Exception) as edad:
            self.paciente.edad = -1
        self.assertEqual(
            str(edad.exception), "Edad: debe ser mayor que 0")
        with self.assertRaises(Exception) as edad:
            self.paciente.edad = 151
        self.assertEqual(
            str(edad.exception), "Edad: debe ser menor que 150")
        self.paciente.edad = 33
        self.assertEqual(self.paciente.edad, 33)

    def test_setter_sexo(self):
        with self.assertRaises(Exception) as sexo:
            self.paciente.sexo = 123
        self.assertEqual(str(sexo.exception),
                         "El sexo debe contener solo caracteres de texto")
        with self.assertRaises(Exception) as sexo:
            self.paciente.sexo = "asdads"
        self.assertEqual(str(sexo.exception),
                         str('Solo se acepta que el sexo sea "Masculino" o "Femenino"'))
        with self.assertRaises(Exception) as sexo:
            self.paciente.sexo = "masculino"
        self.assertEqual(str(sexo.exception),
                         str('Solo se acepta que el sexo sea "Masculino" o "Femenino"'))
        with self.assertRaises(Exception) as sexo:
            self.paciente.sexo = "femenino"
        self.assertEqual(str(sexo.exception),
                         str('Solo se acepta que el sexo sea "Masculino" o "Femenino"'))
        self.paciente.sexo = "Masculino"
        self.assertEqual(self.paciente.sexo, "Masculino")

    def test_setter_fecha_nacimiento(self):
        min = date(date.today().year-150, 1, 1)
        max = date.today()
        with self.assertRaises(Exception) as fecha:
            self.paciente.fecha_nacimiento = 123
        self.assertEqual(str(fecha.exception),
                         "Fecha Nacimiento: debe ser una fecha valida")
        with self.assertRaises(Exception) as fecha:
            self.paciente.fecha_nacimiento = "asdasd"
        self.assertEqual(str(fecha.exception),
                         "Fecha Nacimiento: debe ser una fecha valida")
        with self.assertRaises(Exception) as fecha:
            self.paciente.fecha_nacimiento = date(date.today().year-151, 1, 1)
        self.assertEqual(str(fecha.exception),
                         f"Fecha Nacimiento: debe ser mayor que {min}")
        with self.assertRaises(Exception) as fecha:
            self.paciente.fecha_nacimiento = date(
                date.today().year+1, date.today().month, date.today().day)
        self.assertEqual(str(fecha.exception),
                         f"Fecha Nacimiento: debe ser menor que {max}")
        self.paciente.fecha_nacimiento = date(1989, 3, 15)
        self.assertEqual(self.paciente.fecha_nacimiento, date(1989, 3, 15))

    def test_setter_direccion(self):
        with self.assertRaises(Exception) as direccion:
            self.paciente.direccion = 123412341234
        self.assertEqual(
            str(direccion.exception), "Direccion: solo acepta caracteres de texto")
        with self.assertRaises(Exception) as direccion:
            self.paciente.direccion = "asdga"
        self.assertEqual(
            str(direccion.exception), "Direccion: debe contener al menos 10 caracteres")
        with self.assertRaises(Exception) as direccion:
            self.paciente.direccion = "er"*150
        self.assertEqual(
            str(direccion.exception), "Direccion: debe contener como maximo 254 caracteres")
        self.paciente.direccion = "Calle CA#24, Camaguey"
        self.assertEqual(self.paciente.direccion, "Calle CA#24, Camaguey")

    def test_constructor(self):
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[0]
        respuesta = self.datos.pacientes_respuestas[0]
        self.paciente = Paciente(
            ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(self.paciente), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[1]
        respuesta = self.datos.pacientes_respuestas[1]
        self.paciente = Paciente(
            ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(self.paciente), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[2]
        respuesta = self.datos.pacientes_respuestas[2]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[3]
        respuesta = self.datos.pacientes_respuestas[3]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[4]
        respuesta = self.datos.pacientes_respuestas[4]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[5]
        respuesta = self.datos.pacientes_respuestas[5]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[6]
        respuesta = self.datos.pacientes_respuestas[6]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[7]
        respuesta = self.datos.pacientes_respuestas[7]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[8]
        respuesta = self.datos.pacientes_respuestas[8]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[9]
        respuesta = self.datos.pacientes_respuestas[9]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
        ci, nombre, edad, sexo, fecha_nacimiento, direccion = self.datos.pacientes[10]
        respuesta = self.datos.pacientes_respuestas[10]
        with self.assertRaises(Exception) as err:
            self.paciente = Paciente(
                ci, nombre, edad, sexo, fecha_nacimiento, direccion)
        self.assertEqual(str(err.exception), respuesta)
