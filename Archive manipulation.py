arquivo = open('texto.txt', 'r')

conteudo = arquivo.read()
print("Conteúdo do arquivo:")
print(conteudo)

num_caracteres = len(conteudo)
print("O arquivo tem", num_caracteres, "caracteres.")

frase = input("Digite uma frase para inserir no arquivo: ")

arquivo = open('texto.txt', 'a')
arquivo.write("\n" + frase)
print("Frase inserida com sucesso no final do arquivo!")

arquivo.close()

arquivo = open('texto.txt', 'r')
conteudo = arquivo.read()
print("\nConteúdo do arquivo atualizado:")
print(conteudo)

arquivo.close()
