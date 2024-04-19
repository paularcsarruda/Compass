def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo)
    

    produtos_acima_da_media = sorted([(produto, preco) for produto, preco in conteudo.items() if preco > media], key=lambda x: x[1])
    
    return produtos_acima_da_media
    