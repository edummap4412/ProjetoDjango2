from django import forms
from django.core.mail.message import EmailMessage

from .models import  Produto, Produto3, Produto2

"""Depois que criei esse arquivo vou aprender a enviar email 
1) importar a biblioteca mail.message
2) Eu faço acesso ao post atraves do cleaned_data
logo em seguida  eu crio um metodo send email , novamente o cleaned_data é usado
para fazer acesso ao post

criei a variavel conteudo nela chamei um f-string com os valores
em seguida criei outra variavel chamada conteudo e passei a funcção EmailMessage
e fiz essa estrutura

mail = EmailMessage(subject= 'E-mail enviado pelo sistema django2',  # informação
                            body= conteudo, # no body coloquei a variavel conteudo
                            from_email= 'eduardomichael1@gmail.com', # em from_email e para qual email vai ser envidado
                            headers={'Reply To': email} # por fim aqui diz para qual email eu vou dar a resposta
                            to = é o email que vai receber
mail.send() # pega as configuracoes de email do "settings " e vai disparar o email
------ Ir para VIEWS ------
3) ir para viwes contato apagar tudo aquilo(que referece aos prints) e colocar 
form.send_mail()

------------------------ FAZENDO FORMS MODEL---------------
USADOPARA SALVAR AS INFORMAÇOES DE MODEL NO BANCO DE DADOS

"""


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',max_length= 100)
    email = forms.EmailField(label ='E-mail', max_length=100)
    assunto = forms.CharField(label ='Assunto', max_length=120)
    mensagem = forms.CharField(label ='Mensagem', widget=forms.Textarea())



    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\n Mensagem: {mensagem}'

        mail = EmailMessage(subject= 'E-mail enviado pelo sistema django2',
                            body= conteudo,
                            from_email= 'eduardomichael1@gmail.com',
                            to=['contato@Gmail.com',],
                            headers={'Reply-To': email}
        )
        mail.send()


class TesteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label ='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=120)
    mensagem = forms.CharField(label ='Mensagem', widget=forms.Textarea())


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']


class EmailForm(forms.Form):

    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\n Mensagem: {mensagem}'

    mail = EmailMessage(subject='E-mail enviado pelo sistema de Treino',
                        body=conteudo,
                        from_email='eduardomichael1@gmail.com',
                        to=['contato@Gmail.com', ],
                        headers={'Reply-To': email}
                        )
    mail.send()


class Produto3ModelForm(forms.ModelForm):
    class Meta:
        model = Produto3
        fields =['nome', 'preco', 'estoque', 'imagem']



class Produto2ModelForm(forms.ModelForm):
    class Meta:
        model = Produto2
        fields = ['nome', 'preco', 'estoque', 'imagem']
