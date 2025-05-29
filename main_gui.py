import io

import PySimpleGUI as sg
from controllers.usuario_controller import UsuarioController
from controllers.livro_controller import LivroController
from controllers.postagem_controller import PostagemController
from models.pessoa import Leitor
from models.postagem import Postagem
from PIL import Image

usuario_ctrl = UsuarioController()
livro_ctrl = LivroController()
livro_ctrl.carregar_livros_padrao()
postagem_ctrl = PostagemController()

def mostrar_mensagem(titulo, mensagem):
    sg.popup(titulo, mensagem)

def carregar_imagem_para_tk(caminho, tamanho=(100, 150)):
    try:
        img = Image.open(caminho)
        img.thumbnail(tamanho)
        bio = io.BytesIO()
        img.save(bio, format='PNG')
        return bio.getvalue()
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")
        return None

def nova_janela_menu():
    layout_menu = [
        [sg.Text('Bem-vindo ao Entrelinhas Clarice!', font=('Helvetica', 16))],
        [sg.Button('Cadastrar Usuário')],
        [sg.Button('Criar Postagem')],
        [sg.Button('Ver Postagens')],
        [sg.Button('Ver Usuários')],
        [sg.Button('Ver Livros')],
        [sg.Button('Editar Usuário')],
        [sg.Button('Remover Usuário')],
        [sg.Button('Editar Postagem')],
        [sg.Button('Remover Postagem')],
        [sg.Button('Sair')]
    ]
    return sg.Window('Entrelinhas Clarice', layout_menu, finalize=True, size=(400, 500), resizable=True)

