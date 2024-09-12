import os, environs
from pathlib import Path

class ENV:
    # Creado por Neil Yesikov Cuadros Miraval 👈(ﾟヮﾟ👈)
    # Esta clase permite leer y obtener variables del archivo .env

    env=environs.Env()
    env.read_env( path=os.path.join( Path(__file__).resolve().parent.parent, '.env' ), override=True )


    @classmethod
    def debug(self): return bool(self.env.bool('DEBUG'))


    @classmethod
    def secret_key(self): return str(self.env.str('SECRET_KEY'))


    @classmethod
    def bridge(self): return str(self.env.str('BRIDGE'))

    @classmethod
    def local(self): return bool(self.env.bool('LOCAL'))

    @classmethod
    def host(self):
        if self.debug() == False:
            app_list: list[str] = []
            for i in list(range(1, self.env.int('HOST_L') + 1)):
                app_list.append(self.env.str('HOST_{}'.format(i)))
            return app_list
        else: return []


    @classmethod
    def cors(self):
        if self.debug() == False:
            app_list: list[str] = []
            for i in list(range(1, self.env.int('CORS_L') + 1)):
                app_list.append(self.env.str('CORS_{}'.format(i)))
            return app_list
        else: return []


    @classmethod
    def connections(self):
        """crea un objeto en base a la longitud: ``TENANT_L`` -> {``DATABASE_N``: ``CONNECTION_N``} """
        connections = {}
        for i in list(range(1, self.env.int('TENANT_L') + 1)):
            connections[self.env.str('TENANT_{}'.format(i))] = self.env.dj_db_url('DATABASE_{}'.format(i))
        # print(connections)
        return connections


    @classmethod
    def databases(self):
        """Ontiene la lista completa de bases de datos [``default``, ``[str...]``] """
        databases: list[str] = []
        for i in list(range(1, self.env.int('TENANT_L') + 1)):
            databases.append(self.env.str('TENANT_{}'.format(i)))
        return databases


    @classmethod
    def countries(self):
        """Retorna la lista de bases de datos menos default ``[str...]`` """
        countries: list[str] = []
        for database in self.databases():
            if database != "default" : countries.append(database)
        return countries


    @classmethod
    def apps(self):
        """Obtiene una lista symple de aplicaciones ``[str...]`` """
        app_list: list[str] = []
        for i in list(range(1, self.env.int('APP_L') + 1)):
            app_list.append(self.env.str('APP_{}'.format(i)))
        return app_list


    @classmethod
    def apps_for_settings(self):
        """Obtiene una lista de aplicaciones para ser importada``[str...]`` """
        app_list: list[str] = []
        for i in list(range(1, self.env.int('APP_L') + 1)):
            app_list.append("apps.{}".format(self.env.str('APP_{}'.format(i))))
        return app_list