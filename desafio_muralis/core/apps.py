import datetime
import fnmatch
import os

from django.apps import AppConfig

from desafio_muralis.settings import BASE_DIR


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'desafio_muralis.core'

    def find(self, pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    def ready(self):
        nomes_arquivos = [
            f"{datetime.datetime.now().strftime('%Y-%m-%d')}",
            f"{(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')}",
            f"{(datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')}",
        ]
        for arquivo in os.listdir(f"{BASE_DIR}/logs/"):
            data_arquivo = arquivo.split(".log")
            if data_arquivo[0] not in nomes_arquivos:
                os.remove(f"{BASE_DIR}/logs/{arquivo}")
