from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect


from .forms import ContatoForm, TesteForm, EmailForm , ProdutoModelForm, Produto3ModelForm, Produto2ModelForm
from .models import Produto, Produto2
"""
1)ContatoFrom vem do 'Forms' e se aplica nesse as mesmas regras que um model , 
importando e trazendo aqui pra views , determinando uma instacia 'form' e chamando a classe ContatoForm e 
depois jogando no context
---------------CRIANDO VALIDAÇÃO--------------
2) Através da condicional que aprendi a criar. usando o 'if str(request.method) == "POST":' junto com if form>is_valid():
VALIDA-SE TODOS OS DADOS INSERIDO NO FINAL coloquei messages.sucesses para me enviar uma mensagem , pra isso precisei importar
a biblioteca django.contrib import messages .e por fim coloquei a instancia form = ContatoFrom() sem parametros para apagar os dados inseridos
para inserção de outros
--------------Explicando a estrutura usada--------
form = TesteForm(request.POST or None)# com essa condição diz que ele pode ter dados ou vazio
    if str(request.method) == 'POST': # aqui eu quero saber se ele é post , chamando request.method
    if form.is_valid(): #aqui eu quero saber se ele é valido
        nome = form.cleaned_data['nome'] # aqui peguei os dados, os nome que inseri lá
        email = form.cleaned_data['email']
        assunto = form.cleaned_data['assunto']
        mensagem = form.cleaned_data['mensagem']
        # PRINT é para arecer no console
------NÃO ESQUECER DE IMPORTAR AS BIBLIOTECAS------
from django.contrib import messages

from .forms import ContatoForm, TesteForm, EmailForm , ProdutoModelForm

------- Confirmando se usuario te acesso------

eu adicionei uma condicional if no produto e coloquei como parametro 'AnonymousUser'
se  ele for anonimous . vou no else  e o mandrei devolta para o ('index) usando  o
redirect , para isso vou importar  djando shortcuts import  redirect

"""

def index(request):

    context = {
        'produtos':Produto.objects.all()
    }
   
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            form.send_mail()
            messages.success(request,'E-mail enviado com sucesso')
            form = ContatoForm()

        else:
            messages.error(request,'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

# Esse é para os MODELS FORM

def produto(request):

    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:

            form = ProdutoModelForm()
        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('index')



def treino(request):
    form = TesteForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f' Nome:{nome}')
            print(f' email:{email}')
            print(f' assunto :{assunto}')
            print(f' mensagem:{mensagem}')

        messages.success(request,'Mensagem enviada com sucesso')
        form= TesteForm()
    else:
        messages.error(request, 'Erro ao enviar mensagem')
    context = {
        'form': form
    }
    return render(request, 'treino.html', context)




def treino_email(request):
    form = EmailForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            messages.success(request, 'Messagem foi enviada')
            form = EmailForm()
        else:
            messages.error(request,'Falha ao enviar a mensagem')
    context= {
        'form': form
    }
    return render(request, 'treinoemail.html',context)



def produto3(request):

    if str(request.method) == 'POST':
        form = Produto3ModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()



            messages.success(request, 'Produto envidado com Sucesso')
            form = Produto3ModelForm()
        else:
            messages.error(request, 'Erro ao salvar o  produto')
    else:
        form = Produto3ModelForm()

    context = {
        'form': form
    }
    return render(request, 'produto3.html', context)


def produto2(request):

    if str(request.method) == 'POST':
        formu =Produto2ModelForm(request.POST,request.FILES)
        if formu.is_valid():
            formu.save()
            messages.success(request,"Produto cadastrado com sucesso com sucesso")
            formu = Produto2ModelForm()
        else:
            messages.error(request, "Falha ao enviar ! Verifique os campos")
    else:

        formu =Produto2ModelForm()
    context = {
        'formulario': formu
    }


    return render(request,'produto2.html', context)