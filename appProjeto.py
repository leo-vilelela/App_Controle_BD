import sqlite3

banco= sqlite3.connect('LCBL.db') # CRIANDO CONEXÃO COM O BANCO DE DADOS SQLITE...
cursor= banco.cursor()            # CRIANDO CURSOR PARA EXECUTAR OS COMANDOS SQLITE...

# COMANDOS PARA CRIAÇÃO DAS TABELAS...
cursor.execute("CREATE TABLE if not exists clientes(nome_do_cliente text, telefone text, cpf text )")
cursor.execute("CREATE TABLE if not exists produtos(produto text, valor real, descrição text )")

# INICICIANDO VARIÁVEIS PARA AS CONDIÇÕES QUE SERÃO USADAS NO CODIGO...
cont = False
log = False
acesso= False
opcaoAdmin=False

# DEFININDO FUNÇÃO PARA CADASTRO DE PRODUTOS...
def cdPdt():    
    cursor.execute("CREATE TABLE if not exists produtos(produto text, valor real, descrição text )")
    while True:
        try: # <- COMANDO PARA TRATAMENTO DE EXCEÇÕES...  
            print('\n\n::::: PRODUTOS CADASTRADOS :::::')
            print(   "ID\t--- PRODUTO ---\n" )
            cursor.execute("SELECT rowid, * FROM produtos")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1])
            print('\n\n::::: área DE CADASTRO DE PRODUTOS! :::::\n')
            produtos= (input("Digite o nome do produto:\n"))
            valores= (float(input("Digite o valor de venda:\n")))
            descrição=input("Digite a descrição:\n")
            rows=cursor.fetchall()
            cursor.execute("INSERT INTO produtos values( '"+produtos+"', "+str(valores)+",'"+descrição+"')")
            banco.commit()
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("Formato invalido! Tente novamente:")
            print("-----------------------------------------------------------------------------\n")
        else:
            print("\n-----------------------------------------------------------------------------")
            print("::::: Produto cadastrado com sucesso! :::::")
            print("-----------------------------------------------------------------------------\n")
            print(   "ID\t--- PRODUTO ---\n" )
            cursor.execute("SELECT rowid, * FROM produtos")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1])      
        break        

# DEFININDO FUNÇÃO PARA VISUALIZAR DETALHES DOS PRODUTOS...
def pPdt():
    while True:
        print('\n\n::::: PRODUTOS CADASTRADOS :::::')
        print(   "ID\t--- PRODUTO ---\n" )
        cursor.execute("SELECT rowid, * FROM produtos")            
        rows= cursor.fetchall()  
        for row in rows:
            print(row[0],'\t',row[1]) 
        print('\n\n::::: área DE INFORMAÇÕES DE PRODUTOS! :::::\n')
        pesquisar = input("\nDigite o código do produto para visualizar as informações:\n")
        cursor.execute("SELECT * FROM produtos WHERE rowid = '"+pesquisar+"'")
        choice=cursor.fetchall()
        for line in choice:
            print("\n___________________________________________________________________________________________________________________\n")
            print(' Modelo - ', line[0],'\n','Valor - R$',line[1],'\n','Descrição do produto:\n\n',line[2],'\n\n')
            print("___________________________________________________________________________________________________________________\n")
            break
        break

