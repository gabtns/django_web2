from django.db import models


class servicios(models.Model):
    title = models.CharField(max_length=200,verbose_name='titulo')
    subtitle = models.CharField(max_length=200,verbose_name='subtitulo')
    content = models.TextField(max_length=200,verbose_name='contenido')
    precios = models.IntegerField(max_length=200,verbose_name='precio')
    images =  models.ImageField(verbose_name='images',upload_to='servicios',)
    created = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    update = models.DateTimeField(auto_now=True,verbose_name='cambiado')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title 
