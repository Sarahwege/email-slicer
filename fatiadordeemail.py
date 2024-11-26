def fatiador de e-mail(e-mail):
    nome de usuário,_,domínio = e-mail.tira().partição("@")
    retornar f"Seu nome de usuário é{nome de usuário}& domínio é{domínio}"
entrada_do_usuário = entrada("Digite seu e-mail: ")
imprimir(fatiador de e-mail(entrada_do_usuário))
