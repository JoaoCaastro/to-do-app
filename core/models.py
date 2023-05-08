from django.db import models

class To_doModel(models.Model):
    title = models.CharField('Titulo', max_length=50)
    startDate = models.DateField('Inicio')
    endDate = models.DateField('Fim')
    description = models.CharField('Descricao', max_length=1000, null=True)
    modifiedAt = models.DateTimeField(verbose_name='Modificado em', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tarefas'
        verbose_name = 'Tarefa'
        ordering = ('startDate', '-endDate')