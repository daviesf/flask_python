import fdb
import json
from decimal import Decimal
from sql_alchemy import banco

class ProdutoModel(banco.Model):
    __tablename__ = 'PRODUTO'
    
    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    valor_venda = banco.Column(banco.Float(precision=2))
    quantidade_estoque = banco.Column(banco.Float(precision=2))
    tipo = banco.Column(banco.String(1))
    
    def __init__(self, nome, valor_venda, quantidade_estoque, tipo):
        self.nome = nome
        self.valor_venda = float(valor_venda)
        self.quantidade_estoque = float(quantidade_estoque)
        self.tipo = tipo
    
    def insertProduct(self):
        banco.session.add(self)
        banco.session.commit()
        
    @staticmethod    
    def searchProduct():
        pass
    
    @staticmethod
    def searchProductById(id):
        product = cls.find_product(id)
        if product:
            return product
        return None
    
    def deleteProduct(self):
        banco.session.delete(self)
        banco.session.commit()
        
    def updateProduct(self, nome, valor_venda, quantidade_estoque, tipo):
        self.nome = nome
        self.valor_venda = valor_venda
        self.quantidade_estoque = quantidade_estoque
        self.tipo = tipo
    
    @classmethod    
    def find_product(cls, id):
        produto = cls.query.filter_by(id=id).first() # SELECT * FROM hoteis WHERE hotel_id = hotel_id LIMIT 1
        if produto:
            return produto
        return None
        
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'valor_venda': self.valor_venda,
            'quantidade_estoque': self.quantidade_estoque,
            'tipo': self.tipo
        }
        
    @classmethod
    def from_tuple(cls, produto_tuple):
        return cls(*produto_tuple)
    
        