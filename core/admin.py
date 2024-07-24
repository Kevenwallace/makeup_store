from django.contrib import admin
from django import forms
from core.models import Pedido, PedidoItem, Produto, TabelaPreco

@admin.action(description="criar pedidos")
def criar_pedido(modeladmin, request, queryset):
    pedido_instance = Pedido.objects.create()

    print(pedido_instance)
    instance = PedidoItem()
    
    bulk_creat = []
    for produtos in queryset:
        instance = PedidoItem(
        pedido=pedido_instance,
        produto=produtos)
        bulk_creat += [instance]
    
    print(bulk_creat)
    
    

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("no_descricao", "qtd")
    search_fields = ['no_descricao']  # Campos que serão pesquisáveis
    actions = [criar_pedido]
    def qtd_produtos(self, obj):
        print(obj)

        return obj.qtd
    



# Register your models here

admin.site.register(Pedido,)
admin.site.register(PedidoItem)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(TabelaPreco)