# DEFININDO FUNÇÃO PARA ALTERAÇÃO PRODUTOS...            
def alterarProduto():
    while True:
        try:
            print('\n\n::::: PRODUTOS CADASTRADOS :::::')
            print(   "ID\t--- PRODUTO ---\n" )
            cursor.execute("SELECT rowid, * FROM produtos")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1]) 
            print('\n\n::::: área DE ALTERAÇÃO DE PRODUTOS! :::::\n')
            pesquisar = int(input("Digite o id do produto que deseja alterar:\n"))
            produtos= (input("Digite o nome do produto:\n"))
            valores= (float(input("Digite o valor de venda:\n")))
            descrição=input("Digite a descrição:\n")
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("Formato invalido! Tente novamente:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            cursor.execute("UPDATE produtos SET produto = (?), valor = (?), descrição = (?) WHERE rowid = '"+str(pesquisar)+"'",(produtos, valores, descrição))
            banco.commit()
            print('\n\n::::: PRODUTOS CADASTRADOS :::::')
            print(   "ID\t--- PRODUTO ---\n" )
            cursor.execute("SELECT rowid, * FROM produtos")
            rows=cursor.fetchall()
            for row in rows:
                print(row[0],'\t',row[1])
            print("\n-----------------------------------------------------------------------------")
            print("::::: PRODUTO ALTERADO COM SUCESSO! :::::")
            print("-----------------------------------------------------------------------------\n") 
            break  
    
# DEFININDO FUNÇÃO PARA EXCLUSÃO PRODUTOS...
def excluirProduto():
    while True:
        try:
            print('\n\n::::: PRODUTOS CADASTRADOS :::::')
            print(   "ID\t--- PRODUTO ---\n" )
            cursor.execute("SELECT rowid, * FROM produtos")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1]) 
            print('\n\n::::: ÁREA DE EXCLUSÃO DE PRODUTOS! :::::\n')
        
            pesquisar = int(input("Digite o id do produto que deseja excluir:\n"))
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("Formato invalido! Tente novamente:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            cursor.execute("SELECT rowid, * FROM produtos WHERE rowid = '"+str(pesquisar)+"'")            
            rows= cursor.fetchall()
            print("\n-----------------------------------------------------------------------------")
            print("Tem certeza que deseja excluir este item?:")
            print("-----------------------------------------------------------------------------\n")
            print(   "ID\t--- PRODUTO ---" )
            for row in rows:
                print(row[0],'\t',row[1],'\n')

            y=input("Digite: 'y' para excluir...  ou digite: 'n' para cancelar a exclusão:\n ")
            if y == "y":
                cursor.execute("DELETE FROM produtos WHERE rowid = '"+str(pesquisar)+"'")
                banco.commit()
            
                print('\n\n::::: PRODUTOS CADASTRADOS :::::')
                print(   "ID\t--- PRODUTO ---\n" )
                cursor.execute("SELECT rowid, * FROM produtos")            
                rows= cursor.fetchall()  
                for row in rows:
                    print(row[0],'\t',row[1])
                print("\n-----------------------------------------------------------------------------")
                print("::::: PRODUTO EXCLUÍDO COM SUCESSO! :::::")
                print("-----------------------------------------------------------------------------\n")
                break
            else:
                print('\n\n::::: PRODUTOS CADASTRADOS :::::')
                print(   "ID\t--- PRODUTO ---\n" )
                cursor.execute("SELECT rowid, * FROM produtos")            
                rows= cursor.fetchall()  
                for row in rows:
                    print(row[0],'\t',row[1])         
                print("\n-----------------------------------------------------------------------------")
                print("::::: EXCLUSÃO CANCELADA! :::::")
                print("-----------------------------------------------------------------------------\n")
                break
    
# DEFININDO FUNÇÃO PARA ALTERAÇÃO CLIENTE...
def alterarCliente():
    while True:
        try:
            print('\n\n::::: CLIENTES CADASTRADOS :::::')
            print(   "ID\t--- CLIENTE ---\n" )
            cursor.execute("SELECT rowid, * FROM clientes")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1]) 
            
            print('\n\n::::: ÁREA DE ALTERAÇÃO DE CLIENTES! :::::\n')
            pesquisar = int(input("Digite o id do cliente que deseja alterar:\n"))
            clientes=input("Digite o mome do cliente:\n")
            telefones=input("Digite o numero de telefone do cliente:\n")
            cpf= int(input("Digite o CPF do cliente:\n"))
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("FORMATO INVALIDO! TENTE NOVAMENTE:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            cursor.execute("UPDATE clientes SET nome_do_cliente = (?), telefone = (?), cpf = (?) WHERE rowid = '"+str(pesquisar)+"'",(clientes, telefones, str(cpf)))
            banco.commit()
            print('\n\n::::: CLIENTES CADASTRADOS :::::')
            print(   "ID\t--- CLIENTE ---\n" )
            cursor.execute("SELECT rowid, * FROM clientes")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1]) 
            print("\n-----------------------------------------------------------------------------")
            print("::::: CLIENTE ALTERADO COM SUCESSO! :::::")
            print("-----------------------------------------------------------------------------\n") 
            break  
    
