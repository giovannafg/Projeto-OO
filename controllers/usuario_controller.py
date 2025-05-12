# controllers/usuario_controller.py
import os
import json
from models.pessoa import Leitor

class UsuarioController:
    def __init__(self):
        self.caminho_arquivo = "data/usuarios.json"
        self.usuarios = []
        self.carregar_usuarios()

    def adicionar_usuario(self, leitor):
        self.usuarios.append(leitor)
        self.salvar_usuarios()

    def salvar_usuarios(self):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump([usuario.to_dict() for usuario in self.usuarios], f, indent=4, ensure_ascii=False)

    def carregar_usuarios(self):
        if os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                lista = json.load(f)
                self.usuarios = [Leitor.from_dict(d) for d in lista]

    def listar_usuarios(self):
        return self.usuarios
