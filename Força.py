import random
import webbrowser
def jogar():
    print("=========")
    print("bem_vindo jogo da forca")
    print("voce so tem apenas 6 tentativas")
    print("==========")
    nomes= ["banana","gaveta","janela","violao","abajur","buzina"]
    random.shuffle(nomes)
    escolha = random.choice(nomes)
    palavra_secreta= (escolha)
    acertos= ["_","_","_","_","_","_"]
    erros = 0
    acertou = False
    forca= False
    while not forca  and not acertou:
          chute=input("qual e a letra: ")
          if chute in palavra_secreta:
             posicao= 0
             for letra in escolha:
                 if chute.upper() == letra.upper():
                    acertos[posicao] = letra
                 posicao = posicao +1
          else:
             erros+= 1 
             forca = erros == 6
             acertou=("_" not in  acertos)
             print(acertos)
jogar()
print("fim")
print("==============")
print("deseja ver quem criou jogo ")
opcao=input("sim/nao: ")
opcao.upper()
if opcao.upper() =="SIM" or opcao.upper()=="S":
   print('''[1]-Facebook
[2]-Istagram
[3]-Kwai
[4]-github''')
   rede=input("qual voce deseja: ")
   if rede =="1" or rede=="02":
      new =2
      url="https://www.facebook.com/profile.php?id=100065500847251"
      webbrowser.open(url,new=new)
   elif rede =="02" or rede =="2":
      new=2
      url="https://www.instagram.com/reel/Ckwhf2AgVLB/?igshid=MDM4ZDc5MmU="
      webbrowser.open(url,new=new)
   elif rede=="4" or rede=="04":
   	   new=2
   	   url="https://github.com/Mundoprogramador"
   	   webbrowser.open(url,new=new)
   elif rede =="3" or rede=="03":
         new=2
         url="https://kwai-video.com/u/@charles_silva015/CNpvN5vp"
         webbrowser.open(url,new=new)
   else:
       print("opçao invalida")
print("fim")
