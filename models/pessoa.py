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
   pass
# herda tudo de Pessoa (incluindo to_dict() e from_dict()), sem precisar reescrever nada.