from django.test import TestCase
from Core_app.tests import TestCaseColor
from .models import Carro
from django.contrib.auth.models import User

class TestCarro(TestCaseColor):
  def test_criacao_do_carro(self):
    proprietario = User.objects.create(
      username="admin",
      password="admin",
      email=""
    )
    carro = Carro.objects.create(
        modelo="Fusca",
        ano=1990,
        placa="ABC-1234",
        marca="Volkswagen",
        cor="Azul",
		proprietario=proprietario,
		preco=10000.00
    )
    self.assert_equal_color(carro.modelo, "Fusca", "Criacao do carro")
    self.assert_equal_color(carro.modelo, "Camaro", "Criacao do carro")
    self.assert_not_equal_color(carro.modelo, "Fusca2", "Criacao do carro")