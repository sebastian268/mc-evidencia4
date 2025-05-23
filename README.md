# mc-evidencia4

# Sebastián Acosta Marín 
# A01278278 

# ¿Qué problematica resolví?

el autómata que desarrollé sirve para confirmar si una contraseña cumple con el siguiente formato:
- Un número
- Una minúscula
- Una mayúscula 

# ¿Qué tipo de autómata es? 

Mi autómata es del tipo AFD (Autómata Finito Determinista) el cual como su nombre lo indica es determinista y no da lugar a ambigüedades; esto se debe a que por cada estado en el que se encuentre el automata, solo existe un movimiento de cambio posible con un simbolo, es decir, no existen diferente movimientos con el mismo simbolo o caracter. "para cada estado en que se encuentre el autómata, y con cualquier símbolo del alfabeto leído, existe siempre no más de una transición posible desde ese estado y con ese símbolo." (colaboradores de Wikipedia, 2019) Esto significa que el automáta no tiene dos caminos posibles con el mismo simbolo.

# Alfabeto del autómata 

El alfabeto es un aspecto muy importante a considerar dentro de un autómata debido a que al momento de implementarlo este solo funciona con el alfabeto establecido. Tomando esto en cuenta, el afabeto con el que funciona este automata es el siguiente:

Σ = a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9

Es decir: 
- Todos los números
- Todas las minúsculas
- Todas las mayúsculas

# Autómata diseñado 

![image]
