from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    sku             = models.CharField(max_length=16, null=False)
    no_descricao    = models.CharField(max_length=255, null=False, blank=False)
    qtd             = models.CharField(max_length=10, null=False, blank=False)
    
    def __str__(self):
        return self.no_descricao

class TabelaPreco(models.Model):
    produto         = models.ForeignKey(Produto, related_name="precos", on_delete=models.CASCADE)
    valor_produto   = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    data_inicio     = models.DateField(null=False, blank=False)
    data_fim        = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.produto.no_descricao} - {self.valor_produto}$"

class Pedido(models.Model):
    nr_pedido       = models.BigAutoField(primary_key=True)

class PedidoItem(models.Model):
    pedido          = models.ForeignKey(Pedido,related_name="pedidos", on_delete=models.CASCADE)
    produto         = models.ForeignKey(Produto,related_name="produtos", on_delete=models.CASCADE)
    
    def __str__(self):
        preco_atual = self.produto.precos.order_by('-data_inicio').first()
        return f"{preco_atual}"
    