# models/postagem.py
import uuid
from datetime import datetime

class Postagem:
    def __init__(self, leitor_id, livro_id, comentario, data=None):
        self.id = str(uuid.uuid4())
        self.leitor_id = leitor_id  # ID da Pessoa (Leitor)
        self.livro_id = livro_id    # ID do Livro
        self.comentario = comentario
        self.data = data if data else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "leitor_id": self.leitor_id,
            "livro_id": self.livro_id,
            "comentario": self.comentario,
            "data": self.data
        }

    @staticmethod
    def from_dict(d):
        return Postagem(d["leitor_id"], d["livro_id"], d["comentario"], d["data"])

    def exibir_info(self, leitor_nome, livro_titulo):
        return f"{leitor_nome} leu '{livro_titulo}' e comentou: \"{self.comentario}\" em {self.data}"