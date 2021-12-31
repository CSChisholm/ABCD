# ABCD

Propagation of a gaussian beam through free space and an arbitrary configuration thin lenses using the ABCD formalism[^ref1].

Maxwell's equations give us the equation of motion for a propagatin gelectric field:

<img src="https://render.githubusercontent.com/render/math?math=\nabla^2E(\mathbf{r},t)-\frac{1}{c^2}\partial_t^2E(\mathbf{r},t) = 0-"><br> Under the assumption that <img src="https://render.githubusercontent.com/render/math?math=E(\mathbf{r},t) = \varepsilon(\mathbf{r})\exp{(ikz-i\omega t)}"> and <img src="https://render.githubusercontent.com/render/math?math=\partial_z^2\varepsilon_0(\mathbf{r})\exp{(ikz)} \approx \exp{(ikz)}\left[2ik\pderiv{}{z}\varepsilon_0(\mathbf{r}) - k^2\varepsilon_0(\mathbf{r})\right]"> we arrive at the Helmholtz equation

<img src="https://render.githubusercontent.com/render/math?math=\left(\nabla_T^2 + 2ik\partial_z\right)\varepsilon_0(\mathbf{r}) = 0">

From which, we find  the field:

<img src="https://render.githubusercontent.com/render/math?math=E(\mathbf{r},t) \propto \exp{\left[ik\frac{x^2+y^2}{2R(z)} - \frac{x^2+y^2}{w^2(z)}\right]}">
where <img src="https://render.githubusercontent.com/render/math?math=z_R = \pi w_0^2/\lambda"> is the Rayleigh range, <img src="https://render.githubusercontent.com/render/math?math=\varphi(z) = \arctan{(z/z_R)}"> is the Gouy phase, <img src="https://render.githubusercontent.com/render/math?math=R(z) = z_R^2/z + z"> is the radius of curvature of the wavefront, and <img src="https://render.githubusercontent.com/render/math?math=w(z) = w_0\sqrt{1 + (z/z_R)^2}"> is the radius of the beam.

We define the 'complex-q' parameter as
<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{q(z)} = \frac{1}{R(z)} + \frac{i\lambda}{\pi w^2(z)}.">

When the beam propagates through free space or a thin lens, it transforms according to
<img src="https://render.githubusercontent.com/render/math?math=q_f = (Aq_i + B)/(Cq_i + D)">

where

<img src="https://render.githubusercontent.com/render/math?math=\left(\begin{array}{cc} A & B \\ C & D\end{array}\right)} = \left(\begin{array}{cc} 1 & d \\ 0 & 1\end{array}\right)">

for propagation by a distance <img src="https://render.githubusercontent.com/render/math?math=d"> and

<img src="https://render.githubusercontent.com/render/math?math=\left(\begin{array}{cc} A & B \\ C & D\end{array}\right)} = \left(\begin{array}{cc} 1 & 0 \\ -1/f & 1\end{array}\right)">

for transmission through a thin lens with focal length <img src="https://render.githubusercontent.com/render/math?math=f.">

## Requirements
-numpy
-matplotlib

## To come

Propagation through thick lenses.

***References***

[^ref1]: P. W. Milonni and J. H. Eberly, **Lasers** (John Wiley and Sons, New York, 1988)
