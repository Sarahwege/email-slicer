e-mail = entrada("Digite seu e-mail: ").tira()

nome de usuário = e-mail[:e-mail.índice('@')]
domínio = e-mail[e-mail.índice('@')+ 1:]

imprimir(f"Seu nome de usuário é{nome de usuário}& domínio é{domínio}")
