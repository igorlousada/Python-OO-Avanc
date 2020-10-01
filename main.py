from modelo import ClasseFilme,ClasseSerie

vingadores = ClasseFilme('Vingadores - Guerra Infinita','2012',120)
breakingbad = ClasseSerie('breaking bad','2008',5)
print(vingadores)
print(breakingbad)

vingadores.dar_like()
print(vingadores.like)