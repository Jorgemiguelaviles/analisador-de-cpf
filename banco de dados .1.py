clientes=[]
def bancodedados ():
	c={}
	c['nome']=input('escreva seu nome')
	c['cpf']=input('digite o cpf')
	c['endereco']=input('digite o endereço')
	c['idade']=input('digite sua idade')
	return c

clientes={}
clientes['cl1']=bancodedados()
clientes['cl2']=bancodedados()
clientes['cl3']=bancodedados()
print(clientes)