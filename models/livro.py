import uuid

class Livro:
    def __init__(self, titulo, autor, caminho_imagem):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.autor = autor
        self.caminho_imagem = caminho_imagem

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "caminho_imagem": self.caminho_imagem
        }

    @staticmethod
    def from_dict(d):
        livro = Livro(d["titulo"], d["autor"], d["caminho_imagem"])
        livro.id = d["id"]
        return livro

    def exibir_info(self):
        return f"{self.titulo} - {self.autor}"