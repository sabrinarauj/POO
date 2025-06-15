class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao:  int, disponivel:  bool):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            print("O livro não está disponível")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
           print("Livro já devolvido")
        self.disponivel = True

    def obter_info(self):
        return f"Titulo: {self.titulo}, Ano: {self.ano_publicacao}, Disponivel: {self.disponivel}"

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                return False
        return True
    
class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool, numero_edicao: int):
        super().__init__(titulo, ano_publicacao, disponivel)
        if numero_edicao <= 0:
            raise ValueError("Não há edições publicadas")
        self.numero_edicao = numero_edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            raise ValueError("Não há novas edições")
        self.numero_edicao = nova_edicao

    def emprestimo(self, maximo_dias):
        if self.ano_publicacao <= 2000:
            return maximo_dias <= 7
        else:
            return True 
        
    def obter_info(self):
        info = super().obter_info()
        print(f"{info} \n Edição: {self.numero_edicao}")

class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.itens:
            print("Esse item já existe na biblioteca")
        self.itens[item.titulo] = item

    def remover_item(self, titulo):
        if titulo not in self.itens:
            print("Item não encontrado na biblioteca")
            self.itens[titulo]

    def itens_disponiveis(self):
        return [titulo for titulo, item in self.itens.items()]
    
    def contar_itens(self):
        return sum(1 for item in self.itens.values())
    
class RelatorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        relatorio = "Relatório biblioteca"
        for item in self.biblioteca.itens.values():
            relatorio += item.obter_info()
        return relatorio 
    
    def gerar_relatorio_disponiblidade(self):
        itens_disponiveis = [
            titulo for titulo, item in self.biblioteca.itens.items() 
        ]
        total_disponiveis = len(itens_disponiveis)
        total_itens = len(self.biblioteca.itens)

        relatorio = (f"{total_disponiveis} de {total_itens}")
    
        for titulo in itens_disponiveis:
            relatorio += (f"- {titulo}")
        return relatorio
    
    def gerar_relatorio_emprestimos(self):
        total_itens = len(self.biblioteca.itens)
        emprestados = self.biblioteca.contar_itens()

        if total_itens == 0:
            proporcao = 0
        else:
            proporcao = (emprestados / total_itens) * 100

            relatorio = (f"Itens emprestados: {emprestados} de {total_itens}")
            relatorio = (f"Proporção: {proporcao:.2f}%")
            return relatorio
        
# Lembrar de criar novos itens e testar novamente o código

    