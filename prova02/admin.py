from django.contrib import admin
from prova02.models import Funcao
from prova02.models import Funcionario
from prova02.models import Horario
from prova02.models import Horario_trab_func
from prova02.models import Premiacao
from prova02.models import Diretor
from prova02.models import Genero
from prova02.models import Filme
from prova02.models import Filme_has_premiacao
from prova02.models import Filme_exibido_sala
from prova02.models import Sala

# Register your models here.
admin.site.register(Funcao)
admin.site.register(Funcionario)
admin.site.register(Horario)
admin.site.register(Horario_trab_func)
admin.site.register(Premiacao)
admin.site.register(Diretor)
admin.site.register(Genero)
admin.site.register(Filme)
admin.site.register(Filme_has_premiacao)
admin.site.register(Filme_exibido_sala)
admin.site.register(Sala)