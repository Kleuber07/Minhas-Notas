# Cria e grava 3 frases no arquivo com 'w'
with open('minhas_notas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Hoje comecei a aprender Python.\n")
    arquivo.write("Aprendi a usar a função open para arquivos.\n")
    arquivo.write("Usei o modo 'w' para criar e escrever.\n")

# Adiciona 2 frases com 'a'
with open('minhas_notas.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write("Agora estou usando o modo 'a' para adicionar mais frases.\n")
    arquivo.write("Gostei de manipular arquivos com Python!\n")

# Lê e imprime o conteúdo do arquivo
with open('minhas_notas.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)