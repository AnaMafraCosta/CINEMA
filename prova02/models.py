from django.db import models

# Create your models here.

class Funcao(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Funções"

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=45)
    carteiraTrabalho = models.IntegerField()
    dataContratacao = models.DateField()
    salario = models.FloatField()

    class Meta:
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome

class Horario(models.Model):
    horario= models.TimeField()

    class Meta:
        verbose_name_plural = "Horários"

class Horario_trab_func(models.Model):
    unique_together = (('Horario','Funcionario'))
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name_plural = "Horários de trabalho dos funcionários"

class Premiacao(models.Model):
    nome = models.CharField(max_length=45)
    ano = models.IntegerField()

    class Meta:
        verbose_name_plural = "Premiações"

    def __str__(self):
        return self.nome

class Diretor(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Diretores"

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.nome

class Filme(models.Model):
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, default=None, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=None, null=True)
    nomeBR = models.CharField(max_length=45)
    nomeEN = models.CharField(max_length=45)
    anoLancamento = models.IntegerField()
    sinopse = models.TextField()

    def __str__(self):
        return self.nomeBR

class Filme_has_premiacao(models.Model):
    unique_together = (('Filme','Premiacao'))
    ganhou = models.BooleanField()

    class Meta:
        verbose_name_plural = "Filmes Premiados"

class Sala(models.Model):
    nome = models.CharField(max_length=45)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Filme_exibido_sala(models.Model):
    unique_together = (('Filme','Sala','Horario'))

    class Meta:
        verbose_name_plural = "Sala dos filmes exibidos"