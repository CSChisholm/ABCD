# ABCD

Propagation of a gaussian beam through free space and an arbitrary configuration thin lenses using the ABCD formalism[^ref1].

Maxwell's equations give us the equation of motion for a propagatin gelectric field: $\nabla^2E(\mathbf{r},t)-\frac{1}{c^2}\pderiv[2]{}{t}E(\mathbf{r},t) = 0$. Under the assumption that $E(\mathbf{r},t) = \varepsilon(\mathbf{r})\exp{(ikz-i\omega t)}$ and $\pderiv[2]{}{z}\varepsilon_0(\mathbf{r})\exp{(ikz)} \approx \exp{(ikz)}\left[2ik\pderiv{}{z}\varepsilon_0(\mathbf{r}) - k^2\varepsilon_0(\mathbf{r})\right]$ we arrive at the Helmholtz equation
$$\left(\nabla_T^2 + 2ik\pderiv{}{z}\right)\varepsilon_0(\mathbf{r}) = 0$$

From which, we find  the field:
$$E(\mathbf{r},t) \propto \exp{\left[ik\frac{x^2+y^2}{2R(z)} - \frac{x^2+y^2}{w^2(z)}\right]}$$
where $z_R = \pi w_0^2/\lambda$ is the Rayleigh range, $\varphi(z) = \arctan{(z/z_R)}$ is the Gouy phase, $R(z) = z_R^2/z + z$ is the radius of curvature of the wavefront, and $w(z) = w_0\sqrt{1 + (z/z_R)^2}$ is the radius of the beam.

We define the 'complex-q' parameter as
$$\frac{1}{q(z)} = \frac{1}{R(z)} + \frac{i\lambda}{\pi w^2(z)}.$$
When the beam propagates through free space or a thin lens, it transforms according to $q_f = (Aq_i + B)/(Cq_i + D)$ where
$$\left(\begin{array}{cc} A & B \\ C & D\end{array}\right)} = \left(\begin{array}{cc} 1 & d \\ 0 & 1\end{array}\right)$$
for propagation by a distance $d$ and 
$$\left(\begin{array}{cc} A & B \\ C & D\end{array}\right)} = \left(\begin{array}{cc} 1 & 0 \\ -1/f & 1\end{array}\right)$$
for transmission through a thin lens with focal length $f$.

## Requirements
-numpy
-matplotlib

[ref1]: P. W. Milonni and J. H. Eberly, **Lasers** (John Wiley and Sons, New York, 1988)