def janela_cadastro_usuario():
    layout = [
        [sg.Text('Nome:'), sg.Input(key='nome')],
        [sg.Text('Email:'), sg.Input(key='email')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')]
    ]
    return sg.Window('Cadastro de Usuário', layout, finalize=True)

def janela_criar_postagem():
    usuarios = usuario_ctrl.listar_usuarios()
    livros = livro_ctrl.listar_livros()
    layout = [
        [sg.Text('Selecione o usuário:')],
        [sg.Combo([f"{u.nome} ({u.email})" for u in usuarios], key='usuario')],
        [sg.Text('Selecione o livro:')],
        [sg.Combo([f"{l.titulo} - {l.autor}" for l in livros], key='livro')],
        [sg.Text('Comentário:')],
        [sg.Multiline(key='comentario', size=(60, 10))],
        [sg.Button('Postar'), sg.Button('Voltar')]
    ]
    return sg.Window('Criar Postagem', layout, finalize=True, size=(700, 400), resizable=True)



def janela_listar_postagens():
    postagens = postagem_ctrl.listar_postagens()
    usuarios = {u.id: u.nome for u in usuario_ctrl.listar_usuarios()}
    livros = {l.id: (l.titulo, l.caminho_imagem) for l in livro_ctrl.listar_livros()}
    
    layout = [
        [sg.Text('Postagens Recentes:', font=('Helvetica', 14))]
    ]

    # Container para manter todas as postagens
    postagens_frame = []

    for p in postagens:
        nome = usuarios.get(p.leitor_id, 'Desconhecido')
        titulo, imagem = livros.get(p.livro_id, ('Desconhecido', None))
        linha = []

        # Carregar imagem
        imagem_bytes = carregar_imagem_para_tk(imagem) if imagem else None
        if imagem_bytes:
            linha.append(sg.Image(data=imagem_bytes, size=(100, 150)))
        
        # Texto com a postagem
        linha.append(sg.Text(f"{nome} leu '{titulo}' e comentou em {p.data}:"))
        postagens_frame.append(linha)

        # Comentário da postagem com scroll
        postagens_frame.append([
            sg.Multiline(default_text=p.comentario, size=(80, 10), disabled=True, no_scrollbar=False, autoscroll=True)
        ])
        postagens_frame.append([sg.HorizontalSeparator()])

    # Usando sg.Column para criar a área de postagens rolável
    postagens_column = sg.Column(postagens_frame, scrollable=True, vertical_scroll_only=True, size=(800, 400))

    # Adiciona a coluna com as postagens no layout
    layout.append([postagens_column])

    # Botão de voltar
    layout.append([sg.Button('Voltar')])

    # Cria a janela com rolagem
    return sg.Window('Postagens', layout, finalize=True, size=(800, 600), resizable=True)




def janela_listar_usuarios():
    usuarios = usuario_ctrl.listar_usuarios()
    layout = [[sg.Text('Usuários Cadastrados:', font=('Helvetica', 14))]]
    for u in usuarios:
        layout.append([sg.Text(u.exibir_info())])
    layout.append([sg.Button('Voltar')])
    return sg.Window('Usuários', layout, finalize=True, size=(600, 400), resizable=True)

def janela_listar_livros():
    livros = livro_ctrl.listar_livros()
    layout = [[sg.Text('Livros Disponíveis:', font=('Helvetica', 14))]]
    for l in livros:
        layout.append([sg.Text(l.exibir_info())])
    layout.append([sg.Button('Voltar')])
    return sg.Window('Livros', layout, finalize=True, size=(600, 440), resizable=True)

def janela_editar_usuario():
    usuarios = usuario_ctrl.listar_usuarios()
    layout = [
        [sg.Text('Selecione um usuário:')],
        [sg.Combo([f"{u.nome} ({u.email})" for u in usuarios], key='usuario')],
        [sg.Text('Novo nome:'), sg.Input(key='novo_nome')],
        [sg.Text('Novo email:'), sg.Input(key='novo_email')],
        [sg.Button('Salvar'), sg.Button('Voltar')]
    ]
    return sg.Window('Editar Usuário', layout, finalize=True, size=(600, 300), resizable=True)

def janela_remover_usuario():
    usuarios = usuario_ctrl.listar_usuarios()
    layout = [
        [sg.Text('Selecione o usuário a remover:')],
        [sg.Combo([f"{u.nome} ({u.email})" for u in usuarios], key='usuario')],
        [sg.Button('Remover'), sg.Button('Voltar')]
    ]
    return sg.Window('Remover Usuário', layout, finalize=True, size=(500, 200), resizable=True)

def janela_editar_postagem():
    postagens = postagem_ctrl.listar_postagens()
    usuarios = {u.id: u.nome for u in usuario_ctrl.listar_usuarios()}
    livros = {l.id: l.titulo for l in livro_ctrl.listar_livros()}
    layout = [[sg.Text('Editar Postagem:', font=('Helvetica', 14))]]
    opcoes = [f"{i} - {usuarios.get(p.leitor_id)}: {livros.get(p.livro_id)} - {p.comentario}" for i, p in enumerate(postagens)]
    layout += [
        [sg.Combo(opcoes, key='postagem')],
        [sg.Text('Novo comentário:'), sg.Multiline(key='novo_comentario', size=(60, 10))],
        [sg.Button('Salvar'), sg.Button('Voltar')]
    ]
    return sg.Window('Editar Postagem', layout, finalize=True, size=(700, 300), resizable=True)

def janela_remover_postagem():
    postagens = postagem_ctrl.listar_postagens()
    usuarios = {u.id: u.nome for u in usuario_ctrl.listar_usuarios()}
    livros = {l.id: l.titulo for l in livro_ctrl.listar_livros()}
    layout = [[sg.Text('Remover Postagem:', font=('Helvetica', 14))]]
    opcoes = [f"{i} - {usuarios.get(p.leitor_id)}: {livros.get(p.livro_id)} - {p.comentario}" for i, p in enumerate(postagens)]
    layout += [
        [sg.Combo(opcoes, key='postagem')],
        [sg.Button('Remover'), sg.Button('Voltar')]
    ]
    return sg.Window('Remover Postagem', layout, finalize=True, size=(700, 250), resizable=True)

janela = nova_janela_menu()

while True:
    evento, valores = janela.read()
    if evento in (sg.WIN_CLOSED, 'Sair'):
        break

    if evento == 'Cadastrar Usuário':
        janela.close()
        janela = janela_cadastro_usuario()

    elif evento == 'Criar Postagem':
        janela.close()
        janela = janela_criar_postagem()

    elif evento == 'Ver Postagens':
        janela.close()
        janela = janela_listar_postagens()

    elif evento == 'Ver Usuários':
        janela.close()
        janela = janela_listar_usuarios()

    elif evento == 'Ver Livros':
        janela.close()
        janela = janela_listar_livros()

    elif evento == 'Editar Usuário':
        janela.close()
        janela = janela_editar_usuario()

    elif evento == 'Remover Usuário':
        janela.close()
        janela = janela_remover_usuario()

    elif evento == 'Editar Postagem':
        janela.close()
        janela = janela_editar_postagem()

    elif evento == 'Remover Postagem':
        janela.close()
        janela = janela_remover_postagem()

    elif evento == 'Cadastrar':
        nome = valores['nome']
        email = valores['email']
        if nome and email:
            usuario_ctrl.adicionar_usuario(Leitor(nome, email))
            mostrar_mensagem('Sucesso', 'Usuário cadastrado com sucesso!')
            janela.close()
            janela = nova_janela_menu()
        else:
            mostrar_mensagem('Erro', 'Preencha todos os campos.')

    elif evento == 'Postar':
        usuario_nome = valores['usuario']
        livro_info = valores['livro']
        comentario = valores['comentario'].strip()
        usuarios = usuario_ctrl.listar_usuarios()
        livros = livro_ctrl.listar_livros()
        leitor = next((u for u in usuarios if f"{u.nome} ({u.email})" == usuario_nome), None)
        livro = next((l for l in livros if f"{l.titulo} - {l.autor}" == livro_info), None)
        if leitor and livro and comentario:
            postagem = Postagem(leitor.id, livro.id, comentario)
            postagem_ctrl.adicionar_postagem(postagem)
            mostrar_mensagem('Sucesso', 'Postagem criada!')
            janela.close()
            janela = nova_janela_menu()
        else:
            mostrar_mensagem('Erro', 'Preencha todos os campos corretamente.')

    elif evento == 'Salvar':
        if 'usuario' in valores and valores['usuario']:
            nome_original = valores['usuario']
            novo_nome = valores['novo_nome']
            novo_email = valores['novo_email']
            for u in usuario_ctrl.listar_usuarios():
                if f"{u.nome} ({u.email})" == nome_original:
                    u.nome = novo_nome
                    u.email = novo_email
                    usuario_ctrl.salvar_usuarios()
                    mostrar_mensagem('Sucesso', 'Usuário editado com sucesso!')
                    break
            janela.close()
            janela = nova_janela_menu()

        elif 'postagem' in valores and valores['postagem']:
            idx = int(valores['postagem'].split(' - ')[0])
            novo_comentario = valores['novo_comentario'].strip()
            if novo_comentario:
                postagem_ctrl.postagens[idx].comentario = novo_comentario
                postagem_ctrl.salvar_postagens()
                mostrar_mensagem('Sucesso', 'Comentário atualizado!')
                janela.close()
                janela = nova_janela_menu()

    elif evento == 'Remover':
        if 'usuario' in valores and valores['usuario']:
            nome_selecionado = valores['usuario']
            for i, u in enumerate(usuario_ctrl.listar_usuarios()):
                if f"{u.nome} ({u.email})" == nome_selecionado:
                    del usuario_ctrl.usuarios[i]
                    usuario_ctrl.salvar_usuarios()
                    mostrar_mensagem('Sucesso', 'Usuário removido.')
                    break
            janela.close()
            janela = nova_janela_menu()

        elif 'postagem' in valores and valores['postagem']:
            idx = int(valores['postagem'].split(' - ')[0])
            del postagem_ctrl.postagens[idx]
            postagem_ctrl.salvar_postagens()
            mostrar_mensagem('Sucesso', 'Postagem removida.')
            janela.close()
            janela = nova_janela_menu()

    elif evento == 'Voltar':
        janela.close()
        janela = nova_janela_menu()

janela.close()
