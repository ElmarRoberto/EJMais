# EJMais

## 1. O Software

Este software tem como objetivo auxiliar na gestão de tarefas de Empresas Juniores, tornando a gerência de atividades mais fácil e atrativa. Para tal fim, serão utilizados métodos de gamificação, nos quais estão descritos neste [Plano de Gamificação](https://stebezs.github.io/ejmais.github.io/).

## 2. Configurando o Ambiente

Siga os passos no terminal:
**OBS:** Configurações garantidas para Linux 64 bits.  

**Passo 1**
Cheque se vocë já tem o Python instalado na sua máquina:  
      ``$ python3 --version``  

**Passo 2**  
Se não tiver, execute para python 3.4 ou superior:  
**Ubuntu**
      ``$ sudo apt-get install python3.4``  

Feito isso, é necessário instalar o "virtual environment" (**virtualenv**).  

**Passo 3**  
Cheque se vocë já possui o virtualenv:  
	``$ virtualenv --version``  
	
**Passo 4**  
Se vc não tiver, execute:  
	``$ sudo apt-get install python-virtualenv``  

Feito, com o virtualenv instalado podemos continuar.  

**Passo 5**  
Crie uma pasta (any name):  
	``$ mkdir gamificacao``  
Acesse a pasta:  
	``$ cd gamificacao``  
Agora vamos criar um ambiente virtual chamado amb_vir_gami(any name), com isso:  
	``python3 -m venv amb_vir_gami``  

**Passo 6**  
Feito isso, note que você terá um novo diretório chamado amb_vir_gami.  
Execute o comando:  
	``$ source amb_vir_gami/bin/activate``  

Para encerrar esse passo, seu terminal deve estar parecido com a linha abaixo:  
	``(amb_vir_gami) ~/gamificacao $``  

**Passo 7**  
Agora, dentro do ambiente virtual do virtualenv instale as dependências do projeto:  
	``(amb_vir_gami) ~$ pip install -r requirements``  

OBS.: se você não tiver o pip instalado, rode o comando:  
        ``apt-get install python-pip``  

E para ter a última versão execute:   
        ``pip install -U pip``
ou 
        ``pip install --upgrade pip`` 
 
Pronto! Seu ambiente de desenvolvimento está configurado.    

**Saindo do ambiente virtual**  
Se você precisar sair do seu ambiente virtual basta usar esse comando:  
        ``(amb_vir_gami) ~$ deactivate``  

Assim, seu terminal deve parecer algo dessa forma:  
         ``~$``
