# Mathematical Derivation 

## Calculus Background

**Laplacian Operator:**

$$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

**Gradient Operator:**

$$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right) = \frac{\partial f}{\partial x} \hat{i} + \frac{\partial f}{\partial y} \hat{j} + \frac{\partial f}{\partial z} \hat{k}$$

## Crater Diffusion 

$$\frac{\partial h}{\partial t} = \kappa \left(\frac{\partial^2 h}{\partial x^2} + \frac{\partial^2 h}{\partial y^2}\right)$$

$$\implies \frac{\partial h}{\partial t} = \kappa \nabla^2 h$$

where $h(x,y,t)$ is the surface elevation, $t$ is the time, and $\kappa$ is the hillslope transport coefficient.

To solve numerically, we can discretize the continuous domain into a grid with spatial steps $\Delta x$ and $\Delta y$ and a time step $\Delta t$.

Using a Forward-Time Central-Space (FTCS) finite difference scheme, the spatial second derivatives (the Laplacian $\nabla^2 h$) at a grid cell $(i,j)$ are approximated:

$$\frac{\partial^2 h}{\partial x^2} \approx \frac{h_{i+1,j} - 2h_{i,j} + h_{i-1,j}}{\Delta x^2}$$

$$\frac{\partial^2 h}{\partial y^2} \approx \frac{h_{i,j+1} - 2h_{i,j} + h_{i,j-1}}{\Delta y^2}$$

## Discretize the Time Derivative 

Approximating the time derivative:

$$\frac{\partial h}{\partial t} \approx \frac{h_{i,j}^{n+1} - h_{i,j}^{n}}{\Delta t}$$

$$\frac{h_{i,j}^{n+1} - h_{i,j}^{n}}{\Delta t} \approx \kappa \left( \frac{h_{i+1,j}^{n} - 2h_{i,j}^n + h_{i-1,j}^n}{\Delta x^2} + \frac{h_{i,j-1}^{n} - 2h_{i,j}^n + h_{i,j+1}^n}{\Delta y^2} \right)$$

$$h_{i,j}^{n+1} = h_{i,j}^{n} + \kappa\Delta t \left( \frac{h_{i+1,j}^{n} - 2h_{i,j}^n + h_{i-1,j}^n}{\Delta x^2} + \frac{h_{i,j-1}^{n} - 2h_{i,j}^n + h_{i,j+1}^n}{\Delta y^2} \right)$$

**NOTE:** This means that to find the elevation of a pixel tomorrow (later $t$), take the elevation today ($t$), and add or subtract material based on how much higher or lower it is compared to its immediate neighbors, scaled by the diffusion coefficient and the time step size (i.e., $\kappa \Delta t$).
