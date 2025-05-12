import os
from models.postagem import Postagem
from models.pessoa import Leitor

class TerminalView:
    def __init__(self, usuario_ctrl, livro_ctrl, postagem_ctrl):
        self.usuario_ctrl = usuario_ctrl
        self.livro_ctrl = livro_ctrl
        self.postagem_ctrl = postagem_ctrl

    def menu_principal(self):
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Listar usuários")
            print("2. Listar livros")
            print("3. Listar postagens")
            print("4. Cadastrar novo usuário")
            print("5. Criar nova postagem")
            print("6. Editar usuário")
            print("7. Remover usuário")
            print("8. Editar postagem")
            print("9. Remover postagem")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_usuarios()
            elif opcao == "2":
                self.listar_livros()
            elif opcao == "3":
                self.listar_postagens()
            elif opcao == "4":
                self.cadastrar_usuario()
            elif opcao == "5":
                self.criar_postagem()
            elif opcao == "6":
                self.editar_usuario()
            elif opcao == "7":
                self.remover_usuario()
            elif opcao == "8":
                self.editar_postagem()
            elif opcao == "9":
                self.remover_postagem()
            elif opcao == "0":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

    def selecionar_indice(self, lista, titulo):
        while True:
            try:
                for i, item in enumerate(lista):
                    print(f"{i} - {item.exibir_info()}")
                idx = int(input(f"Digite o número do {titulo}: "))
                if 0 <= idx < len(lista):
                    return idx
                else:
                    print("Número fora do intervalo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    def listar_usuarios(self):
        usuarios = self.usuario_ctrl.listar_usuarios()
        print("\n--- USUÁRIOS CADASTRADOS ---")
        for u in usuarios:
            print(u.exibir_info())

    def listar_livros(self):
        livros = self.livro_ctrl.listar_livros()
        print("\n--- LIVROS DISPONÍVEIS ---")
        for l in livros:
            print(l.exibir_info())

    def listar_postagens(self):
        postagens = self.postagem_ctrl.listar_postagens()
        usuarios = {u.id: u.nome for u in self.usuario_ctrl.listar_usuarios()}
        livros = {l.id: l.titulo for l in self.livro_ctrl.listar_livros()}

        print("\n--- POSTAGENS ---")
        for p in postagens:
            nome = usuarios.get(p.leitor_id, "Desconhecido")
            titulo = livros.get(p.livro_id, "Desconhecido")
            print(p.exibir_info(nome, titulo))

    def cadastrar_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        leitor = Leitor(nome, email)
        self.usuario_ctrl.adicionar_usuario(leitor)
        print("Usuário cadastrado com sucesso!")

    def criar_postagem(self):
        usuarios = self.usuario_ctrl.listar_usuarios()
        livros = self.livro_ctrl.listar_livros()

        if not usuarios or not livros:
            print("É necessário ter pelo menos um usuário e um livro cadastrado.")
            return

        print("\nSelecione um usuário:")
        idx_usuario = self.selecionar_indice(usuarios, "usuário")

        print("\nSelecione um livro:")
        idx_livro = self.selecionar_indice(livros, "livro")

        comentario = input("Comentário sobre o livro: ")

        postagem = Postagem(
            leitor_id=usuarios[idx_usuario].id,
            livro_id=livros[idx_livro].id,
            comentario=comentario
        )
        self.postagem_ctrl.adicionar_postagem(postagem)
        print("Postagem criada com sucesso!")

    def editar_usuario(self):
        usuarios = self.usuario_ctrl.listar_usuarios()
        if not usuarios:
            print("Nenhum usuário para editar.")
            return
        idx = self.selecionar_indice(usuarios, "usuário a editar")
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        usuarios[idx].nome = nome
        usuarios[idx].email = email
        self.usuario_ctrl.salvar_usuarios()
        print("Usuário atualizado com sucesso.")

    def remover_usuario(self):
        usuarios = self.usuario_ctrl.listar_usuarios()
        if not usuarios:
            print("Nenhum usuário para remover.")
            return
        idx = self.selecionar_indice(usuarios, "usuário a remover")
        del usuarios[idx]
        self.usuario_ctrl.salvar_usuarios()
        print("Usuário removido com sucesso.")

    def editar_postagem(self):
        postagens = self.postagem_ctrl.listar_postagens()
        if not postagens:
            print("Nenhuma postagem para editar.")
            return

        usuarios = {u.id: u.nome for u in self.usuario_ctrl.listar_usuarios()}
        livros = {l.id: l.titulo for l in self.livro_ctrl.listar_livros()}

        print("\n--- POSTAGENS ---")
        for i, p in enumerate(postagens):
            nome = usuarios.get(p.leitor_id, "Desconhecido")
            titulo = livros.get(p.livro_id, "Desconhecido")
            print(f"{i} - {p.exibir_info(nome, titulo)}")

        try:
            idx = int(input("Digite o número da postagem a editar: "))
            if 0 <= idx < len(postagens):
                novo_comentario = input("Novo comentário: ")
                postagens[idx].comentario = novo_comentario
                self.postagem_ctrl.salvar_postagens()
                print("Postagem atualizada com sucesso.")
            else:
                print("Índice fora do intervalo.")
        except ValueError:
            print("Entrada inválida. Use apenas números.")

    def remover_postagem(self):
        postagens = self.postagem_ctrl.listar_postagens()
        if not postagens:
            print("Nenhuma postagem para remover.")
            return

        usuarios = {u.id: u.nome for u in self.usuario_ctrl.listar_usuarios()}
        livros = {l.id: l.titulo for l in self.livro_ctrl.listar_livros()}

        print("\n--- POSTAGENS ---")
        for i, p in enumerate(postagens):
            nome = usuarios.get(p.leitor_id, "Desconhecido")
            titulo = livros.get(p.livro_id, "Desconhecido")
            print(f"{i} - {p.exibir_info(nome, titulo)}")

        try:
            idx = int(input("Digite o número da postagem a remover: "))
            if 0 <= idx < len(postagens):
                del postagens[idx]
                self.postagem_ctrl.salvar_postagens()
                print("Postagem removida com sucesso.")
            else:
                print("Índice fora do intervalo.")
        except ValueError:
            print("Entrada inválida. Use apenas números.")
