from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Montadora', max_length=50, help_text='Máximo 50 caracteres')

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


class Carro(models.Model):
    """
    OneToOne (OneToOneField)
    Cada carro só pode se relacionar com um chassi
    Cada chassi só pode se relacionar com um carro
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE) #1:1
    """
    OneToMany (ForeignKey)
    Cada carro tem uma montadora
    Mas uma montadora pode montar vários carros
    """
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE) #1:n
    """
    ManyToMany (ManyToManyField)
    Um carro pode ser dirigido por vários motoristas
    Um motorista pode dirigir diversos carros
    """
    motorista = models.ManyToManyField(get_user_model()) #n:n
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2) #99999999.99

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'
