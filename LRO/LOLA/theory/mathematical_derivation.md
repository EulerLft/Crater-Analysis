# Mathematical Derivation 

## Calculus Background

<b> Laplacian Operator <br> : <br> 

$\nabla^2f  = \frac{\partial^2f}{\partial x^2} + \frac{\partial^2f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}\nabla ^2 f = \frac{\partial}$ <br> 

<b> Gradient Operator <b> : <br> 

$\nabla f  =(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})$ <br> 
	   = $\nabla f  =(\frac{\partial f}{\partial x} \hat{i} +  \frac{\partial f}{\partial y} \hat{j} + \frac{\partial f}{\partial z} \hat{z})$ <br> 

## Crater Difusion 

\frac{\partial h}{\partial t} = \kappa (\frac{\partial^2h}{\partial x^2} + \frac{\partial^2h}{\partial^2y}) <br> 

$\implies$ $\frac{\partial h}{\partial t} = \kappa \nabla^2 h$ <br> 

where, $h(x,y,t)$ is the surface elevation, $t$ is the time, and $\kappa$ is is the hillslope transport coefficient <br> 

To solve numerically, we can discretize the continuous domain into a grid with spatial steps $\Delta x$ and $\Delta y$ and a time step $\Delta t$. <br> 

Using a Forward-Time Central-Space (FTCS) finite difference scheme, the spatial second derivative (the Laplacian $\nabla^2 h$) at a grid cell $(i,j)$ are approximated: <br> 

\frac{\partial^2h}{\partial x^2} \approx \frac{h_{i+1,j} - 2h_{i,j} + h_{i-1,j}}{\Delta x^2} <br> 

\frac{\partial^2h}{\partial y^2} \approx \frac{h_{i,j+1} - 2h_{i,j} + h_{i-1,j}}{\Delta x^2} <br> 

## Discretize the Time Derivative 

Approximating the time derivate on the right hand-side: 

\\frac{\partial h}{\partial t} = (\frac{\partial ^2 h}{\partial x^2} + \frac{\partial^2 h}{\partial y^2})\approx \frac{h_{i,j}^{n+1} - h_{i,j}^{n}}{\Delta t} <br> 

\frac{h_{i,j}^{n+1} - h_{i,j}^{n}}{\Delta t} \approx \kappa \left( \frac{h_{i+1,j}^{n} - 2h_{i,j}^n + h_{i-1,j}^n}{\Delta x^2} + \frac{h_{i,j-1}^{n} - 2h_{i,j}^n + h_{i,j+1}^n}{\Delta y^2} \right) <br> 

h_{i,j}^{n+1}  = h_{i,j}^{n} + \kappa\Delta t \left( \frac{h_{i+1,j}^{n} - 2h_{i,j}^n + h_{i-1,j}^n}{\Delta x^2} + \frac{h_{i,j-1}^{n} - 2h_{i,j}^n + h_{i,j+1}^n}{\Delta y^2} \right) <br> 

<b> # NOTE <b>: this means that to find the elevation of a pixel tomorrow (later $t$), take the elveation today ($t=0$), and add or subtract material based on how much higher or lower it is compared to its immediate neighbours, scaled by the diffusion coefficient and the tie step size (i.e. : $\kappa\Deta t$). <br> 
