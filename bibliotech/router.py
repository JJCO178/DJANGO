# Crea un archivo database_routers.py en tu proyecto
class SegundoDBRouter:
    modelos_externos = {"alumno", "docente"}  


    def db_for_read(self, model, **hints):
        if model._meta.model_name in self.modelos_externos:
            return "bd_externa"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name in self.modelos_externos:
            return "bd_externa"
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.modelos_externos:
            return db == "bd_externa"
        elif db == "bd_externa":
            return False
        return None
    
    
    