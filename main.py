# Estrutura MVC - Sistema de Postagem de Livros
# main.py

from controllers.usuario_controller import UsuarioController
from controllers.livro_controller import LivroController
from controllers.postagem_controller import PostagemController
from views.terminal_view import TerminalView

def main():
    usuario_ctrl = UsuarioController()
    livro_ctrl = LivroController()
    livro_ctrl.carregar_livros_padrao() 
    ##add essa de cima
    postagem_ctrl = PostagemController()
    view = TerminalView(usuario_ctrl, livro_ctrl, postagem_ctrl)
    view.menu_principal()

if __name__ == "__main__":
    main()