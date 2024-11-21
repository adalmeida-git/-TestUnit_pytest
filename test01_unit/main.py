from src.service.service_user import ServiceUser


def main():
    service = ServiceUser()

    try:
        # Adicionar um usuário
 #       print(service.add_user("Andre", "Analyst"))

        # Tentar adicionar o mesmo usuário novamente (duplicado)
#        print(service.add_user("Andre", "Analyst"))

        # Adicionar um usuário diferente
 #       print(service.add_user("Andree", "Analyst"))

        # Remover um usuário existente
  #      print(service.remove_user("Andre", "Analyst"))

        # Tentar remover um usuário com parâmetros inválidos (nome vazio)
 #       print(service.add_user("andre", "Analyst"))
 #       print(service.store.bd[0].name)

        print(service.add_user("", "Analyst"))
        print(service.store.bd[0].name)

        # Atualizando usuário
   #     print(service.update_user("Andree", "Jose", "Analyst"))
    #    print(service.store.bd[0].name)

        # Atualizando que não existe
    #    print(service.update_user("Andre", "Jose", "Analyst"))

        #Retornar JOB
     #   print(service.get_user("Jose", "Analyst"))


    except Exception as e:
        print(f"Erro inesperado: {e}")


# Executar a função principal
if __name__ == "__main__":
    main()