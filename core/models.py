from django.db import models

# Create your models here.
class Produto(models.Model):
    sku             = models.CharField(max_length=16, null=False)
    no_descricao    = models.CharField(max_length=255, null=False, blank=False)
    qtd             = models.CharField(max_length=10, null=False, blank=False)
    
    def __str__(self):
        return self.no_descricao


class Pedido(models.Model):
    nr_pedido       = models.CharField(max_length=10)

class PedidoItem(models.Model):
    produto         = models.ForeignKey('Produto', related_name='produto', on_delete=models.CASCADE)
    valor_venda     = models.CharField(max_length=10, null=False, blank=False)