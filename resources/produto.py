from flask_restful import Resource, reqparse
from models.produto import ProdutoModel

atributos = reqparse.RequestParser()
atributos.add_argument("nome", type=str, required=True, help="The field 'nome' cannot be left blank.")
atributos.add_argument('valor_venda', type=float, required=True, help="The field 'valor' cannot be left blank.")
atributos.add_argument('quantidade_estoque', type=float, required=True, help="The field 'estoque' cannot be left blank.")
atributos.add_argument('tipo', type=str, required=True, help="The field 'tipo' cannot be left blank.")

class Produto(Resource):

    @staticmethod
    def get():
        produtos = ProdutoModel.query.all()
        produtos_json = [produto.json() for produto in produtos]
        return {'produtos': produtos_json}

    def post(self):
        dados = atributos.parse_args()
        produto = ProdutoModel(dados.nome, dados.valor_venda, dados.quantidade_estoque, dados.tipo)
        produto.insertProduct()
        return {'message': 'Produto cadastrado com sucesso!'}, 201
    
class Produtinho(Resource):
    def get(self, id):
        produtos = ProdutoModel.find_product(id)
        if produtos:
            return {'Produto:': produtos.json()}, 200
        return {'message': 'Produto não encontrado.'}, 404
    
    def delete(self, id):
        produto = ProdutoModel.find_product(id)
        if produto:
            produto.deleteProduct()
            return {'message': 'deletado com sucesso!'}, 200
        return {'message': 'Produto não encontrado.'}, 404
    
    def put(self, id):
        dados = atributos.parse_args()
        produto = ProdutoModel.find_product(id)
        if produto:
            produto.updateProduct(**dados)
            produto.insertProduct()
            return {'message': 'Produto atualizado com sucesso!'}, 200
        return {'message': 'Produto não encontrado.'}, 404
        
        
    