#  DEFININDO FUNÇÃO PARA EXCLUSÃO DE CLIENTE...
def excluirCliente():
    while True:
        print('\n\n::::: CLIENTES CADASTTRADOS :::::')
        print(   "ID\t----- CLIENTE -----" )
        cursor.execute("SELECT rowid, * FROM clientes")            
        rows= cursor.fetchall()  
        for row in rows:
            print(row[0],'\t',row[1])
        print('\n\n::::: ÁREA DE EXCLUSÃO DE CLIENTES! :::::\n')
        try:
            pesquisar = int(input("Digite o id do cliente que deseja excluir:\n"))
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("FORMATO INVALIDO! TENTE NOVAMENTE:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            cursor.execute("SELECT rowid, * FROM clientes WHERE rowid ='"+str(pesquisar)+"'")            
            rows= cursor.fetchall()
            print("\n-----------------------------------------------------------------------------")
            print("Tem certeza que deseja excluir este cliente?:")
            print("-----------------------------------------------------------------------------\n")
            print(   "ID\t----- CLIENTE -----" )
            for row in rows:
                print(row[0],'\t',row[1],'\n')

            y=input("Digite: 'y' para excluir...  ou digite: 'n' para cancelar a exclusão:\n ")
            if y == "y":
                cursor.execute("DELETE FROM clientes WHERE rowid = '"+str(pesquisar)+"'")
                banco.commit()
            
                print('\n\n::::: CLIENTES CADASTTRADOS :::::')
                print(   "ID\t----- CLIENTE -----" )
                cursor.execute("SELECT rowid, * FROM clientes")            
                rows= cursor.fetchall()  
                for row in rows:
                    print(row[0],'\t',row[1])
                print("\n-----------------------------------------------------------------------------")
                print("::::: CLIENTE EXCLUÍDO COM SUCESSO! :::::")
                print("-----------------------------------------------------------------------------\n")
                break
            else:
                
                print('\n\n::::: CLIENTES CADASTTRADOS :::::')
                print(   "ID\t----- CLIENTE -----" )
                cursor.execute("SELECT rowid, * FROM clientes")            
                rows= cursor.fetchall()  
                for row in rows:
                    print(row[0],'\t',row[1])        
                print("\n-----------------------------------------------------------------------------")
                print("::::: EXCLUSÃO CANCELADA! :::::")
                print("-----------------------------------------------------------------------------\n")
                break

# DEFNINDO FUNÇÃO PARA CADASTRO DE CLIENTES...     
def cdClt():
    while True:
        print('\n\n::::: CLIENTES CADASTTRADOS :::::')
        print(   "ID\t----- CLIENTE -----" )
        cursor.execute("SELECT rowid, * FROM clientes")            
        rows= cursor.fetchall()  
        for row in rows:
            print(row[0],'\t',row[1])
        try:
            print('\n\n::::: ÁREA DE CADASTRO DE CLIENTES! :::::\n')
            clientes=input("\nDigite o mome do cliente:\n")
            telefones=input("Digite o numero de telefone do cliente:\n")
            cpf= int(input("Digite o CPF do cliente (APENAS NÚMEROS!):\n"))
            cursor.execute("INSERT INTO clientes values('"+clientes+"', "+telefones+","+str(cpf)+")")
            banco.commit()
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("FORMATO INVALIDO! TENTE NOVAMENTE:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            print("\n-----------------------------------------------------------------------------")
            print("::::: CLIENTE CADASTRADO COM SUCESSO! :::::")
            print("-----------------------------------------------------------------------------\n")
            print('\n\n::::: CLIENTES CADASTTRADOS :::::')
            print(   "ID\t----- CLIENTE -----" )
            cursor.execute("SELECT rowid, * FROM clientes")            
            rows= cursor.fetchall()  
            for row in rows:
                print(row[0],'\t',row[1])
            break

# DEFININDO FUNÇÃO PARA VISUALIZAÇÃO DAS INFORMAÇÕES DOS CLIENTES...
def pClt():
    while True:
        print('\n\n::::: CLIENTES CADASTTRADOS :::::')
        print(   "ID\t----- CLIENTE -----" )
        cursor.execute("SELECT rowid, * FROM clientes")            
        rows= cursor.fetchall()  
        for row in rows:
            print(row[0],'\t',row[1])
        try:
            print('\n\n::::: ÁREA DE INFORMAÇÕES DE CLIENTES! :::::\n')
            pCliente = int(input("Digite o indice do cliente para visualizar as informações:\n"))
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("Formato invalido! Tente novamente:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            print('\n\n')
            cursor.execute("SELECT rowid, * FROM clientes WHERE rowid = '"+str(pCliente)+"'")             
            rows= cursor.fetchall()  
            for row in rows:
                print("___________________________________________________________________________________________________________________\n")
                print('Nome -',row[1], '\nTelefone -', row[2], '\nCPF -', row[3])
                print("___________________________________________________________________________________________________________________\n")

            break
# DEFININDO FUNÇÃO PARA ACESSO DO CLIENTE...
def acesso2():
    print("\n\n")
    print("::::: BEM VINDO À LCBL! :::::")
    print("\n-----------------------------------------------------------------------------")
    print(":::: ÁREA DO CLIENTE ::::")
    print("-----------------------------------------------------------------------------\n")    
    while True:
        try:
            cursor.execute("SELECT rowid, * FROM produtos")            
            print("___________________ GALERIA ___________________\n")
            print('::::: PRODUTOS CADASTRADOS :::::')
            print(   "\nID\t--- PRODUTO ---\n" )
            rows= cursor.fetchall() 
            for row in rows:
                print(row[0],'\t',row[1],)
            print('\n')
            escolha = int(input('Digite o indice para visualizar a descrição do produto:\n Ou digite "0" para sair:'))
        except ValueError:
            print("\n-----------------------------------------------------------------------------")
            print("Formato invalido! Tente novamente:")
            print("-----------------------------------------------------------------------------\n")
            break
        else:
            if escolha != 0:            
                cursor.execute("SELECT * FROM produtos WHERE rowid = "+str(escolha)+"")
                choice=cursor.fetchall()
                for line in choice:
                    print("\n___________________________________________________________________________________________________________________\n")
                    print(' Modelo - ', line[0],'\n','Valor - R$',line[1],'\n','Descrição do produto:\n\n',line[2],)
                    print("___________________________________________________________________________________________________________________\n")
                    break
                break
            else:
                break 

acesso = input("BEM INDO À LCBL!!\n----------------------------------------------------------------------------- \nDigite o número da opção com a qual você deseja acessar:\n 1- Administrador\n 2- Cliente\n")
cont="s"
if acesso == "2":
    while cont != 'n':
        acesso2()         
        cont = input("Deseja continuar na área do cliente? (s/n)\n\n")
        continue
    acesso = input("Bem vindo á LCBL!\n----------------------------------------------------------------------------- \nDigite o número da opção com a qual você deseja acessar:\n 1- Administrador\n 2- Cliente\n")

# VALIDAÇÃO DE USUÁRIO...
while acesso != "2"and acesso != "1":
    acesso = input("OPÇÃO INVÁLIDA!!!\n----------------------------------------------------------------------------- \nDigite o número da opção com a qual você deseja acessar:\n 1- Administrador\n 2- Cliente\n")
x = 0
if (acesso == "1" ):
    while (x < 4 and log != True):
        user = input("Digite o nome de Usuário: \n")
        
        x = x+1
        cursor.execute("SELECT * FROM usuarios WHERE usuario = '"+user.lower()+"' ")
        login= cursor.fetchall()
        if login != []:
            print("\n")
            print("Olá", user.upper(), "!\n")
            log = True
            # VALIDAÇÃO DE SENHA...
            snha = input("Digite sua senha:")
            cursor.execute("SELECT * FROM usuarios WHERE senha = '"+snha+"' ")
            pswd= cursor.fetchall()
            while pswd == []:
                print("\n-----------------------------------------------------------------------------")
                print("Senha Invalida!")
                print("-----------------------------------------------------------------------------\n")
                snha = input("Digite sua senha:")
                cursor.execute("SELECT * FROM usuarios WHERE senha = '"+snha+"' ")
                pswd= cursor.fetchall()
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Você está logado como administrador!")
                print("-----------------------------------------------------------------------------\n")
                
                cont="n"
                # MENU DE ACESSO, ÁREA DO ADMINISTRADOR...
                while cont != "s":
                    opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Informações de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Alterar produto\n 6- Excluir produto \n 7- Alterar cliente\n 8- Excluir cliente\n \nOU DIGITE - 0 - PARA ACESSAOR A ÁREA DO CLIENTE! ")                                       
                    while opcaoAdmin != "0" and opcaoAdmin != "1" and opcaoAdmin != "2" and opcaoAdmin != "3" and opcaoAdmin != "4" and opcaoAdmin != "5" and opcaoAdmin != "6" and opcaoAdmin != "7" and opcaoAdmin != "8": 
                        print("\n-----------------------------------------------------------------------------")
                        print("OPÇÃO INVÁLIDA!!!")
                        print("-----------------------------------------------------------------------------\n")
                        opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Informações de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Alterar produto\n 6- Excluir produto\n 7- Alterar cliente\n 8- Excluir cliente\n \nOU DIGITE - 0 - PARA ACESSAOR A ÁREA DO CLIENTE! ")                                       

                    # OPÇÕES DO MENU DE ACESSO, CHAMANDO AS FUNÇÕES... 
                    cont="s"
                    if opcaoAdmin == "0":
                        while cont != 'n':
                            acesso2()         
                            cont = input("Deseja continuar na área do cliente? (s/n)\n\n")

                    if opcaoAdmin == "1":
                        while cont != 'n':
                            cdPdt()                            
                            cont = input("Deseja cadastrar outro produto? (s/n)\n\n")
                       
                    if opcaoAdmin == "2":
                        while cont != 'n':
                            pPdt()
                            cont = input("Deseja visualizar informações de outro produto? (s/n)\n\n")
                       
                    if opcaoAdmin == "3":
                        while cont != 'n':
                            cdClt()
                            cont = input("Deseja cadastrar mais algum cliente? (s/n)\n\n")
                        
                    if opcaoAdmin == "4":
                        while cont != 'n':
                            pClt()
                            cont = input("Deseja visualizar as informaçoes de agum outro cliente? (s/n)\n\n")
                        
                    if opcaoAdmin == "5":
                        while cont != 'n':
                            alterarProduto()
                            cont = input("Deseja alterar mais algum produto? (s/n)\n\n")
                        
                    if opcaoAdmin == "6":
                        while cont != 'n':
                            excluirProduto()
                            cont = input("Deseja excluir outro produto? (s/n)\n\n")

                    if opcaoAdmin == "7":
                        while cont != 'n':
                            alterarCliente()
                            cont = input("Deseja alterar outro cliente? (s/n)\n\n")

                    if opcaoAdmin == "8":
                        while cont != 'n':
                            excluirCliente()
                            cont = input("Deseja excluir outro cliente? (s/n)\n\n")
        
        #COMANDO PARA TRATAR AS TENTATIVAS DE LOGIN INVALIDAS...
        else:
            print("Usuário invalido! você tem mais ", 4-x, "tentativas:")

