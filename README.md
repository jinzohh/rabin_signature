# Square Rooting of Modular Equations
The modular equation, $a$ mod $m$ can be square rooted such that $x^2$ = $a$ mod $m$, where $m = pq$.
It involves finding the roots of $a$ mod $p$ and $a$ mod $q$, separately. The result is usually a set of 4 roots {$root_1$, $root_2$, $root_3$, $root_4$}.

### Hoffstein's Proposition
Let $p$ be a prime such that $p\equiv 3\pmod{4}$. Let $a$ be an integer such that the congruence $x^2 \equiv a\pmod{p}$ has a solution; i.e. that $a$ has a square root modulo $p$. Then, $b \equiv a^{(p+1)/4}\pmod{p}$ is a square root of $a\pmod{p}$.
The Hoffstein's proposition, if it can apply, helps to calculate the roots more quickly.

### Rabin's Cryptosystem
The Rabin's Cryptosystem is based on the square rooting principles of modular equations.
The private key is (p, q), which are factors of N. The message is encrypted by squaring $m$ mod $N$. It is decrypted by taking the square root of $m$ mod $N$, or rather, $m$ mod $pq$. So, if p and q are not known, it cannot be decrypted.
