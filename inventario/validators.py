from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        raise ValidationError("%(valor)s no es un numero par", params={'valor': value})


def validation_categoria(value):
    if value == "No permitido":
        raise ValidationError("No es una opcion permitida")
