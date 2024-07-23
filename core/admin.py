from django.contrib import admin
from core.models import Pedido, PedidoItem, Produto

# Register your models here.
admin.site.register(Pedido)
admin.site.register(PedidoItem)
admin.site.register(Produto)