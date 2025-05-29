# Entrelinhas Clarice

Este projeto foi desenvolvido como entrega do **Projeto Livre de Orientação a Objetos **, com foco na aplicação prática dos conceitos abordados em aula. A proposta consiste em um sistema que permite o **cadastro de leitores**, **registro de livros**, **criação e listagem de postagens** com comentários sobre as obras literárias da autora Clarice Lispector, utilizando os recursos da orientação a objetos.


## ** Como executar o projeto**

### **🔧 Pré-requisitos**

Antes de rodar o projeto, é necessário instalar os seguintes pacotes Python:

```bash
pip install PySimpleGUI pillow

### **▶️ Executando**

Para iniciar a interface gráfica:

```bash
python main_gui.py

💾 Os dados são salvos automaticamente nos arquivos JSON localizados na pasta data/.


## 💡 Motivação e Histórico do Projeto

Inicialmente, o sistema foi implementado com **interface em terminal**, mas evoluiu para utilizar uma interface gráfica com **PySimpleGUI**. No entanto, o PySimpleGUI deixou de oferecer, recentemente, **licenças para hobbyistas**, tornando seu uso gratuito disponível apenas por **30 dias após a instalação**.

Assim, o projeto final da disciplina será retomado com base na ideia central do "Entrelinhas Clarice", **sem uso de GUI**, utilizando:

- ✔ **Serviços HTTP/HTTPS** para expor modelos por meio de páginas HTML/CSS/JS.
- ✔ **Sistema web com login** e controle de acesso a páginas, aplicando os conhecimentos adquiridos na **macrotarefa proposta pelo professor**.


## ✅ Critérios de Avaliação Atendidos

### ✔ Casos de Uso
- Cadastrar usuário (leitor).
- Criar uma postagem associando um leitor a um livro.
- Listar, editar e remover postagens e usuários.
- Visualizar livros disponíveis no sistema.

### ✔ Modelagem com Orientação a Objetos
- **Encapsulamento**: entidades como `Livro`, `Postagem`, `Pessoa`, `Leitor`.
- **Herança**: `Leitor` herda de `Pessoa`.
- **Composição forte**: `Postagem` composta por IDs de `Leitor` e `Livro`.
- **Associação fraca**: controladores manipulam listas de objetos.
- **Polimorfismo**: método `exibir_info()` com comportamentos distintos.

### ✔ Serialização de Objetos
- Todos os dados são persistidos por meio de arquivos `.json`, com uso de métodos `to_dict()` e `from_dict()`.

### ✔ Interface Gráfica
- Desenvolvida com **PySimpleGUI**, usando layout com rolagem, campos interativos e separação de janelas por funcionalidade.


## 📁 Estrutura do Projeto

```plaintext
├── controllers/
│   ├── livro_controller.py
│   ├── postagem_controller.py
│   └── usuario_controller.py
├── data/
│   ├── livros.json
│   ├── postagens.json
│   └── usuarios.json
├── imagens/
│   └── *.png (capas dos livros)
├── models/
│   ├── livro.py
│   ├── postagem.py
│   └── pessoa.py
├── main_gui.py
├── README.md