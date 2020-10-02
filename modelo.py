class ClasseFilme:
   def __init__(self,nome,ano,duracao):
       self.__nome = nome.title()
       self.__ano = ano
       self.__duracao = duracao
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
   @property
   def duracao(self):
       return self.__duracao
   @duracao.setter
   def duracao(self,valor):
       self.__duracao = valor
       



class ClasseSerie:

    def __init__(self,nome,ano,temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0
    def dar_like(self):
        self.__likes += 1
    @property
    def likes(self):
        return self.__likes
    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def temporadas(self,valor):
        self.__temporadas = valor    






