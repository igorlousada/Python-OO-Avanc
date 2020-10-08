from modelo import ClasseFilme,ClasseSerie,ClassePrograma,ClassePlaylist

vingadores = ClasseFilme('Vingadores - Guerra Infinita','2012',120)
breakingbad = ClasseSerie('breaking bad','2008',5)
print(vingadores)
print(breakingbad)

vingadores.dar_like()
print(vingadores.likes)

print(vingadores.likes)
print(vingadores.nome)
vingadores.ano = 2013
print(vingadores.ano)
vingadores.duracao = 200
print(vingadores.duracao)


playlist = [vingadores,breakingbad]
my_playlist = ClassePlaylist('my_playlist',playlist)
for programa in  my_playlist.listagem:
    print(programa)

print(my_playlist.tamanho)        