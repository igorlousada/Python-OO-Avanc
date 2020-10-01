class ClasseFilme:
   def __init__(self,nome,ano,duracao,likes=0):
       self.__nome = nome.title()
       self.__ano = ano
       self.__duracao = duracao
       self.__likes = likes
    
   def dar_like(self):
       self.__likes +=1  
   @property
   def like(self):
       return self.__likes
class ClasseSerie:

    def __init__(self,nome,ano,temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas    


