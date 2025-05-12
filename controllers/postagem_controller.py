# controllers/postagem_controller.py
import os
import json
from models.postagem import Postagem

class PostagemController:
    def __init__(self):
        self.caminho_arquivo = "data/postagens.json"
        self.postagens = []
        self.carregar_postagens()

    def adicionar_postagem(self, postagem):
        self.postagens.append(postagem)
        self.salvar_postagens()

    def salvar_postagens(self):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.postagens], f, indent=4, ensure_ascii=False)

    def carregar_postagens(self):
        if os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                lista = json.load(f)
                self.postagens = [Postagem.from_dict(d) for d in lista]

    def listar_postagens(self):
        return self.postagens