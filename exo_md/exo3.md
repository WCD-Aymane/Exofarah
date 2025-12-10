# Exercice 3 : Le Cube

On considère un cube $ABCDEFGH$.
On munit l'espace du repère $(A; \vec{AB}, \vec{AD}, \vec{AE})$.
Les coordonnées des sommets sont donc :
$A(0,0,0), B(1,0,0), C(1,1,0), D(0,1,0), E(0,0,1), F(1,0,1), G(1,1,1), H(0,1,1)$.

## 1. Coordonnées de F
Par définition du repère et du cube : $\vec{AF} = \vec{AB} + \vec{AE}$.
Dans le repère, cela correspond à $1\vec{AB} + 0\vec{AD} + 1\vec{AE}$.
Donc **$F(1; 0; 1)$**.

## 2. Coordonnées de K
L'énoncé corrigé définit $K$ par : $\vec{AK} = 2\vec{AH}$.
Or, $\vec{AH} = \vec{AD} + \vec{AE}$, donc ses coordonnées sont $(0; 1; 1)$.
Ainsi, $\vec{AK} = 2 \times (0; 1; 1) = (0; 2; 2)$.
Les coordonnées de $K$ sont **$K(0; 2; 2)$**.

## 3. Vérification du milieu L
Soit $L(0,5; 1; 1,5)$. Vérifions si $L$ est le milieu du segment $[FK]$.
Formule du milieu : $M(\frac{x_F+x_K}{2} ; \frac{y_F+y_K}{2} ; \frac{z_F+z_K}{2})$.
- $x_L = \frac{1 + 0}{2} = 0,5$. (Correct)
- $y_L = \frac{0 + 2}{2} = 1$. (Correct)
- $z_L = \frac{1 + 2}{2} = 1,5$. (Correct)
Le point **L est bien le milieu de [FK]**.

## 4. Représentation paramétrique de la droite (FK)
La droite passe par $F(1; 0; 1)$.
Son vecteur directeur est $\vec{FK}(x_K-x_F; y_K-y_F; z_K-z_F)$.
$\vec{FK}(0-1; 2-0; 2-1) \implies \vec{FK}(-1; 2; 1)$.

La représentation paramétrique est donc :
$$
\begin{cases} 
x = 1 - t \\ 
y = 0 + 2t = 2t \\ 
z = 1 + t 
\end{cases} 
\quad, t \in \mathbb{R}
$$

## 5. Intersection de la droite (FK) et du plan (ABC)
Dans le repère choisi $(A; \vec{AB}, \vec{AD}, \vec{AE})$, le plan $(ABC)$ correspond à la face du bas du cube.
L'équation cartésienne du plan $(ABC)$ est simplement **$z = 0$**.

Pour trouver le point d'intersection $M$, on cherche le paramètre $t$ tel que la coordonnée $z$ de la droite (FK) soit nulle :
$z = 0 \iff 1 + t = 0 \iff t = -1$.

On remplace $t = -1$ dans les expressions de $x$ et $y$ de la droite (FK) :
- $x = 1 - (-1) = 2$
- $y = 2 \times (-1) = -2$
- $z = 0$

Les coordonnées du point d'intersection $M$ sont **$M(2; -2; 0)$**.