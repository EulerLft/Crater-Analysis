# Physics: Mass Wasting/Diffusion Derivation

<b>crater forms:</b> steep, pristine rims (figure 1.1)

<b>billion of years later:</b> broken rocks from seismic activity or microscopic cratering loosen and slide downward (see figure 1.2)

## Flux Equation

$$\mathbf{q} = -\kappa\nabla h$$

- rate of sediment transport (mass flux - $\mathbf{q}$) per unit contour length is proportional to the local surface slope ($\nabla h$).
- material moves from highest elevation (rim) to lowest elevation (floor) down the steepest gradient

## Mass Conservation

It is well established that:

$$\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{j} = \sigma$$

$$\implies \frac{\partial h}{\partial t} + \nabla \mathbf{q} = 0$$

(i.e. mass is conserved in the system)

substituting our flux into the mass conservation equation we obtain:

$$\frac{\partial h}{\partial t} = -\nabla\cdot(-\kappa \nabla h)$$

$$\implies \frac{\partial h}{\partial t} = \kappa \nabla^2 h$$
