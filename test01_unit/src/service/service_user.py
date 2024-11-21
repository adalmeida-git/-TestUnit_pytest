from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if isinstance(name, str) and isinstance(job, str):
            if not name or not job:
                return "Parametros inválidos"

            if self.search_user(name) is None:
                user = User(name,job)
                self.store.bd.append(user)
                return "Usuário adicionado"
            else:
                return "Usuário já existe"
        else:
            return "Não é string"

    def search_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None


    def remove_user(self, name,  job):
        if not name or not job:
            return "parametro vazio"

        if isinstance(name, str) and isinstance(job, str):
            if self.search_user(name) is not None:
                    user = self.search_user(name)
                    self.store.bd.remove(user)
                    return "Usuário removido"
            else:
                return "Usuário não existe"
        else:
            return "parametro inválidos"




    def update_user(self, name, new_name, job):
        if not name or not job:
            return "Variavel incorreta"

        if isinstance(name, str) and isinstance(job, str):
            if self.search_user(name) is not None:
                  self.search_user(name).name = new_name
                  return "Nome atualizado com sucesso"

            else:
                return "Nome não atualizado"
        else:
            return "Parametro incorreto"


    def get_user(self, name, job):
        if not name or not job:
            return "Vazio"
        if isinstance(name, str) and isinstance(job, str):
            if self.search_user(name) is not None:
                    job = self.search_user(name).job
                    return job
            else:
                return "Não encontrado"
        else:
            return "Parametro incorreto"

