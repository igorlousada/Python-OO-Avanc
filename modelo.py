class ClassePrograma:
    def __init__(self,nome,ano):
        self.__nome=nome.title()
        self.__ano=ano
        self.__likes = 0     
    def dar_like(self):
        self.__likes +=1  
    @property
    def likes(self):
        return self.__likes
    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self,valor):
        self.__ano = valor


class ClasseFilme(ClassePrograma):
   def __init__(self,nome,ano,duracao):
       super().__init__(nome, ano)
       self.__duracao = duracao
   @property
   def duracao(self):
       return self.__duracao
   @duracao.setter
   def duracao(self,valor):
       self.__duracao = valor
       



class ClasseSerie(ClassePrograma):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.__temporadas = temporadas
    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def temporadas(self,valor):
        self.__temporadas = valor    






