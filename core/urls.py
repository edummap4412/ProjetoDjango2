from django.urls import path
from .views import index, contato, produto, treino, treino_email ,produto3 , produto2



urlpatterns =[
    path('', index, name='index'),
    path('contato/', contato, name ='contato'),
    path('produto/', produto, name= 'produto'),
    path('treino/', treino, name='treino'),
    path('treinoemail', treino_email, name='treinoemail'),
    path('produtos', produto3, name= 'testeproduto'),
    path('xuxa', produto2, name='produtodois')
]

