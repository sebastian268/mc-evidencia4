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

![image](https://github.com/user-attachments/assets/31b6722e-2d42-4a2b-9990-af4d6a375fbf)


# Implementación del autómata en prolog

```prolog
% Definición de las transiciones del autómata
move(from,to,with).
move(a,b,a). 
move(a,b,b). 
move(a,b,c). 
move(a,b,d). 
move(a,b,e). 
move(a,b,f). 
move(a,b,g). 
move(a,b,h). 
move(a,b,i). 
move(a,b,j). 
move(a,b,k). 
move(a,b,l). 
move(a,b,m). 
move(a,b,n). 
move(a,b,ñ). 
move(a,b,o). 
move(a,b,p). 
move(a,b,q). 
move(a,b,r). 
move(a,b,s). 
move(a,b,t). 
move(a,b,u). 
move(a,b,v). 
move(a,b,w). 
move(a,b,x). 
move(a,b,y). 
move(a,b,z).

move(b,b,a). 
move(b,b,b). 
move(b,b,c). 
move(b,b,d). 
move(b,b,e). 
move(b,b,f). 
move(b,b,g). 
move(b,b,h). 
move(b,b,i). 
move(b,b,j). 
move(b,b,k). 
move(b,b,l). 
move(b,b,m). 
move(b,b,n). 
move(b,b,ñ). 
move(b,b,o). 
move(b,b,p). 
move(b,b,q). 
move(b,b,r). 
move(b,b,s). 
move(b,b,t). 
move(b,b,u). 
move(b,b,v). 
move(b,b,w). 
move(b,b,x). 
move(b,b,y). 
move(b,b,z).
 
move(b,c,'A'). 
move(b,c,'B'). 
move(b,c,'C'). 
move(b,c,'D'). 
move(b,c,'E'). 
move(b,c,'F'). 
move(b,c,'G'). 
move(b,c,'H'). 
move(b,c,'I'). 
move(b,c,'J'). 
move(b,c,'K'). 
move(b,c,'L'). 
move(b,c,'M'). 
move(b,c,'N'). 
move(b,c,'Ñ'). 
move(b,c,'O'). 
move(b,c,'P'). 
move(b,c,'Q'). 
move(b,c,'R'). 
move(b,c,'S'). 
move(b,c,'T'). 
move(b,c,'U'). 
move(b,c,'V'). 
move(b,c,'W'). 
move(b,c,'X'). 
move(b,c,'Y'). 
move(b,c,'Z').

move(c,c,a). 
move(c,c,b). 
move(c,c,c). 
move(c,c,d). 
move(c,c,e). 
move(c,c,f). 
move(c,c,g). 
move(c,c,h). 
move(c,c,i). 
move(c,c,j). 
move(c,c,k). 
move(c,c,l). 
move(c,c,m). 
move(c,c,n). 
move(c,c,ñ). 
move(c,c,o). 
move(c,c,p). 
move(c,c,q). 
move(c,c,r). 
move(c,c,s). 
move(c,c,t). 
move(c,c,u). 
move(c,c,v). 
move(c,c,w). 
move(c,c,x). 
move(c,c,y). 
move(c,c,z). 

move(c,e,'A'). 
move(c,c,'B'). 
move(c,c,'C'). 
move(c,c,'D'). 
move(c,c,'E'). 
move(c,c,'F'). 
move(c,c,'G'). 
move(c,c,'H'). 
move(c,c,'I'). 
move(c,c,'J'). 
move(c,c,'K'). 
move(c,c,'L'). 
move(c,c,'M'). 
move(c,c,'N'). 
move(c,c,'Ñ'). 
move(c,c,'O'). 
move(c,c,'P'). 
move(c,c,'Q'). 
move(c,c,'R'). 
move(c,c,'S'). 
move(c,c,'T'). 
move(c,c,'U'). 
move(c,c,'V'). 
move(c,c,'W'). 
move(c,c,'X'). 
move(c,c,'Y'). 
move(c,c,'Z').

move(c,e,0). 
move(c,e,1). 
move(c,e,2). 
move(c,e,3). 
move(c,e,4). 
move(c,e,5). 
move(c,e,6). 
move(c,e,7). 
move(c,e,8). 
move(c,e,9). 

move(b,d,0). 
move(b,d,1). 
move(b,d,2). 
move(b,d,3). 
move(b,d,4). 
move(b,d,5). 
move(b,d,6). 
move(b,d,7). 
move(b,d,8). 
move(b,d,9). 

move(d,d,0). 
move(d,d,1). 
move(d,d,2). 
move(d,d,3). 
move(d,d,4). 
move(d,d,5). 
move(d,d,6). 
move(d,d,7). 
move(d,d,8). 
move(d,d,9). 

move(d,d,a). 
move(d,d,b). 
move(d,d,c). 
move(d,d,d). 
move(d,d,e). 
move(d,d,f). 
move(d,d,g). 
move(d,d,h). 
move(d,d,i). 
move(d,d,j). 
move(d,d,k). 
move(d,d,l). 
move(d,d,m). 
move(d,d,n). 
move(d,d,ñ). 
move(d,d,o). 
move(d,d,p). 
move(d,d,q). 
move(d,d,r). 
move(d,d,s). 
move(d,d,t). 
move(d,d,u). 
move(d,d,v). 
move(d,d,w). 
move(d,d,x). 
move(d,d,y). 
move(d,d,z).

move(d,e,'A'). 
move(d,e,'B'). 
move(d,e,'C'). 
move(d,e,'D'). 
move(d,e,'E'). 
move(d,e,'F'). 
move(d,e,'G'). 
move(d,e,'H'). 
move(d,e,'I'). 
move(d,e,'J'). 
move(d,e,'K'). 
move(d,e,'L'). 
move(d,e,'M'). 
move(d,e,'N'). 
move(d,e,'Ñ'). 
move(d,e,'O'). 
move(d,e,'P'). 
move(d,e,'Q'). 
move(d,e,'R'). 
move(d,e,'S'). 
move(d,e,'T'). 
move(d,e,'U'). 
move(d,e,'V'). 
move(d,e,'W'). 
move(d,e,'X'). 
move(d,e,'Y'). 
move(d,e,'Z').

move(a,f,'A'). 
move(a,f,'B'). 
move(a,f,'C'). 
move(a,f,'D'). 
move(a,f,'E'). 
move(a,f,'F'). 
move(a,f,'G'). 
move(a,f,'H'). 
move(a,f,'I'). 
move(a,f,'J'). 
move(a,f,'K'). 
move(a,f,'L'). 
move(a,f,'M'). 
move(a,f,'N'). 
move(a,f,'Ñ'). 
move(a,f,'O'). 
move(a,f,'P'). 
move(a,f,'Q'). 
move(a,f,'R'). 
move(a,f,'S'). 
move(a,f,'T'). 
move(a,f,'U'). 
move(a,f,'V'). 
move(a,f,'W'). 
move(a,f,'X'). 
move(a,f,'Y'). 
move(a,f,'Z').

move(f,f,'A'). 
move(f,f,'B'). 
move(f,f,'C'). 
move(f,f,'D'). 
move(f,f,'E'). 
move(f,f,'F'). 
move(f,f,'G'). 
move(f,f,'H'). 
move(f,f,'I'). 
move(f,f,'J'). 
move(f,f,'K'). 
move(f,f,'L'). 
move(f,f,'M'). 
move(f,f,'N'). 
move(f,f,'Ñ'). 
move(f,f,'O'). 
move(f,f,'P'). 
move(f,f,'Q'). 
move(f,f,'R'). 
move(f,f,'S'). 
move(f,f,'T'). 
move(f,f,'U'). 
move(f,f,'V'). 
move(f,f,'W'). 
move(f,f,'X'). 
move(f,f,'Y'). 
move(f,f,'Z').

move(f,g,a). 
move(f,g,b). 
move(f,g,c). 
move(f,g,d). 
move(f,g,e). 
move(f,g,f). 
move(f,g,g). 
move(f,g,h). 
move(f,g,i). 
move(f,g,j). 
move(f,g,k). 
move(f,g,l). 
move(f,g,m). 
move(f,g,n). 
move(f,g,ñ). 
move(f,g,o). 
move(f,g,p). 
move(f,g,q). 
move(f,g,r). 
move(f,g,s). 
move(f,g,t). 
move(f,g,u). 
move(f,g,v). 
move(f,g,w). 
move(f,g,x). 
move(f,g,y). 
move(f,g,z).

move(g,g,a). 
move(g,g,b). 
move(g,g,c). 
move(g,g,d). 
move(g,g,e). 
move(g,g,f). 
move(g,g,g). 
move(g,g,h). 
move(g,g,i). 
move(g,g,j). 
move(g,g,k). 
move(g,g,l). 
move(g,g,m). 
move(g,g,n). 
move(g,g,ñ). 
move(g,g,o). 
move(g,g,p). 
move(g,g,q). 
move(g,g,r). 
move(g,g,s). 
move(g,g,t). 
move(g,g,u). 
move(g,g,v). 
move(g,g,w). 
move(g,g,x). 
move(g,g,y). 
move(g,g,z).

move(g,g,'A'). 
move(g,g,'B'). 
move(g,g,'C'). 
move(g,g,'D'). 
move(g,g,'E'). 
move(g,g,'F'). 
move(g,g,'G'). 
move(g,g,'H'). 
move(g,g,'I'). 
move(g,g,'J'). 
move(g,g,'K'). 
move(g,g,'L'). 
move(g,g,'M'). 
move(g,g,'N'). 
move(g,g,'Ñ'). 
move(g,g,'O'). 
move(g,g,'P'). 
move(g,g,'Q'). 
move(g,g,'R'). 
move(g,g,'S'). 
move(g,g,'T'). 
move(g,g,'U'). 
move(g,g,'V'). 
move(g,g,'W'). 
move(g,g,'X'). 
move(g,g,'Y'). 
move(g,g,'Z').

move(g,e,0). 
move(g,e,1). 
move(g,e,2). 
move(g,e,3). 
move(g,e,4). 
move(g,e,5). 
move(g,e,6). 
move(g,e,7). 
move(g,e,8). 
move(g,e,9). 

move(f,h,0). 
move(f,h,1). 
move(f,h,2). 
move(f,h,3). 
move(f,h,4). 
move(f,h,5). 
move(f,h,6). 
move(f,h,7). 
move(f,h,8). 
move(f,h,9). 

move(h,h,'A'). 
move(h,h,'B'). 
move(h,h,'C'). 
move(h,h,'D'). 
move(h,h,'E'). 
move(h,h,'F'). 
move(h,h,'G'). 
move(h,h,'H'). 
move(h,h,'I'). 
move(h,h,'J'). 
move(h,h,'K'). 
move(h,h,'L'). 
move(h,h,'M'). 
move(h,h,'N'). 
move(h,h,'Ñ'). 
move(h,h,'O'). 
move(h,h,'P'). 
move(h,h,'Q'). 
move(h,h,'R'). 
move(h,h,'S'). 
move(h,h,'T'). 
move(h,h,'U'). 
move(h,h,'V'). 
move(h,h,'W'). 
move(h,h,'X'). 
move(h,h,'Y'). 
move(h,h,'Z').

move(h,h,0). 
move(h,h,1). 
move(h,h,2). 
move(h,h,3). 
move(h,h,4). 
move(h,h,5). 
move(h,h,6). 
move(h,h,7). 
move(h,h,8). 
move(h,h,9). 

move(h,e,a). 
move(h,e,b). 
move(h,e,c). 
move(h,e,d). 
move(h,e,e). 
move(h,e,f). 
move(h,e,g). 
move(h,e,h). 
move(h,e,i). 
move(h,e,j). 
move(h,e,k). 
move(h,e,l). 
move(h,e,m). 
move(h,e,n). 
move(h,e,ñ). 
move(h,e,o). 
move(h,e,p). 
move(h,e,q). 
move(h,e,r). 
move(h,e,s). 
move(h,e,t). 
move(h,e,u). 
move(h,e,v). 
move(h,e,w). 
move(h,e,x). 
move(h,e,y). 
move(h,e,z).

move(a,i,0). 
move(a,i,1). 
move(a,i,2). 
move(a,i,3). 
move(a,i,4). 
move(a,i,5). 
move(a,i,6). 
move(a,i,7). 
move(a,i,8). 
move(a,i,9). 

move(i,i,0). 
move(i,i,1). 
move(i,i,2). 
move(i,i,3). 
move(i,i,4). 
move(i,i,5). 
move(i,i,6). 
move(i,i,7). 
move(i,i,8). 
move(i,i,9). 

move(i,k,a). 
move(i,k,b). 
move(i,k,c). 
move(i,k,d). 
move(i,k,e). 
move(i,k,f). 
move(i,k,g). 
move(i,k,h). 
move(i,k,i). 
move(i,k,j). 
move(i,k,k). 
move(i,k,l). 
move(i,k,m). 
move(i,k,n). 
move(i,k,ñ). 
move(i,k,o). 
move(i,k,p). 
move(i,k,q). 
move(i,k,r). 
move(i,k,s). 
move(i,k,t). 
move(i,k,u). 
move(i,k,v). 
move(i,k,w). 
move(i,k,x). 
move(i,k,y). 
move(i,k,z).

move(k,k,a). 
move(k,k,b). 
move(k,k,c). 
move(k,k,d). 
move(k,k,e). 
move(k,k,f). 
move(k,k,g). 
move(k,k,h). 
move(k,k,i). 
move(k,k,j). 
move(k,k,k). 
move(k,k,l). 
move(k,k,m). 
move(k,k,n). 
move(k,k,ñ). 
move(k,k,o). 
move(k,k,p). 
move(k,k,q). 
move(k,k,r). 
move(k,k,s). 
move(k,k,t). 
move(k,k,u). 
move(k,k,v). 
move(k,k,w). 
move(k,k,x). 
move(k,k,y). 
move(k,k,z).

move(k,k,0). 
move(k,k,1). 
move(k,k,2). 
move(k,k,3). 
move(k,k,4). 
move(k,k,5). 
move(k,k,6). 
move(k,k,7). 
move(k,k,8). 
move(k,k,9). 

move(i,j,'A'). 
move(i,j,'B'). 
move(i,j,'C'). 
move(i,j,'D'). 
move(i,j,'E'). 
move(i,j,'F'). 
move(i,j,'G'). 
move(i,j,'H'). 
move(i,j,'I'). 
move(i,j,'J'). 
move(i,j,'K'). 
move(i,j,'L'). 
move(i,j,'M'). 
move(i,j,'N'). 
move(i,j,'Ñ'). 
move(i,j,'O'). 
move(i,j,'P'). 
move(i,j,'Q'). 
move(i,j,'R'). 
move(i,j,'S'). 
move(i,j,'T'). 
move(i,j,'U'). 
move(i,j,'V'). 
move(i,j,'W'). 
move(i,j,'X'). 
move(i,j,'Y'). 
move(i,j,'Z').


move(j,j,0). 
move(j,j,1). 
move(j,j,2). 
move(j,j,3). 
move(j,j,4). 
move(j,j,5). 
move(j,j,6). 
move(j,j,7). 
move(j,j,8). 
move(j,j,9). 

move(j,j,'A'). 
move(j,j,'B'). 
move(j,j,'C'). 
move(j,j,'D'). 
move(j,j,'E'). 
move(j,j,'F'). 
move(j,j,'G'). 
move(j,j,'H'). 
move(j,j,'I'). 
move(j,j,'J'). 
move(j,j,'K'). 
move(j,j,'L'). 
move(j,j,'M'). 
move(j,j,'N'). 
move(j,j,'Ñ'). 
move(j,j,'O'). 
move(j,j,'P'). 
move(j,j,'Q'). 
move(j,j,'R'). 
move(j,j,'S'). 
move(j,j,'T'). 
move(j,j,'U'). 
move(j,j,'V'). 
move(j,j,'W'). 
move(j,j,'X'). 
move(j,j,'Y'). 
move(j,j,'Z'). 

move(j,e,a). 
move(j,e,b). 
move(j,e,c). 
move(j,e,d). 
move(j,e,e). 
move(j,e,f). 
move(j,e,g). 
move(j,e,h). 
move(j,e,i). 
move(j,e,j). 
move(j,e,k). 
move(j,e,l). 
move(j,e,m). 
move(j,e,n). 
move(j,e,ñ). 
move(j,e,o). 
move(j,e,p). 
move(j,e,q). 
move(j,e,r). 
move(j,e,s). 
move(j,e,t). 
move(j,e,u). 
move(j,e,v). 
move(j,e,w). 
move(j,e,x). 
move(j,e,y). 
move(j,e,z).

move(e,e,'A'). 
move(e,e,'B'). 
move(e,e,'C'). 
move(e,e,'D'). 
move(e,e,'E'). 
move(e,e,'F'). 
move(e,e,'G'). 
move(e,e,'H'). 
move(e,e,'I'). 
move(e,e,'J'). 
move(e,e,'K'). 
move(e,e,'L'). 
move(e,e,'M'). 
move(e,e,'N'). 
move(e,e,'Ñ'). 
move(e,e,'O'). 
move(e,e,'P'). 
move(e,e,'Q'). 
move(e,e,'R'). 
move(e,e,'S'). 
move(e,e,'T'). 
move(e,e,'U'). 
move(e,e,'V'). 
move(e,e,'W'). 
move(e,e,'X'). 
move(e,e,'Y'). 
move(e,e,'Z'). 

move(e,e,a). 
move(e,e,b). 
move(e,e,c). 
move(e,e,d). 
move(e,e,e). 
move(e,e,f). 
move(e,e,g). 
move(e,e,h). 
move(e,e,i). 
move(e,e,j). 
move(e,e,k). 
move(e,e,l). 
move(e,e,m). 
move(e,e,n). 
move(e,e,ñ). 
move(e,e,o). 
move(e,e,p). 
move(e,e,q). 
move(e,e,r). 
move(e,e,s). 
move(e,e,t). 
move(e,e,u). 
move(e,e,v). 
move(e,e,w). 
move(e,e,x). 
move(e,e,y). 
move(e,e,z).

move(e,e,0). 
move(e,e,1). 
move(e,e,2). 
move(e,e,3). 
move(e,e,4). 
move(e,e,5). 
move(e,e,6). 
move(e,e,7). 
move(e,e,8). 
move(e,e,9).

% Defnción de los estados finales
final(e).  


% Verificar si una secuencia de símbolos es aceptada por el autómata.
automata(Lista) :-
    aux_automata(Lista, a).  % Se inicia el autómata desde el estado 'a'.

% Caso base: Si la lista está vacía y el estado actual es final, se imprime que está dentro del lenguaje.
aux_automata([], EstadoActual) :-
    final(EstadoActual),  % Verifica si el estado final es alcanzado.
    write('La contraseña cumple con los requisitos'), nl.  % Si es un estado final, imprime 'Dentro del lenguaje'.

% Caso recursivo: Si hay más símbolos en la lista, se realiza una transición basada en el estado actual.
aux_automata([Sim|Res], EstadoActual) :-
    move(EstadoActual, EstadoSiguiente, Sim),  % Realiza la transición según el símbolo 'Sim'.
    aux_automata(Res, EstadoSiguiente).  % Llama recursivamente al autómata con el nuevo estado.
```

# ¿Cómo funciona?

La regla de los movimientos (cambios de estado) del autómata se encuntran definidos en la primera línea de código con el formato de "move (from,to,with)" por ejemplo, si la linea de código dice "move(a,b,b) significa que si el aútomata está en el estado "a", y recibe el simbolo "b" este hara un cambio de estado al estado "b" Siguiendo esta regla establecida, se procede a establecer todos los cambios de estado que pueden tomar lugar en el autómata.

Posteriormente se definen cuales son los estados de aceptación mediante la nomeclatura "final(caracter)" para establecer cuales son los estados en los que el autómata tiene un proceso de éxito, es decir, aquellos estados en los que, al terminar de procesar toda la cadena de entrada, el autómata acepta la palabra como válida. Esto significa que si, al finalizar el recorrido de la secuencia de símbolos, el autómata termina en uno de estos estados de aceptación, la cadena es considerada parte del lenguaje reconocido por el autómata. En este caso solo existe un estado en el que el el automata da como resultado valido, el cual es el estado "e"

# Resultados de la implementación 

![image](https://github.com/user-attachments/assets/0a197f97-d378-4632-8183-110677ff3fc0)


# Expresión regular 

Como hemos visto en clase, todo automáta tiene su forma de representarse mediante una expresión regular, la de este automata es la siguiente: 

r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]+'

pero... ¿cómo funciona esta expresión regular? bueno, esta expresión funciona con ayuda de lo que se conoce como lookahead, el cual se encarga de confirmar sí dentro de una cadena hay existencia de lo que esta "buscando" por lo que para dar verdadero, en esta debe existir al menos una mayúscula, una minúscula y un número.

Además la parte de "[A-Za-z\d]" limita a que solo puedan existir esos cáracteres, evitando así el uso de cáracteres no previstos.

# Fuente sobre los lookahead

Lookahead assertion: (?=. . .), (?!. . .) - JavaScript | MDN. (2024, 25 noviembre). MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion


# Implemtenación del regex 

![Captura de Pantalla 2025-05-23 a la(s) 11 24 00 p m](https://github.com/user-attachments/assets/6c14cdb4-05b7-4c1e-bb0f-13f9c374c34e)

El código funciona mediante un ciclo que le permite al usuario ingresar cadenas para validad si su contraseña cumple o no cumple con los requisitos. Esta implementado en python.

# Complejidad del sistema.

El sistema tiene un nivel de complejidad de **O(n)** debido a que en este, a pesar de la recursión, siempre realiza las iteraciones caracter por caracter, por lo que realiza una función a la vez, es decir, solo procesa un elemento por iteración; Y al no haber ciclos dentro de otro ciclo no se generan múltiples llamadas simultáneas que incrementen la complejidad del sistema. Por lo que se podría decir que el rendimiento del algoritmo depende totalmente de la longitud de la lista que recibe la función y no de la cantidad de operaciones que tiene que realizar al mismo timpo.

# Tipo de autómata 

El tipo de autómata es determinista debido a que no hay estados con múltiples transiciones con el mismo símbolo.

# Conclusión.

Si bien el autómata puede ser útil para estas situaciones sencillas, cuando la situación se torna más complicada deja de ser viable debido a su falta de memoria, como por ejemplo, en este caso no es capaz de verificar la longitud de la contraseña. Por lo que hay situaciones en las que es importante contar con una memoria capaz de guardar los sucesos.

# Referencias 

Lookahead assertion: (?=. . .), (?!. . .) - JavaScript | MDN. (2024, 25 noviembre). MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion

Kantor, I. (s. f.). Lookahead y lookbehind (revisar delante/detrás). https://es.javascript.info/regexp-lookahead-lookbehind
