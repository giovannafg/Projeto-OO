import uuid

class Pessoa:
    def __init__(self, nome, email):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }

    @staticmethod
    def from_dict(d):
        pessoa = Pessoa(d["nome"], d["email"])
        pessoa.id = d["id"]
        return pessoa

    def exibir_info(self):
        return f"Nome: {self.nome} | Email: {self.email}"

class Leitor(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.postagens = []  # agregação com Postagem

    def to_dict(self):
        data = super().to_dict()
        data["postagens"] = self.postagens
        return data

    @staticmethod
    def from_dict(d):
        leitor = Leitor(d["nome"], d["email"])
        leitor.id = d["id"]
        leitor.postagens = d.get("postagens", [])
        return leitor
