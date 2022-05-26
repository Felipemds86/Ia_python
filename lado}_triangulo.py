classe Triângulo:
  def  __init __ ( self , lado1 , lado2 , lado3 , base , altura ) : #construtor
    próprio . lado1  = lado1
    próprio . lado2  = lado2
    próprio . lado3  = lado3
    próprio . base  = base
    próprio . altura  = altura
 
  def area ( self ) :
    return  ( self . base * self . altura ) / 2
  
  def tipo_triangulo ( self ) :
    se  auto . lado1  >  self . lado2 + self . lado3 :
      return  'Isso não é um triângulo!'
    ele  mesmo . lado1  ==  self . lado2  ou  self . lado1  ==  self . lado3  ou  self . lado2  ==  self . lado3 :
      voltar  'Triânculo isóceles'
    mais :
      return  'Triângulo de outro tipo'