# Quantitative Lunar Crater Degradation & Topographic Diffusion

Welcome to my digital lab notebook and research repository for investigating lunar impact crater degradation. This project treats planetary topography as continuous mathematical surfaces, employing advanced numerical methods and partial differential equations (PDEs) to model mass-wasting and regolith transport over geological timescales. <br> 

## 1. Project Overview & Scientific Motivation
Impact craters on airless bodies like the Moon gradually degrade due to micrometeoroid bombardment, seismic shaking, and gravity-driven downslope mass-wasting (hillslope diffusion). <br> 
By modeling this process deterministically, this research aims to:

- <b>Quantify Regolith Transport<b>: Measure how hillslope diffusion coefficients ($\kappa$) vary across different lunar terrains.
- <b>Determine Morphologic Age<b>: Estimate the age of impact structures and geologic units through forward and inverse diffusion modeling.
- <b>Advance Computational Geomorphology<b>: Build robust, vectorized Python solvers capable of handling large-scale satellite topography data without performance bottlenecks.

## 2. Repository Architecture
This repository is organized to maintain a clear separation between high-level project management, instrument-specific data pipelines, and mathematical theory:

```
/Crater Analysis/
├── README.md               # High-level project direction and roadmap (this file)
├── theory/                 # Mathematical and physical derivations (PDEs, FTCS, inversion)
└── LRO/                    # Lunar Reconnaissance Orbiter data and pipelines
    └── LOLA/               # Lunar Orbiter Laser Altimeter data products
        ├── data/           # Local destination for downloaded .img and .lbl files
        └── scripts/        # Data scraping, indexing, and downsampling modules
```
- README.md (Root): Outlines project scope, phases, and structural layout.
- theory/: Houses detailed LaTeX/Markdown notes on the physics of mass-wasting, finite-difference discretizations, and stability criteria.
- LRO/LOLA/: Contains instrument-specific scripts (`test1.py`, `pull_pds_repository.py`) for memory-safe ingestion of PDS-format Global Digital Elevation Models (LDEMs).

## 3. Research Roadmap & Execution Phases

### Phase 1: Forward PDE Solver
- <b>Objective<b>: Establish the core numerical solver using NumPy vectorization.
- <b>Details<b>: Solve the 2D linear diffusion equation ($\frac{\partial h}{\partial t} = \frac{\partial h}{\partial t} = \kappa\nabla ^2h$) using an explicit Forward-Time Central-Space (FTCS) scheme on isolated, real lunar elevation models. 

### Phase 2: Empirical Scaling & Synthetics
- <b>Objective<b>: Construct baseline geometries and validate conservation properties.
- <b>Details<b>: Integrate empirical morphometric scaling relations (e.g., Pike's laws) to generate idealized pristine crater baselines. Run forward simulations on synthetic topographies to test boundary conditions and numerical stability.

### Phase 3: Inverse Optimization Engine
- <b>Objective<b>: Build an automated inversion workflow (Approach 4).
- <b>Details<b>: Implement cost-function minimization algorithms to automatically fit simulated degradation profiles to observed present-day crater topography, solving for initial depth and effective age ($\kappa t$) simultaneously.

### Phase 4: Targeted Case Study & Proposal
- <b>Objective<b>: Execute analysis and compile research documentation.
