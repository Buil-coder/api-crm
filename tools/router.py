from tools.env import ENV

class empresaUno_router(object):
    route_app_labels = ENV.apps()

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels: return ENV.countries()[0]
        print(ENV.countries())  # Debería mostrar una lista con al menos 'empresaUno'

        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels: return ENV.countries()[0]
        print(ENV.countries())  # Debería mostrar una lista con al menos 'empresaUno'

        return None

    def allow_relation(self, obj1, obj2, **hints): return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels: return db
        return None