# Exercice 2 : Géométrie dans l'espace

Données : Repère $(O; \vec{i}, \vec{j}, \vec{k})$.
Points : $A(-3; 2; 2)$, $B(0; 3; 3)$, $C(-2; 3; 1)$ et $D(4; 3; 10)$.

## 1. Positions relatives

**(a) Alignement des points A, B, C**
Calculons les vecteurs :
- $\vec{AB} (0 - (-3); 3-2; 3-2) \implies \vec{AB}(3; 1; 1)$
- $\vec{AC} (-2 - (-3); 3-2; 1-2) \implies \vec{AC}(1; 1; -1)$

Il n'existe pas de réel $k$ unique tel que $\vec{AB} = k\vec{AC}$.
(Pour les abscisses $3 = k \times 1 \implies k=3$, mais pour les ordonnées $1 = k \times 1 \implies k=1$).
Les vecteurs ne sont pas colinéaires, donc les points **A, B et C ne sont pas alignés**.

**(b) Coplanarité des vecteurs**
Calculons $\vec{AD}(4 - (-3); 3-2; 10-2) \implies \vec{AD}(7; 1; 8)$.
On cherche deux réels $x$ et $y$ tels que $\vec{AD} = x\vec{AB} + y\vec{AC}$.
Cela donne le système :
$$
\begin{cases} 
3x + y = 7 \\ 
x + y = 1 \\ 
x - y = 8 
\end{cases}
$$
En additionnant les deux dernières lignes : $2x = 9 \implies x = 4,5$.
En remplaçant dans la deuxième ligne : $4,5 + y = 1 \implies y = -3,5$.
Vérifions dans la première ligne : $3(4,5) + (-3,5) = 13,5 - 3,5 = 10$.
Or, on attendait 7. Le système est incompatible.
Les vecteurs $\vec{AB}$, $\vec{AC}$ et $\vec{AD}$ ne sont **pas coplanaires**.

**(c) Position relative de (AD) et (ABC)**
Comme les vecteurs ne sont pas coplanaires, le point D n'appartient pas au plan (ABC). La droite (AD) n'est ni incluse ni parallèle au plan (ABC).
La droite (AD) et le plan (ABC) sont donc **sécants** (en un point unique, qui est le point A).

## 2. Représentation paramétrique

**(a) Droite (AD)**
La droite passe par $A(-3; 2; 2)$ et a pour vecteur directeur $\vec{AD}(7; 1; 8)$.
$$
\begin{cases} 
x = -3 + 7t \\ 
y = 2 + t \\ 
z = 2 + 8t 
\end{cases} 
\quad, t \in \mathbb{R}
$$

**(b) Appartenance du point M**
Soit $M(-\frac{19}{4}; \frac{7}{4}; 0)$. Appartient-il à (AD) ?
On résout l'équation sur $z$ : $2 + 8t = 0 \implies 8t = -2 \implies t = -0,25$.
On vérifie les autres coordonnées avec $t = -0,25$ :
- $x = -3 + 7(-0,25) = -3 - 1,75 = -4,75$. Or $-\frac{19}{4} = -4,75$. (Vrai)
- $y = 2 + (-0,25) = 1,75$. Or $\frac{7}{4} = 1,75$. (Vrai)
Le point M **appartient** à la droite (AD).

## 3. Intersection de droites

Soit la droite $(d)$ définie par :
$$
\begin{cases} 
x = -2 - 2k \\ 
y = -3 + k \\ 
z = -6 
\end{cases}
\quad, k \in \mathbb{R}
$$

**(a) Un point appartenant à (d)**
En prenant $k=0$, on obtient le point $P(-2; -3; -6)$.

**(b) Un vecteur directeur de (d)**
On lit les coefficients devant le paramètre $k$ : $\vec{u}(-2; 1; 0)$.

**(c) Intersection des droites (AD) et (d)**
On cherche s'il existe un couple $(t, k)$ vérifiant le système :
$$
\begin{cases} 
-3 + 7t = -2 - 2k \quad (1) \\ 
2 + t = -3 + k \quad \quad (2) \\ 
2 + 8t = -6 \quad \quad \quad (3)
\end{cases}
$$
D'après (3) : $8t = -8 \implies t = -1$.
On remplace $t$ dans (2) : $2 + (-1) = -3 + k \implies 1 = -3 + k \implies k = 4$.
On vérifie la compatibilité dans (1) :
- Membre de gauche : $-3 + 7(-1) = -10$.
- Membre de droite : $-2 - 2(4) = -2 - 8 = -10$.
L'égalité est vérifiée. Les droites sont sécantes.

Pour trouver les coordonnées du point d'intersection $I$, on remplace $t=-1$ dans la paramétrique de (AD) :
- $x = -3 - 7 = -10$
- $y = 2 - 1 = 1$
- $z = 2 - 8 = -6$
Les droites sont sécantes au point **$M(-10; 1; -6)$** (Note: l'énoncé l'appelle M, mais pour éviter la confusion avec la question 2b, notons-le point d'intersection).