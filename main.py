from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.__livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.__livros_emprestados) < 3 and livro.disponivel:
            self.__livros_emprestados.append(livro)
            livro.alterar_disponibilidade(False)

    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            livro.alterar_disponibilidade(True)

    def listar_livros_emprestados(self):
        return [livro.titulo for livro in self.__livros_emprestados]

class Administrador(Pessoa):
    def cadastrar_livro(self, biblioteca, titulo, autor, ano):
        novo_livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(novo_livro)

    def cadastrar_usuario(self, biblioteca, nome, idade, matricula):
        novo_usuario = UsuarioComum(nome, idade, matricula)
        biblioteca.adicionar_usuario(novo_usuario)

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    @abstractmethod
    def alterar_disponibilidade(self, status):
        pass

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor)
        self.ano_publicacao = ano_publicacao

    def alterar_disponibilidade(self, status):
        self.disponivel = status

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        return [livro.titulo for livro in self.livros if livro.disponivel]

    def listar_usuarios_com_livros(self):
        return {
            usuario.nome: usuario.listar_livros_emprestados()
            for usuario in self.usuarios if usuario.listar_livros_emprestados()
        }

biblioteca = Biblioteca()
admin = Administrador("Ana", 35)

admin.cadastrar_livro(biblioteca, "1984", "George Orwell", 1949)
admin.cadastrar_livro(biblioteca, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
admin.cadastrar_usuario(biblioteca, "João", 20, "1234")

usuario = biblioteca.usuarios[0]

usuario.emprestar_livro(biblioteca.livros[0])
print("Livros emprestados por João:", usuario.listar_livros_emprestados())

usuario.devolver_livro(biblioteca.livros[0])
print("Livros emprestados por João após devolução:", usuario.listar_livros_emprestados())

print("Livros disponíveis:", biblioteca.listar_livros_disponiveis())
print("Usuários com livros emprestados:", biblioteca.listar_usuarios_com_livros())
