import os
import json
from models.livro import Livro

class LivroController:
    def __init__(self):
        self.caminho_arquivo = "data/livros.json"
        self.livros = []

    def carregar_livros_padrao(self):
        if not os.path.exists(self.caminho_arquivo):
            livros_clarice = [
                {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "caminho_imagem": "imagens/a_hora_da_estrela.jpg"},
                {"titulo": "Perto do Coração Selvagem", "autor": "Clarice Lispector", "caminho_imagem": "imagens/perto_do_coracao.png"},
                {"titulo": "Laços de Família", "autor": "Clarice Lispector", "caminho_imagem": "imagens/lacos_de_familia.jpg"},
                {"titulo": "A Paixão Segundo G.H.", "autor": "Clarice Lispector", "caminho_imagem": "imagens/a_paixao_gh.jpg"},
                {"titulo": "O Lustre", "autor": "Clarice Lispector", "caminho_imagem": "imagens/o_lustre.jpg"},
                {"titulo": "A Cidade Sitiada", "autor": "Clarice Lispector", "caminho_imagem": "imagens/a_cidade_sitiada.jpg"},
                {"titulo": "Um Sopro de Vida", "autor": "Clarice Lispector", "caminho_imagem": "imagens/um_sopro_de_vida.jpg"},
                {"titulo": "Água Viva", "autor": "Clarice Lispector", "caminho_imagem": "imagens/agua_viva.jpg"},
                {"titulo": "Felicidade Clandestina", "autor": "Clarice Lispector", "caminho_imagem": "imagens/felicidade_clandestina.jpg"},
                {"titulo": "A Maça no Escuro", "autor": "Clarice Lispector", "caminho_imagem": "imagens/maca_escuro.jpg"},
                {"titulo": "Uma Aprendizagem", "autor": "Clarice Lispector", "caminho_imagem": "imagens/aprendizagem.jpg"},
                {"titulo": "Alguns Contos", "autor": "Clarice Lispector", "caminho_imagem": "imagens/alguns_contos.jpg"},
                {"titulo": "A Bela e a Fera", "autor": "Clarice Lispector", "caminho_imagem": "imagens/bela_fera.jpg"},
                {"titulo": "A Legião Estrangeira", "autor": "Clarice Lispector", "caminho_imagem": "imagens/legiao_estrangeira.jpg"}
            ]
            self.livros = [Livro(**dados) for dados in livros_clarice]
            self.salvar_livros()
        else:
            self.carregar_livros()

    def salvar_livros(self):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump([livro.to_dict() for livro in self.livros], f, indent=4, ensure_ascii=False)

    def carregar_livros(self):
        with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
            lista = json.load(f)
            self.livros = [Livro.from_dict(dados) for dados in lista]

    def listar_livros(self):
        return self.livros
