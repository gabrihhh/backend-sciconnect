from ninja import NinjaAPI, Body
from django.db import models,IntegrityError, DatabaseError

api = NinjaAPI()

class Usuario(models.Model):
    usuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)

    class Meta:
        db_table = 'usuarios' 
    
    def __str__(self):
        return self.username

#Post para criação do usuário
@api.post("/usuario")
def post_usuario(request, usuario: str = Body(...), senha: str = Body(...)):
    try:        
        usuario = Usuario(usuario=usuario, senha=senha)
        usuario.save()
        return {'message': 'Usuário criado com sucesso!'}
    except IntegrityError as e:
        return {
            'error': 'Erro de integridade',
            'message': str(e),
            'code': e.args[0]
        }
    except DatabaseError as e:
        return {
            'error': 'Erro de banco de dados',
            'message': str(e),
            'code': e.args[0]
        }
    except Exception as e:
        return {
            'error': 'Erro desconhecido',
            'message': str(e),
            'code': e.__class__.__name__
        }