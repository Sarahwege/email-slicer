e-mail = entrada("Digite seu e-mail: ").tira()
nome de usuário = e-mail[:e-mail.índice("@")]
nome_de_domínio = e-mail[e-mail.índice("@")+1:]
formatar_ =(f"Seu nome de usuário é '{nome de usuário}' e seu domínio é '{nome_de_domínio}"")
imprimir(formatar_)
