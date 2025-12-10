# Exercice 1 : Analyse de suite et fonction

## 1. Étude de la fonction $f$

**(a) Calcul de la dérivée**
On considère la fonction définie sur $[0; 1]$ par $f(x) = 0,2 x e^{x^2}$.
C'est une forme $u \times v$ avec :
- $u(x) = 0,2x \implies u'(x) = 0,2$
- $v(x) = e^{x^2} \implies v'(x) = 2x e^{x^2}$ (dérivée composée $(e^u)' = u'e^u$)

$$f'(x) = u'(x)v(x) + u(x)v'(x)$$
$$f'(x) = 0,2 e^{x^2} + 0,2x (2x e^{x^2})$$
$$f'(x) = 0,2 e^{x^2} (1 + 2x^2)$$

Sachant que $0,2 = \frac{1}{5}$, on obtient bien :
$$f'(x) = \frac{1}{5}(1 + 2x^2)e^{x^2}$$

**(b) Tableau de variation sur $[0; 1]$**
- **Signe :** Pour tout $x \in [0; 1]$, $x^2 \geqslant 0$ donc $(1+2x^2)$ est strictement positif. La fonction exponentielle est toujours strictement positive. Donc $f'(x) > 0$.
- **Variation :** La fonction $f$ est strictement croissante sur l'intervalle.
- **Images aux bornes :**
  - $f(0) = 0,2 \times 0 \times e^0 = 0$
  - $f(1) = 0,2 \times 1 \times e^1 = 0,2e \approx 0,54$

| $x$ | $0$ | $\quad$ | $1$ |
|:---:|:---:|:---:|:---:|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $0$ | $\nearrow$ | $0,2e$ |

## 2. Raisonnement par récurrence
On souhaite démontrer que pour tout entier naturel $n$ : $0 \leqslant u_{n+1} \leqslant u_n \leqslant 1$.

* **Initialisation ($n=0$) :**
    $u_0 = 1$ et $u_1 = f(u_0) = f(1) = 0,2e \approx 0,54$.
    On constate que $0 \leqslant 0,54 \leqslant 1 \leqslant 1$.
    La propriété est vraie au rang $n=0$.

* **Hérédité :**
    Supposons que pour un entier $k$ fixé, $0 \leqslant u_{k+1} \leqslant u_k \leqslant 1$.
    La fonction $f$ étant **strictement croissante** sur $[0; 1]$, elle conserve l'ordre des inégalités :
    $$f(0) \leqslant f(u_{k+1}) \leqslant f(u_k) \leqslant f(1)$$
    Or :
    - $f(0)=0$
    - $f(u_{k+1}) = u_{k+2}$
    - $f(u_k) = u_{k+1}$
    - $f(1) \approx 0,54 \leqslant 1$
    
    On obtient donc : $0 \leqslant u_{k+2} \leqslant u_{k+1} \leqslant 1$.
    L'hérédité est démontrée.

* **Conclusion :** D'après le principe de récurrence, la propriété est vraie pour tout $n \in \mathbb{N}$.

## 3. Convergence
La suite $(u_n)$ est **décroissante** (car $u_{n+1} \leqslant u_n$ pour tout $n$) et **minorée** par 0 (car $u_n \geqslant 0$).
D'après le théorème de convergence monotone, la suite $(u_n)$ converge vers une limite $\ell$ telle que $0 \leqslant \ell \leqslant 1$.

## 4. Algorithmique (Python)

**(a) Justification**
On admet que $\ell = 0$. Par définition de la limite, pour tout réel $a > 0$, il existe un rang $n_0$ à partir duquel tous les termes de la suite sont strictement inférieurs à $a$ ($u_n \in [0; a[$). La fonction cherche ce premier rang $n_0$.

**(b) Script Python complété**
L'algorithme doit tourner tant que $u$ n'est pas passé sous le seuil $a$.

```python
from math import *

def seuil(a):
    u = 1
    n = 0
    while u >= a :        # Tant que u est supérieur ou égal au seuil a
        n = n + 1         # On passe au rang suivant
        u = 0.2 * u * exp(u**2) # Calcul du terme u_n+1 avec la formule de f(x)
    return(n)