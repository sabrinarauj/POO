# exercício 1

class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool):
        
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

        if ano_publicacao <= 0:
            raise ValueError("O ano de publicação deve ser maior que 0")
        
        def emprestar(self):
            if not self.disponivel:
                raise Exception("Item já emprestado")
        self.disponivel = False
    

        def devolver(self):
             if self.disponivel:
                 raise Exception("Item disponível")
             self.disponivel = True

        def obter_info(self):
            return f"Título: {self.titulo} | Ano: {self.ano_publicacao} | Disponível: {self.disponivel}"
        
# exercício 2 

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int):
        super().__init__(titulo, ano_publicacao) #Herdando da classe pai
        self.livros = [] #Lista de livros para armazenar

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.livro.append(livro) # adiciona livro na coleção

    def verificar_disponibilidade_colecao(self):
        return(livro.disponivel for livro in self.livros)
    
    def obter_info(self):
        # o join ajuda a unir strings com concatenação
        info_livros = ",".join([livro.titulo for livro in self.livros])
        return (f"{super().obter_info()} | Livros na coleção: [{info_livros}]")
    
# exercício 3

class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: str, numero_edicao: int):
        super.__init__(titulo, ano_publicacao) # herança
        if numero_edicao <= 0:
            raise ValueError("Número da edição deve ser maior que 0")
        self.numero_edicao

    def atualizar_edicao(self, nova_edicao: int): # atualiza o número da edição
        if nova_edicao <= 0:
            raise ValueError("A nova edição deve ser maior que 0")
        self.numero_edicao = nova_edicao

    def restringir_emprestimo(self, dias_max: int): # verificar se a revista pode ser emprestada nos dias maximos
        if self.ano_publicacao <= 2000:
            return dias_max <= 7
        return True

    def obter_info(self):
        return f"{super().obter_info()} | Edição: {self.numero_edicao}"
    
# exercicio 4 
    
class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.itens:
            raise Exception("Item já cadastrado na biblioteca")
        self.itens[item.titulo] = item

    def remover_item(self, titulo: str):
        if titulo not in self.itens:
            raise Exception("Item nãio encontrado na biblioteca")
            self.itens[titulos]

    def listar_itens_disponiveis(self):
        # retorna uma lista com titulos disponiveis
        return [titulo for titulo, item in self.itens.itens() if item.disponivel]
    
    def contar_itens_emprestados(self):
        # conta os itens que serão emprestados
        return sum(1 for item in self.itens.values() if not item.disponivel)
    
# exercicio 5

class RelatorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
         relatorio = "Relatório completo: "
         for item in self.biblioteca.itens.values():
             relatorio += item.obter_info() 
         return relatorio
    
    def gerar_relatorio_disponiblidade(self):
        # lista itens e total deles
        disponiveis = self.biblioteca.listar_itens_disponiveis()
        relatorio = "Itens disponiveis: "
        for titulo in disponiveis:
            relatorio += f" - {titulo}"
        relatorio += f"Total disponivel: {disponiveis}"
        return relatorio
    
    def gerar_relatorio_emprestimos(self): # total de emprestados e sua proporção
        total_itens = self.biblioteca.itens
        emprestados = self.biblioteca.contar_itens_emprestados()
        proporcao =(emprestados / total_itens) * 100 
        return (f"Itens emprestados: {emprestados}") (f"Proporção: {proporcao:.2f}")