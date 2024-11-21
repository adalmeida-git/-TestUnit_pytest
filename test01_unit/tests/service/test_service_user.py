

import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuário adicionado"

        #chamada
        resultado = service.add_user("Andre", "Analyst")

        #Validação
        assert resultado == resultado_esperado


    def test_add_user_duplicado(self):
        #setup
        service = ServiceUser()
        primeiro_resultado_esperado = "Usuário adicionado"
        resultado_esperado = "Usuário já existe"

        #chamada

        resultado_add = service.add_user("Andre", "Analyst")
        resultado_duplicado = service.add_user("Andre", "Analyst")

        #Validação

        assert resultado_add == primeiro_resultado_esperado
        assert resultado_duplicado == resultado_esperado


    def test_add_user_invalido(self):

        service = ServiceUser()
        resultado_erro_string = "Não é string"

        # chamada
        resultado_add_invalido = service.add_user(123123, "Analyst")
        # Validação
        assert resultado_add_invalido == resultado_erro_string


    def test_add_user_vazio(self):
        service = ServiceUser()
        resultado_parametro_name_incorreto = "Parametros inválidos"
        resultado_parametro_job_incorreto = "Parametros inválidos"

        # chamada
        parametro_name_incorreto = service.add_user("", "Analyst")
        parametro_job_incorreto = service.add_user("Andre", "")

        # Validação
        assert parametro_name_incorreto == resultado_parametro_name_incorreto
        assert parametro_job_incorreto == resultado_parametro_job_incorreto


    def test_remove_success(self):
         # Setup
        service = ServiceUser()
        resultado_remove = "Usuário removido"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        remove_user = service.remove_user("Andre", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_remove == remove_user

    def test_remove_does_not_exist(self):
         # Setup
        service = ServiceUser()
        resultado_remove = "Usuário não existe"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        remove_user = service.remove_user("Pedro", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_remove == remove_user


    def test_remove_invalid(self):
         # Setup
        service = ServiceUser()
        resultado_remove = "parametro inválidos"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        remove_user = service.remove_user(1234234, "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_remove == remove_user

    def test_remove_none(self):
         # Setup
        service = ServiceUser()
        resultado_remove = "parametro vazio"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        remove_user = service.remove_user("", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_remove == remove_user



    def test_update_success(self):
         # Setup
        service = ServiceUser()
        resultado_update = "Nome atualizado com sucesso"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        update_user = service.update_user("Andre", "Pedro", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_update == update_user


    def test_update_not_update(self):
         # Setup
        service = ServiceUser()
        resultado_update = "Nome não atualizado"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        update_user = service.update_user("Joao", "Pedro", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_update == update_user


    def test_update_param_incorret(self):
         # Setup
        service = ServiceUser()
        resultado_update = "Parametro incorreto"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        update_user = service.update_user(21312, "Pedro", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_update == update_user

    def test_update_param_none(self):
         # Setup
        service = ServiceUser()
        resultado_update = "Variavel incorreta"
        resultado_create = "Usuário adicionado"

        # chamada
        create_user = service.add_user("Andre", "Analyst")
        update_user = service.update_user("", "Pedro", "Analyst")

        # Validação
        assert resultado_create == create_user
        assert resultado_update == update_user


    def test_get_user_sucess(self):
        #setup
        service = ServiceUser()
        resultado_create = "Usuário adicionado"
        resultado_get = "Analyst"

        #chamada
        create_user = service.add_user("Andre", "Analyst")
        get_user = service.get_user("Andre","Analyst")


        #Validação
        assert resultado_create == create_user
        assert resultado_get == get_user

    def test_get_user_none(self):
        #setup
        service = ServiceUser()
        resultado_create = "Usuário adicionado"
        resultado_get = "Vazio"

        #chamada
        create_user = service.add_user("Andre", "Analyst")
        get_user = service.get_user("Andre","")


        #Validação
        assert resultado_create == create_user
        assert resultado_get == get_user


    def test_get_user_incorret(self):
        #setup
        service = ServiceUser()
        resultado_create = "Usuário adicionado"
        resultado_get = "Parametro incorreto"

        #chamada
        create_user = service.add_user("Andre", "Analyst")
        get_user = service.get_user("Andre",123123)


        #Validação
        assert resultado_create == create_user
        assert resultado_get == get_user


    def test_get_user_not_found(self):
        #setup
        service = ServiceUser()
        resultado_create = "Usuário adicionado"
        resultado_get = "Não encontrado"

        #chamada
        create_user = service.add_user("Andre", "Analyst")
        get_user = service.get_user("Pedro","Analyst")


        #Validação
        assert resultado_create == create_user
        assert resultado_get == get_user