## Block 1: Phase-Space Dynamics and Truncation Limits (Days 1–5)

### Main Goal
Develop rapid intuition for Wigner-function animations and determine exactly where numerical Hilbert-space truncation ruins quantum simulations.

---
### Big Project
Build a highly optimized script that generates animated Wigner-function movies of displaced coherent states and highly excited thermal states, intentionally pushing the system until numerical boundary errors appear.

---

### Key Equations

$$
W(x, p) = \frac{1}{\pi\hbar} \int_{-\infty}^{\infty} \langle x + y | \hat{\rho} | x - y \rangle e^{-2ipy/\hbar} dy
$$

$$
\hat{D}(\alpha) = \exp(\alpha \hat{a}^\dagger - \alpha^* \hat{a})
$$
### Day 1 — The Wigner Grid and Coherent States 


#### Build
- [x] Construct a coherent state $|\alpha\rangle$ for various amplitudes.
- [x] Set up a custom phase-space grid $(x, p)$ using `numpy.linspace`.
#### Simulate
- [x] Compute the Wigner function $W(x, p)$ using `qutip.wigner`.
#### Plot
- [x] Generate a 2D heatmap with a diverging colormap (`RdBu`) centered at zero.
- [x] Generate a 3D surface plot of the same Wigner function.
#### Investigate
- [x] Integrate the Wigner matrix numerically (using `scipy.integrate.simps`). Verify it normalizes to 1.
#### Learn
- How `qutip.wigner` maps state vectors to phase-space arrays and how to manipulate those arrays as standard data.

---

### Day 2 — Unitary Evolution Animation

#### Build
- [x] Define the free harmonic oscillator Hamiltonian $\hat{H} = \hbar\omega \hat{a}^\dagger \hat{a}$.
- [x] Create a time array $t$ spanning three full oscillation periods.

#### Simulate
- [x] Evolve $|\alpha\rangle$ using `mesolve`, saving the state at 100 time steps.

#### Plot
- [x] Use `matplotlib.animation.FuncAnimation` to render an MP4/GIF of the Wigner function orbiting the origin.

#### Investigate
- Track the expectation values $\langle \hat{x} \rangle$ and $\langle \hat{p} \rangle$ simultaneously and overlay them on the animation as a tracing dot.

#### Learn
- How to efficiently bundle QuTiP states into Matplotlib animations without crashing memory.

---

### Day 3 — Hilbert-Space Truncation Failure

#### Build
- [x] Set the maximum Fock dimension to $N=20$.

#### Simulate
- [x] Systematically displace the vacuum by increasing $\alpha$ from $0$ to $15$.

#### Plot
- [x] Plot the trace of the density matrix $\text{Tr}(\rho)$ vs. $\alpha$.
- Plot Wigner functions for $\alpha$ near the boundary.

#### Investigate
- Observe the unphysical "ripples" and "wall reflections" in the Wigner function when $\alpha$ approaches $\sqrt{N}$.

#### Learn
- Exactly how and why probability "leaks" out of a truncated finite-dimensional matrix, and how to detect it via trace calculations.


---

### Day 4 — Thermal States and Mixture Geometries

#### Build
- Construct thermal density matrices $\rho_{th}$ for various mean photon numbers $\bar{n}$.

#### Simulate
- Add coherent displacement to the thermal state: $\rho' = \hat{D}(\alpha)\rho_{th}\hat{D}^\dagger(\alpha)$.

#### Plot
- Create a comparative grid of 3D Wigner plots showing the broadening of the thermal state.

#### Investigate
- Extract the peak amplitude of the Wigner function at the center of the blob. Plot peak height vs. $\bar{n}$.

#### Learn
- The difference between pure-state minimal uncertainty and mixed-state thermal broadening in phase space.

---

### Day 5 — Arbitrary State Engineering (Superpositions)

#### Build
- Construct an arbitrary non-classical state, e.g., $|\psi\rangle = (|0\rangle + |3\rangle + |6\rangle)/\sqrt{3}$.

#### Simulate
- Compute its Wigner function on a high-resolution grid.

#### Plot
- Generate a high-contrast heatmap isolating the negative regions (setting all positive values to zero in the array).

#### Investigate
- Extract the total Wigner negativity (sum of all negative elements).
- Sweep the grid resolution and observe how low resolution aliasing destroys the negativity calculation.

#### Learn
- How numerical grid density directly impacts the extraction of quantum non-classicality metrics.

---

### Visual Goals

- 3D surface plots of displaced thermal states
- Animated Wigner evolution (MP4/GIF) of an orbiting coherent state
- Heatmaps explicitly isolating negative phase-space regions
- Line plots of $\text{Tr}(\rho)$ dropping due to boundary errors

---

### Numerical Investigation

Explore:
- truncation effects when displacing near the Hilbert space limit
- normalization failure when integrating coarse Wigner grids
- memory usage when storing hundreds of `Qobj` states for animation

---

### Research Connection

Connect to:
- State tomography experiments
- Visualizing quantum states in circuit QED
- Benchmarking the numerical safety limits for all future simulations

---

### Final Outcome

You now have a fully reusable "Phase Space Camera" Python module. You understand exactly what $N$ (dimension) you need for a given energy scale, and you can animate the output of any future `mesolve` result instantly.

---

## Block 2: Squeezed States & Quadrature Dynamics (Days 6–10)

### Main Goal
Master the generation, evolution, and numerical pathologies of squeezed vacuum states, mapping out the limits of continuous-variable quantum optics.

---

### Big Project
Build a phase-space simulation of a highly squeezed vacuum state rotating in a cavity, extracting the time-dependent variance of generalized quadratures and generating a "breathing" variance phase diagram.

---

### Key Equations

$$
\hat{S}(\xi) = \exp\left(\frac{1}{2}\xi^* \hat{a}^2 - \frac{1}{2}\xi (\hat{a}^\dagger)^2\right)
$$

$$
\hat{X}_\theta = \frac{1}{\sqrt{2}}(\hat{a}e^{-i\theta} + \hat{a}^\dagger e^{i\theta})
$$

---

### Day 6 — The Squeezing Operator and Ellipses

#### Build
- Define the generalized quadrature operator $\hat{X}_\theta$ as a Python function taking angle $\theta$.

#### Simulate
- Apply the squeezing operator $\hat{S}(r)$ to the vacuum for $r = 0.5$ to $1.5$.

#### Plot
- Plot the 2D Wigner heatmap. Overlay a 1-sigma contour ellipse extracted from the covariance matrix.

#### Investigate
- Sweep $\theta$ from $0$ to $\pi$. Compute $\Delta X_\theta^2$ and plot variance vs. angle to map the squeezing/anti-squeezing axes.

#### Learn
- How squeezing breaks phase symmetry and transforms the vacuum disc into an error ellipse.

---

### Day 7 — Squeezing Instability limits

#### Build
- Fix the Hilbert space cutoff at $N=50$.

#### Simulate
- Sweep the squeezing parameter $r$ from $0$ to $3.0$.

#### Plot
- Plot the minimum quadrature variance $\Delta X_{min}^2$ vs $r$ on a logarithmic scale.

#### Investigate
- Identify the exact value of $r$ where numerical truncation causes the variance to artificially *increase* instead of squeezing further.
- Fit the stable region to the theoretical $e^{-2r}$ scaling.

#### Learn
- Squeezed states expand exponentially in photon number. You learn precisely how to detect when your simulation of a highly squeezed state becomes numerical garbage.

---

### Day 8 — Rotating Squeezed Vacuum Animation

#### Build
- Initialize a squeezed vacuum state with $r=1.0$.

#### Simulate
- Evolve under the free harmonic oscillator Hamiltonian $\hat{H} = \omega \hat{a}^\dagger\hat{a}$.

#### Plot
- Animate the Wigner function. It should rotate in place, resembling a spinning propeller.

#### Investigate
- Compute the variances $\Delta X^2$ and $\Delta P^2$ at each time step. Plot them vs time.
- Verify that the product $\Delta X(t) \Delta P(t)$ fluctuates, but the determinant of the full covariance matrix remains invariant.

#### Learn
- Free evolution rotates the squeezing axis, causing laboratory frame measurements to see periodic "breathing" of the variance.

---

### Day 9 — Squeezed Coherent States

#### Build
- Combine operations: displace then squeeze, versus squeeze then displace.

#### Simulate
- Generate $|\alpha, \xi\rangle = \hat{D}(\alpha)\hat{S}(\xi)|0\rangle$.

#### Plot
- 3D Wigner plots of both orderings. Show they result in different phase-space geometries (displacement direction vs squeezing axis).

#### Investigate
- Calculate the Mandel Q-parameter for the squeezed coherent state. Map out the parameter space of $(\alpha, r)$ to find regimes of sub-Poissonian vs super-Poissonian statistics.

#### Learn
- Non-commutativity of displacement and squeezing visually, and how squeezing can induce extreme photon bunching or anti-bunching.

---

### Day 10 — Nonlinear Squeezing Generation (Kerr)

#### Build
- Define a Kerr nonlinear Hamiltonian $\hat{H} = \chi (\hat{a}^\dagger\hat{a})^2$.

#### Simulate
- Evolve an initial coherent state $|\alpha\rangle$ under the Kerr Hamiltonian.

#### Plot
- Animate the Wigner function. Watch the coherent state shear into a squeezed crescent, then over-shear into a complex interference pattern.

#### Investigate
- At each time step, find the optimal quadrature angle $\theta$ that minimizes variance. Extract the maximum squeezing generated before the state breaks apart.

#### Learn
- How self-phase modulation naturally generates squeezing dynamically, and how to programmatically extract the optimal measurement axis.

---

### Visual Goals

- Contour maps of covariance error ellipses
- Log-scale plots of exponential squeezing scaling
- Spinning propeller Wigner animations
- Kerr crescent state shearing movies

---

### Numerical Investigation

Explore:
- The exact $r_{max}$ supported by a given dimension $N$
- Extracting optimal angles from numerical covariance matrices
- Breakdown of minimum uncertainty under Kerr evolution

---

### Research Connection

Connect to:
- Gravitational wave detectors (LIGO) injecting squeezed vacuum
- Continuous-variable quantum key distribution (CV-QKD)
- Microwave squeezing in Josephson Parametric Amplifiers (JPAs)

---

### Final Outcome

You have built a rigorous toolkit for dealing with squeezed states. You can generate them, rotate them, extract their principle axes dynamically, and—crucially—know exactly when your computer is lying to you due to Hilbert space explosion.

---

## Block 3: Multi-Mode Tensors & The HOM Effect (Days 11–15)

### Main Goal
Conquer the multi-mode tensor product space, understand beam splitter unitaries, and simulate pure quantum interference (Hong-Ou-Mandel) while extracting scaling bottlenecks.

---

### Big Project
Simulate a two-port beam splitter, inject single photons and coherent states, calculate output correlation functions, and profile the exponential runtime scaling of multi-mode tensor products.

---

### Key Equations

$$
\hat{H}_{BS} = i\theta (\hat{a}^\dagger \hat{b} -  \hat{a} \hat{b}^\dagger)
$$

$$
\mathcal{H}_{tot} = \mathcal{H}_A \otimes \mathcal{H}_B
$$

---

### Day 11 — The Tensor Product Explosion

#### Build
- Construct two cavity modes $\hat{a} = \hat{a}_1 \otimes \hat{1}_2$ and $\hat{b} = \hat{1}_1 \otimes \hat{a}_2$ using `qutip.tensor`.

#### Simulate
- Build an $M$-mode coupled system (e.g., a tight-binding photon chain).

#### Plot
- Plot the memory size (`.data.nbytes`) of the resulting sparse Hamiltonian matrix versus mode count $M$.

#### Investigate
- Profile the execution time of a single 1-step `mesolve` integration as $N$ (truncation per mode) and $M$ (number of modes) increase.

#### Learn
- The "Curse of Dimensionality". You gain a hard, practical intuition for why full quantum state vector simulation is limited to small networks.

---

### Day 12 — The Beam Splitter Unitary

#### Build
- Define the beam splitter unitary $\hat{U}_{BS}(\theta) = \exp[\theta (\hat{a}^\dagger \hat{b} - \hat{a} \hat{b}^\dagger)]$.

#### Simulate
- Inject $|\alpha\rangle \otimes |0\rangle$. Apply $\hat{U}_{BS}(\pi/4)$ (50:50 split).

#### Plot
- Extract the partial trace `rho_A = ptrace(state, 0)` and `rho_B = ptrace(state, 1)`.
- Plot the photon number distributions (bar charts) of the output ports.

#### Investigate
- Inject $|\alpha\rangle \otimes |\beta\rangle$. Sweep the relative phase between them and plot the output intensity of mode A to map out classical cosine interference fringes.

#### Learn
- How to construct multi-mode unitaries, apply them, and trace out subsystems to simulate realistic localized detectors.

---

### Day 13 — The Hong-Ou-Mandel Dip

#### Build
- Inject the Fock state $|1\rangle \otimes |1\rangle$ into the beam splitter.

#### Simulate
- Apply the 50:50 beam splitter unitary.
- Calculate the joint probability of detecting one photon in each port: $P(1,1) = \text{Tr}(|1,1\rangle\langle1,1| \rho_{out})$.

#### Plot
- Parameterize the beam splitter reflectivity $R = \sin^2(\theta)$.
- Sweep $R$ from 0 to 1 and plot the coincidence probability $P(1,1)$.

#### Investigate
- Extract the exact minimum of the curve and verify it hits exactly 0 at $R=0.5$.

#### Learn
- The mathematical origin of photon bunching and how to compute joint coincidence probabilities computationally.

---

### Day 14 — Bipartite Entanglement Generation

#### Build
- Inject the dual vacuum $|0,0\rangle$.

#### Simulate
- Apply the two-mode squeezing operator $\hat{S}_2(r) = \exp(r(\hat{a}^\dagger\hat{b}^\dagger -  \hat{a}\hat{b}))$.

#### Plot
- Calculate the von Neumann entropy of the reduced state of mode A.
- Plot entropy vs squeezing parameter $r$.

#### Investigate
- Extract the Logarithmic Negativity (using `qutip.logarithmic_negativity` or a custom partial transpose function) to quantify entanglement exactly.
- Verify that tracing out mode B leaves mode A in a perfect thermal state.

#### Learn
- How parametric down-conversion generates continuous-variable entanglement, and how to measure it numerically.

---

### Day 15 — Joint Wigner Functions

#### Build
- Take the output state of a 50:50 beam splitter fed with a single photon and vacuum ($|1,0\rangle$).

#### Simulate
- This state is entangled: $(|1,0\rangle + |0,1\rangle)/\sqrt{2}$.

#### Plot
- Since a 4D Wigner function is impossible to plot, plot the 2D marginal Wigner functions for mode A and mode B.
- Next, fix the quadratures of mode B to specific measurement outcomes (conditional measurement), and plot the *conditional* Wigner function of mode A.

#### Investigate
- Observe how "measuring" a vacuum in mode B instantly projects mode A into a single-photon Wigner function with a negative core.

#### Learn
- How to visualize correlations in phase space by projecting multi-mode states conditionally.

---

### Visual Goals

- Bar charts of marginal photon statistics
- HOM dip coincidence probability curves
- Entropy vs squeezing scaling graphs
- Memory/Runtime vs Mode-count logarithmic heatmaps

---

### Numerical Investigation

Explore:
- Memory limits of `tensor()`
- Extracting exact HOM dip minimums via array interpolation
- Numerical computation of partial transposes for entanglement metrics

---

### Research Connection

Connect to:
- Boson Sampling architectures
- Entangled photon pair sources (SPDC)
- Dual-rail quantum computing

---

### Final Outcome

You are now comfortable working in multi-mode tensor spaces. You can build optical components as unitary matrices, wire them together, trace out unobserved ports, and compute entanglement entropy directly from the data.

---

## Block 4: Mach-Zehnder Interferometry & Quantum Metrology (Days 16–20)

### Main Goal
Build a complete digital Mach-Zehnder Interferometer (MZI), inject various quantum states, and extract phase sensitivity to computationally prove the Heisenberg limit.

---

### Big Project
Sweep an internal phase shift inside an MZI, extract the Fisher information from the output statistics, and compare the phase sensitivity of Coherent states, Fock states, and N00N states.

---

### Key Equations

$$
\hat{U}_{MZI}(\phi) = \hat{U}_{BS}^\dagger \cdot e^{i\phi \hat{a}^\dagger \hat{a}} \cdot \hat{U}_{BS}
$$

$$
\Delta \phi = \frac{\Delta \hat{O}}{|\partial \langle \hat{O} \rangle / \partial \phi|}
$$

---

### Day 16 — Building the Digital MZI

#### Build
- Construct the three-part unitary: 50:50 BS, phase shift $e^{i\phi \hat{a}^\dagger \hat{a}}$ on arm A, and a second 50:50 BS.

#### Simulate
- Inject a coherent state $|\alpha\rangle \otimes |0\rangle$.
- Sweep the phase $\phi$ from $0$ to $2\pi$.

#### Plot
- Plot the expected photon number at port A vs $\phi$. Overlay the analytical cosine curve.

#### Investigate
- Compute the variance of the photon number at the output port. Plot the signal-to-noise ratio (SNR) vs $\phi$.

#### Learn
- How to stack unitaries to create a full optical instrument computationally.

---

### Day 17 — The Standard Quantum Limit (SQL)

#### Build
- Define an observable operator at the output, e.g., $\hat{O} = \hat{a}^\dagger \hat{a} - \hat{b}^\dagger \hat{b}$ (photon number difference).

#### Simulate
- For a coherent state input, calculate the phase variance $\Delta \phi$ at the most sensitive point of the fringe ($\phi = \pi/2$).

#### Plot
- Sweep the input intensity $|\alpha|^2$ (mean photon number $N$).
- Plot $\Delta \phi$ vs $N$ on a log-log scale.

#### Investigate
- Fit the extracted line and verify the slope matches the Standard Quantum Limit scaling $1/\sqrt{N}$.

#### Learn
- How to extract metrological sensitivity (error bars) from simulated quantum expectation values and variances.

---

### Day 18 — N00N States and the Heisenberg Limit

#### Build
- Construct an arbitrary N00N state: $(|N,0\rangle + |0,N\rangle)/\sqrt{2}$.

#### Simulate
- Inject the N00N state into the MZI (bypassing the first BS, as N00N states are typically generated *inside* the interferometer).
- Sweep $\phi$.

#### Plot
- Plot the output observable. Observe that the interference fringes oscillate $N$ times faster than the classical coherent state (super-resolution).

#### Investigate
- Extract $\Delta \phi$ for the N00N state across different $N$. Plot it against the coherent state data on the log-log scale.
- Fit the new line and verify it follows the Heisenberg Limit $1/N$.

#### Learn
- Visual and numerical proof of quantum super-resolution and enhanced phase sensitivity.

---

### Day 19 — Parity Detection

#### Build
- Define the parity operator for the output port: $\hat{\Pi}_A = \exp(i\pi \hat{a}^\dagger \hat{a})$.

#### Simulate
- Inject a squeezed vacuum state into one port and a coherent state into the other (Caves' 1981 scheme).

#### Plot
- Plot the expectation value of parity $\langle \hat{\Pi}_A \rangle$ as a function of the internal phase $\phi$.

#### Investigate
- Extract the FWHM of the central parity fringe. Show that it is narrower than the classical coherent limit.

#### Learn
- Parity is often the optimal observable for non-classical states. You learn how to construct and measure highly nonlinear observables.

---

### Day 20 — Squeezed MZI Parameter Sweep

#### Build
- Automate the Caves interferometer scheme (Squeezed Vacuum + Coherent State).

#### Simulate
- Fix the total photon number $N_{tot} = |\alpha|^2 + \sinh^2(r)$.
- Sweep the ratio of squeezed photons to coherent photons.

#### Plot
- Plot a 2D heatmap of Phase Sensitivity $\Delta \phi$ vs (Total Photon Number, Squeezing Ratio).

#### Investigate
- Numerically locate the exact optimum splitting ratio that minimizes phase error for a fixed photon budget.

#### Learn
- How to perform research-level parameter sweeps to optimize a quantum sensor's resource allocation.

---

### Visual Goals

- Coherent vs N00N interference fringe comparisons
- Log-log plots comparing SQL vs Heisenberg limit scaling
- Narrowing parity detection fringes
- 2D heatmaps of metrological sensitivity

---

### Numerical Investigation

Explore:
- Numerical derivative extraction for $|\partial \langle \hat{O} \rangle / \partial \phi|$ using `numpy.gradient`.
- Handling highly oscillatory phase factors in large N00N states.
- Optimizing sensor parameters computationally.

---

### Research Connection

Connect to:
- LIGO's use of squeezed light injection.
- Quantum metrology and phase estimation bounds (Cramer-Rao).
- Design of next-generation optical gyroscopes.

---

### Final Outcome

You have built a fully functional digital quantum sensor. You can inject arbitrary quantum states, "tune" the interferometer, measure observables, and computationally prove whether a scheme beats the classical limit.

---

## Block 5: Decoherence & Lindblad Master Equations (Days 21–25)

### Main Goal
Transition from idealized unitary evolution to realistic open quantum systems, simulating cavity decay, thermal baths, and pure dephasing while extracting decay rates.

---

### Big Project
Simulate a coherent state inside a lossy cavity, watch it decay to a thermal state, extract the energy and purity decay rates, and map the Liouvillian dynamics.

---

### Key Equations

$$
\frac{d\rho}{dt} = -i[\hat{H}, \rho] + \sum_n \left( \hat{C}_n \rho \hat{C}_n^\dagger - \frac{1}{2}\{\hat{C}_n^\dagger \hat{C}_n, \rho\} \right)
$$

$$
\hat{C}_{loss} = \sqrt{\kappa}\hat{a}
$$

---

### Day 21 — Amplitude Damping (Cavity Loss)

#### Build
- Define a coherent state $|\alpha=3\rangle$.
- Define the collapse operator for single-photon loss $\hat{C} = \sqrt{\kappa}\hat{a}$.

#### Simulate
- Evolve the state using `mesolve` with $\hat{H}=0$ and $c\_ops=[\hat{C}]$.

#### Plot
- Plot the expected photon number $\langle \hat{n}(t) \rangle$ vs time. Overlay the theoretical exponential decay $e^{-\kappa t}$.
- Generate an animated Wigner movie of the coherent blob spiraling exactly into the origin (vacuum).

#### Investigate
- Compute the purity $\text{Tr}(\rho^2)$ over time. Notice that it dips (becomes mixed) and then returns to 1 (pure vacuum). Extract the exact time of minimum purity.

#### Learn
- How the Lindblad equation models energy dissipation, and how open systems transition through mixed states even if the final state is pure.

---

### Day 22 — Thermal Baths

#### Build
- Define an environment at finite temperature $\bar{n}_{th}$.
- Set up two collapse operators: $\sqrt{\kappa(1+\bar{n}_{th})}\hat{a}$ (emission) and $\sqrt{\kappa\bar{n}_{th}}\hat{a}^\dagger$ (absorption).

#### Simulate
- Start from the vacuum state and evolve.

#### Plot
- Plot the populations of the first 5 Fock states over time.

#### Investigate
- Use `qutip.steadystate` to find the exact infinite-time density matrix directly.
- Calculate the trace distance between the dynamically evolving $\rho(t)$ and $\rho_{steadystate}$. Fit the distance curve to extract the thermalization rate.

#### Learn
- How absorption and emission balance to produce thermal equilibrium, and how to verify thermalization computationally.

---

### Day 23 — Pure Dephasing

#### Build
- Define the pure dephasing collapse operator: $\hat{C}_\phi = \sqrt{\gamma_\phi}\hat{a}^\dagger\hat{a}$.

#### Simulate
- Initialize a coherent superposition $(|0\rangle + |4\rangle)/\sqrt{2}$. Evolve under pure dephasing.

#### Plot
- Plot $\langle \hat{n}(t) \rangle$ to verify that exact energy is conserved (it should be perfectly flat).
- Plot the absolute value of the off-diagonal density matrix element $|\rho_{0,4}(t)|$.

#### Investigate
- Fit the decay of the off-diagonal element to an exponential. Extract the decoherence rate and verify it scales as $\gamma_\phi (\Delta n)^2$.

#### Learn
- The critical difference between $T_1$ (energy relaxation) and $T_2^*$ (pure dephasing), and how dephasing destroys quantum information without exchanging energy.

---

### Day 24 — Driven-Dissipative Systems

#### Build
- Combine a coherent drive Hamiltonian $\hat{H} = \Omega(\hat{a} + \hat{a}^\dagger)$ with cavity loss $\kappa$.

#### Simulate
- Evolve from vacuum to the steady state.

#### Plot
- Sweep the drive strength $\Omega$. Plot the steady-state photon number vs $\Omega$.

#### Investigate
- Calculate the Wigner function of the steady state. Observe that it is a pure coherent state, displaced by $2\Omega/\kappa$.
- Numerically prove that the steady state of a driven lossy cavity is exactly a coherent state (no mixedness added by the loss in this specific driven scenario).

#### Learn
- How drives and dissipation compete to form dynamic steady states, mimicking realistic laser fields in cavities.

---

### Day 25 — Two-Mode Decoherence & Sudden Death

#### Build
- Initialize a two-mode entangled Bell state $(|00\rangle + |11\rangle)/\sqrt{2}$.

#### Simulate
- Apply independent amplitude damping to both modes.

#### Plot
- Compute the Concurrence over time.

#### Investigate
- Observe that the Concurrence hits absolute zero at a finite time, rather than decaying asymptotically. Extract this exact time $T_{ESD}$.
- Sweep the initial purity of the state (by adding white noise) and plot $T_{ESD}$ vs purity to map the boundary of "Entanglement Sudden Death".

#### Learn
- Quantum entanglement can be completely destroyed in finite time by local environments, a vital realization for quantum engineering.

---

### Visual Goals

- Wigner movies of states decaying to vacuum
- Population dynamics showing thermal equilibration
- Trace distance convergence plots
- Entanglement Sudden Death finite-time crash plots

---

### Numerical Investigation

Explore:
- Extracting thermalization and decoherence rates via exponential curve fitting.
- Verifying $T_1$ vs $T_2$ dynamics.
- Using `steadystate()` directly vs running `mesolve` to $t \to \infty$.

---

### Research Connection

Connect to:
- Cavity QED linewidth limits
- Thermal noise in macroscopic resonators
- Protecting entangled states in noisy quantum networks

---

### Final Outcome

You can now simulate realistic, leaky, noisy quantum systems. You know how to extract decay rates, verify steady states, and computationally separate energy loss from phase loss.

---

## Block 6: Schrödinger Cats & Macroscopic Fragility (Days 26–30)

### Main Goal
Demonstrate computationally why we don't see quantum effects in the macroscopic world by scaling up superposition states and analyzing their extreme fragility to environmental coupling.

---

### Big Project
Create massive Schrödinger cat states, subject them to microscopic amounts of cavity loss, and extract the scaling law that proves decoherence rate scales with the macroscopic size of the state.

---

### Key Equations

$$
|\text{cat}_\pm\rangle = \mathcal{N} (|\alpha\rangle \pm |-\alpha\rangle)
$$

$$
\tau_{dec} \approx \frac{1}{\kappa |\alpha|^2}
$$

---

### Day 26 — Constructing the Cat

#### Build
- Write a function that generates an Even or Odd Schrödinger cat state for a given $\alpha$.

#### Simulate
- Compute the Wigner functions for $\alpha \in [1, 2, 3, 4]$.

#### Plot
- Plot the 3D surfaces of the Wigner functions. Observe the central interference fringes.

#### Investigate
- Write a script to count the number of fringes (oscillations) between the two main coherent blobs.
- Show numerically that the spatial frequency of the fringes increases directly with the separation distance $2\alpha$.

#### Learn
- Visualizing macroscopic quantum superpositions and the origin of highly oscillatory phase space structures.

---

### Day 27 — Decoherence of the Cat

#### Build
- Set up amplitude damping ($\kappa$).

#### Simulate
- Evolve an $\alpha=3$ cat state under loss.

#### Plot
- Generate a Wigner animation. Watch the central interference fringes blur and vanish almost instantly, leaving a classical statistical mixture of two blobs that slowly spiral inward.

#### Investigate
- Track the Wigner negativity (sum of all $W(x,p) < 0$) over time. Plot it on a log scale and extract the decay slope.

#### Learn
- The timescale of quantum decoherence is drastically shorter than the timescale of energy dissipation.

---

### Day 28 — The Scaling Law of Fragility

#### Build
- Automate the Wigner negativity extraction from Day 27.

#### Simulate
- Sweep the cat size $\alpha$ from $1$ to $5$.
- For each $\alpha$, evolve the state and extract the decoherence rate $\Gamma_{dec}$ from the decay of Wigner negativity.

#### Plot
- Plot the extracted $\Gamma_{dec}$ versus $|\alpha|^2$.

#### Investigate
- Perform a linear regression on this plot. Numerically prove the theoretical scaling law: $\Gamma_{dec} \propto \kappa |\alpha|^2$.

#### Learn
- Why macroscopic objects (large $|\alpha|^2$) lose their quantum superposition almost instantaneously. This is computational proof of the classical limit.

---

### Day 29 — Wigner Negativity Parameter Sweep

#### Build
- Add thermal noise $\bar{n}_{th}$ to the environment.

#### Simulate
- Sweep both the cat size $\alpha$ and the bath temperature $\bar{n}_{th}$.

#### Plot
- Generate a 2D heatmap of the survival time of Wigner negativity (the time it takes for negativity to drop below $10^{-3}$).

#### Investigate
- Extract the boundary contour mapping exactly how cold an environment must be to preserve a cat state of a certain size for 1 microsecond.

#### Learn
- Mapping robust parameter regimes for continuous-variable quantum memory design.

---

### Day 30 — Squeezed Cats

#### Build
- Apply the squeezing operator to a cat state: $\hat{S}(\xi)(|\alpha\rangle + |-\alpha\rangle)$.

#### Simulate
- Evolve the squeezed cat under amplitude damping.

#### Plot
- Plot Wigner snapshots. Observe how squeezing the axis of separation vs squeezing the orthogonal axis changes the fringe structure.

#### Investigate
- Extract the decoherence rate for the squeezed cat. Show numerically whether squeezing the state makes it more robust or more fragile to amplitude damping.

#### Learn
- How phase-space geometry interacts with isotropic environmental loss, a key concept in fault-tolerant bosonic codes (like the GKP code).

---

### Visual Goals

- Massive cat state 3D Wigner plots
- Animations of interference fringes wiping out while blobs remain stationary
- Log-scale negativity decay plots
- 2D heatmaps of survival times vs temperature

---

### Numerical Investigation

Explore:
- Extracting exact exponential decay constants from 2D matrix sums.
- Verifying the exact $\kappa |\alpha|^2$ scaling law via linear regression.
- Grid resolution aliasing errors when simulating large, highly-oscillatory cat states.

---

### Research Connection

Connect to:
- Bosonic error correction (Cat codes).
- Haroche's Nobel-winning microwave cavity experiments.
- Quantum-to-classical transition theory (Zurek).

---

### Final Outcome

You have computationally verified the mechanism of macroscopic decoherence. You can extract scaling laws from simulated array data and map out phase diagrams for quantum state survival.

---

## Block 7: Noisy Interferometry & Sensing (Days 31–35)

### Main Goal
Inject realistic decoherence into the idealized Mach-Zehnder Interferometer, map how loss degrades phase sensitivity, and optimize squeezed light injection to survive noisy environments.

---

### Big Project
Build an MZI where photon loss occurs inside the arms. Sweep the loss parameter, extract the degraded Fisher information, and find the optimal squeezing level that maximizes sensing under real-world conditions.

---

### Key Equations

$$
\mathcal{E}_{loss}(\rho) = \text{Tr}_{env} [\hat{U}_{BS}(\eta) (\rho \otimes |0\rangle\langle0|) \hat{U}_{BS}^\dagger(\eta)]
$$

$$
\Delta \phi \ge \frac{1}{\sqrt{F_Q}}
$$

---

### Day 31 — Modeling Loss as a Beam Splitter

#### Build
- Model internal loss $\eta$ explicitly by inserting a fictitious beam splitter into the MZI arm, where the second input is traced out (representing lost photons leaking to the environment).

#### Simulate
- Inject a N00N state. Apply the loss channel with a small transmission $\eta = 0.9$.

#### Plot
- Plot the output interference fringes. Compare the perfect $\eta=1.0$ fringes to the $\eta=0.9$ fringes.

#### Investigate
- Extract the visibility (contrast) of the fringes: $V = (I_{max} - I_{min}) / (I_{max} + I_{min})$. Plot Visibility vs $\eta$.

#### Learn
- How to rigorously model environmental loss mathematically as interaction with an unobserved vacuum mode.

---

### Day 32 — The Death of the Heisenberg Limit

#### Build
- Use the lossy MZI setup from Day 31.

#### Simulate
- Inject N00N states of size $N \in [2, 4, 6, 8, 10]$.
- Set the loss parameter to a tiny value, e.g., $5\%$ loss ($\eta = 0.95$).

#### Plot
- Plot the Phase Sensitivity $\Delta \phi$ vs $N$ on a log-log plot.

#### Investigate
- Observe that for small $N$, the sensitivity follows $1/N$, but for large $N$, the sensitivity violently bends back upwards (gets worse). Extract the critical $N$ where adding more photons ruins the measurement.

#### Learn
- The extreme fragility of highly entangled states: a single photon lost from a N00N state destroys the entire superposition.

---

### Day 33 — Robust Sensing: Squeezing vs Loss

#### Build
- Revert to the Caves MZI setup (Squeezed Vacuum + Coherent State).

#### Simulate
- Apply internal loss $\eta$ to the interferometer arms.
- Fix the total input photon number $N_{tot}$. Sweep the squeezing parameter $r$.

#### Plot
- Plot Phase Sensitivity $\Delta \phi$ vs squeezing $r$ for different loss levels $\eta$.

#### Investigate
- For zero loss, more squeezing always helps. For finite loss, the curve has a minimum. Extract the exact optimal squeezing parameter $r_{opt}$ for a given loss $\eta$.

#### Learn
- Real-world quantum sensors require a highly optimized balance between coherent drive and squeezing; too much squeezing is hyper-fragile to loss.

---

### Day 34 — Unequal Arm Loss

#### Build
- Set up the MZI where Arm A has loss $\eta_A$ and Arm B has loss $\eta_B$.

#### Simulate
- Inject a standard coherent state.

#### Plot
- Plot the output fringes when $\eta_A \neq \eta_B$.

#### Investigate
- Compute the output purity of the state. Show that differential loss creates which-path information, entangling the signal with the environment and reducing fringe visibility.

#### Learn
- The profound connection between "which-path" distinguishability and the destruction of quantum interference.

---

### Day 35 — Optimization via Parameter Sweeps

#### Build
- Wrap the entire noisy Caves MZI simulation in a single function taking $(\alpha, r, \eta)$.

#### Simulate
- Use `qutip.parallel_map` to sweep a massive 2D grid of coherent amplitude $\alpha$ and squeezing $r$ for a fixed, realistic internal loss ($\eta = 0.8$).

#### Plot
- Generate a high-resolution heatmap of the final output SNR.

#### Investigate
- Automatically locate the global maximum SNR. Overlay a contour mapping the region that successfully beats the classical Shot Noise Limit despite the $20\%$ loss.

#### Learn
- How to execute heavy, parallelized parameter sweeps to design realistic, loss-resilient quantum sensing protocols.

---

### Visual Goals

- Fringe visibility degradation curves
- Log-log sensitivity plots showing the N00N state breakdown
- Phase sensitivity vs squeezing curves with optimal dips
- Massive 2D heatmaps of sensor SNR optimization

---

### Numerical Investigation

Explore:
- Modeling non-unitary channels using fictitious beam splitters and partial traces.
- Extracting the "bending point" of scaling laws.
- Using `parallel_map` for computationally heavy parameter space explorations.

---

### Research Connection

Connect to:
- LIGO's specific optimal squeezing limits due to mirror loss.
- Quantum imaging and illumination in noisy environments.
- The theoretical bounds of noisy quantum metrology.

---

### Final Outcome

You can computationally design a quantum sensor for the real world. You understand how to model loss, how loss kills ideal scaling bounds, and how to numerically hunt for the optimal robust operational regime.

---

## Block 8: Quantum Trajectories & Jumps (Days 36–40)

### Main Goal
Unravel the Lindblad master equation into single stochastic trajectories (`mcsolve`), simulating what single experimental runs actually look like (quantum jumps).

---

### Big Project
Simulate a single continuously monitored atom in a cavity. Extract the discrete jump statistics, calculate waiting time distributions, and prove that ensemble averaging recovers the Lindblad equation.

---

### Key Equations

$$
dp = \delta t \langle \hat{C}^\dagger \hat{C} \rangle
$$

$$
|\psi(t+dt)\rangle = \frac{(1 - \frac{i}{\hbar} \hat{H}_{eff} dt)|\psi(t)\rangle}{|| ... ||}
$$

---

### Day 36 — The Stochastic Solver (`mcsolve`)

#### Build
- Define a two-level system (TLS) driven by a resonant laser: $\hat{H} = \Omega \sigma_x$.
- Define the spontaneous emission collapse operator: $\hat{C} = \sqrt{\gamma}\sigma_-$.

#### Simulate
- Use `mcsolve` to run exactly *one* trajectory (`ntraj=1`).

#### Plot
- Plot the excited state population $\langle \sigma_z \rangle$ vs time. Observe the smooth Rabi oscillations interrupted by sudden, discontinuous drops to the ground state.

#### Investigate
- Plot the norm of the state vector (before normalization) during the smooth periods between jumps. Verify it decays, representing continuous probability updates.

#### Learn
- The difference between deterministic ensemble evolution (density matrix) and stochastic single-shot reality (state vectors).

---

### Day 37 — Extracting Jump Statistics

#### Build
- Run a single, very long trajectory of the driven TLS using `mcsolve`.

#### Simulate
- Extract the raw time-series data of $\langle \sigma_z(t) \rangle$.

#### Plot
- Write an array-processing script using `numpy.diff` to automatically detect the exact timestamps of the quantum jumps.

#### Investigate
- Calculate the waiting times (time differences) between consecutive jumps.
- Plot a histogram of these waiting times. Fit the histogram to an exponential to extract the effective macroscopic emission rate.

#### Learn
- How to perform signal processing on simulated quantum data to extract physical rates, exactly as an experimentalist would with photon click data.

---

### Day 38 — Ensemble Averaging

#### Build
- Use the same driven TLS setup.

#### Simulate
- Run `mesolve` to get the exact deterministic density matrix evolution.
- Run `mcsolve` for $N\_{traj} \in [10, 100, 500, 1000]$.

#### Plot
- Overlay the averaged $\langle \sigma_z \rangle$ for the different $N\_traj$ sets on top of the exact `mesolve` curve.

#### Investigate
- Calculate the absolute error between the $N\_traj$ average and the exact solution at $t=5$. Plot Error vs $1/\sqrt{N\_traj}$ to verify standard Monte Carlo convergence scaling.

#### Learn
- The master equation is simply the statistical average of infinitely many single quantum trajectories.

---

### Day 39 — The Zeno Effect

#### Build
- Drive a TLS with a slow Rabi frequency $\Omega$.
- Apply a heavy pure dephasing operator $\hat{C}_\phi = \sqrt{\Gamma}\sigma_z$ to simulate continuous, strong measurement of the energy basis.

#### Simulate
- Evolve using `mesolve`. Sweep the measurement strength $\Gamma$.

#### Plot
- Plot $\langle \sigma_x(t) \rangle$. Observe how strong measurement "freezes" the Rabi oscillations.

#### Investigate
- Extract the effective slowed transition rate. Plot this rate vs $\Gamma$. Show numerically that transition probability is suppressed inversely proportional to measurement strength ($1/\Gamma$).

#### Learn
- Continuous observation collapses the wave function so rapidly that coherent dynamics are frozen (the Quantum Zeno Effect).

---

### Day 40 — Solver Runtime Profiling

#### Build
- Construct a large Hilbert space system, e.g., a multi-mode cavity array.

#### Simulate
- Wrap `mesolve` and `mcsolve` (with $N\_traj=200$) in Python `time` profiling blocks.

#### Plot
- Sweep the Hilbert space dimension $N$. Plot the runtime of `mesolve` vs `mcsolve`.

#### Investigate
- `mesolve` scales as $O(N^6)$, while `mcsolve` scales as $O(N^3 \times N\_traj)$. Find the intersection point on the graph.
- Extract the exact dimension $N$ where integrating 200 state vectors becomes computationally faster than integrating one large density matrix.

#### Learn
- Pure computational intuition: knowing *which* solver to use based on matrix dimensionality and scaling laws.

---

### Visual Goals

- Discontinuous quantum jump trajectory plots
- Histograms of waiting-time distributions
- Convergence plots of noisy trajectories collapsing onto smooth master equations
- Zeno freezing dynamics
- Runtime vs Dimension logarithmic benchmark charts

---

### Numerical Investigation

Explore:
- Array manipulation to detect discontinuities (jumps) in time-series data.
- Proving $1/\sqrt{N}$ Monte Carlo error convergence.
- Benchmarking big-O scaling limits of different ODE solvers.

---

### Research Connection

Connect to:
- Single-molecule fluorescence experiments.
- Trapped ion quantum jump observations.
- Error mitigation via stochastic unravelling.

---

### Final Outcome

You can now simulate exactly what happens in a single run of an experiment. You can process noisy "click" data, extract rates, and know exactly when to abandon `mesolve` for `mcsolve` to save RAM.

---

## Block 9: Homodyne Detection & Stochastic Evolution (Days 41–45)

### Main Goal
Simulate continuous homodyne measurement using Stochastic Master Equations (SMEs), generating noisy diffusion trajectories and demonstrating measurement-induced squeezing.

---

### Big Project
Implement a continuous homodyne monitor on a decaying cavity, track the stochastic diffusion of the quadrature, and show that continuous measurement conditionally purifies and squeezes the state.

---

### Key Equations

$$
d\rho = \text{Lindblad}(\rho)dt + \sqrt{\eta \kappa} \mathcal{H}[a](\rho) dW
$$

$$
\mathcal{H}[a](\rho) = a\rho + \rho a^\dagger - \text{Tr}(a\rho + \rho a^\dagger)\rho
$$

---

### Day 41 — Introduction to the SME

#### Build
- Define a cavity with single photon loss $\kappa$.
- Set up `qutip.photocurrent_mesolve` (or manually configure the stochastic solvers using `smesolve`).

#### Simulate
- Initialize the vacuum state. Monitor the $\hat{x}$ quadrature with $100\%$ efficiency.

#### Plot
- Plot the noisy photocurrent record $I(t)$ returned by the solver.

#### Investigate
- Calculate the power spectral density (FFT) of the photocurrent noise. Verify it matches flat, white shot noise for a vacuum cavity.

#### Learn
- How continuous homodyne detection generates a noisy photocurrent, consisting of the system signal deeply buried in shot noise.

---

### Day 42 — Quadrature Diffusion

#### Build
- Initialize a coherent state $|\alpha=3\rangle$.

#### Simulate
- Run a single trajectory monitoring the $\hat{x}$ quadrature.

#### Plot
- Plot the expectation value $\langle \hat{x}(t) \rangle$ over time. Observe that it does not follow the smooth decay of `mesolve`, but diffuses randomly due to measurement backaction.

#### Investigate
- Run 50 trajectories. Plot all 50 $\langle \hat{x}(t) \rangle$ traces on the same graph as a semi-transparent spaghetti plot. Overlay the thick, smooth `mesolve` average.

#### Learn
- How continuous measurement forces the quantum state to undergo random walks in phase space conditioned on the specific noise record.

---

### Day 43 — Conditional Squeezing (Measurement Backaction)

#### Build
- Initialize a thermal state (a broad, circular blob in phase space).

#### Simulate
- Monitor the $\hat{x}$ quadrature strongly.

#### Plot
- Track the conditional variance $\Delta x^2(t)$ for a single trajectory.
- Plot $\Delta x^2(t)$ vs time. Observe that it rapidly drops *below* the vacuum limit!

#### Investigate
- Animate the Wigner function for this single trajectory. Watch the broad thermal state collapse into a highly squeezed ellipse shifting randomly left and right.

#### Learn
- The act of continuous measurement actually *purifies* and *squeezes* the state relative to the observer's knowledge.

---

### Day 44 — Unconditional Recovery

#### Build
- Use the thermal state and homodyne monitoring setup from Day 43.

#### Simulate
- Run 500 stochastic trajectories.

#### Plot
- Average the density matrices of all 500 final states.
- Plot the Wigner function of this ensemble average.

#### Investigate
- Extract the variance of the ensemble average. Prove numerically that it perfectly matches the broad, unsqueezed thermal state predicted by the deterministic `mesolve`.

#### Learn
- "Ignorance is mixedness." If you average over all measurement records (discarding the info), the conditional squeezing disappears, and the master equation is recovered.

---

### Day 45 — Inefficient Detection

#### Build
- Add an efficiency parameter $\eta \in [0, 1]$ to the measurement operator (representing detector loss).

#### Simulate
- Sweep $\eta$ from $0.1$ to $1.0$.

#### Plot
- Plot the steady-state conditional variance $\Delta x^2$ as a function of detector efficiency $\eta$.

#### Investigate
- Extract the critical efficiency threshold required to observe squeezing below the vacuum limit.

#### Learn
- Real detectors are imperfect. You learn how unobserved information leaks into the environment, diluting the measurement-induced squeezing.

---

### Visual Goals

- Noisy photocurrent records and FFT noise spectra
- "Spaghetti plots" of 50 diffusing trajectories
- Wigner animations of thermal states collapsing into wandering squeezed ellipses
- Variance plots breaking the vacuum limit

---

### Numerical Investigation

Explore:
- FFT analysis of stochastic time-series arrays.
- Computing ensemble averages over hundreds of large density matrices.
- Extracting limits and thresholds from measurement efficiency sweeps.

---

### Research Connection

Connect to:
- Feedback control in optomechanics.
- Generation of deterministic squeezing via measurement.
- State estimation and filtering in continuous-variable quantum systems.

---

### Final Outcome

You have mastered measurement theory. You can simulate homodyne detectors, process the simulated noisy photocurrent, and dynamically update the system state conditioned on that specific noise record.

---

## Block 10: Cavity QED & Approximation Breakdowns (Days 46–50)

### Main Goal
Simulate the Jaynes-Cummings model, extract non-trivial spectral frequencies via FFT, and rigorously computationally stress-test the Rotating Wave Approximation (RWA) until it fails.

---

### Big Project
Simulate a qubit coupled to a coherent cavity field, extract the quantized Rabi frequencies via Fourier analysis to prove the field is discrete, and map the breakdown of the RWA at ultrastrong coupling.

---

### Key Equations

$$
H_{Rabi} = \omega_c a^\dagger a + \frac{\omega_q}{2}\sigma_z + g(a+a^\dagger)(\sigma_+ + \sigma_-)
$$

$$
H_{JC} = \omega_c a^\dagger a + \frac{\omega_q}{2}\sigma_z + g(a^\dagger \sigma_- + a \sigma_+)
$$

---

### Day 46 — Vacuum Rabi Splitting

#### Build
- Tensor a two-level qubit with a cavity mode. Define the Jaynes-Cummings Hamiltonian $H_{JC}$ on resonance ($\omega_c = \omega_q$).

#### Simulate
- Evolve the initial state $|e, 0\rangle$ (excited qubit, vacuum cavity).

#### Plot
- Plot $\langle \sigma_z \rangle$ and $\langle \hat{a}^\dagger\hat{a} \rangle$ to show perfectly out-of-phase vacuum Rabi oscillations.

#### Investigate
- Compute the eigenvalues of $H_{JC}$. Sweep the detuning $\Delta = \omega_c - \omega_q$.
- Plot the eigenenergies vs detuning. Extract the minimum gap size at $\Delta=0$ and verify it equals exactly $2g$ (the avoided crossing).

#### Learn
- Building hybrid discrete/continuous tensor spaces and observing the fundamental hybridization of light and matter.

---

### Day 47 — Collapse and Revival

#### Build
- Initialize the qubit in $|e\rangle$ and the cavity in a coherent state $|\alpha=4\rangle$.

#### Simulate
- Evolve under $H_{JC}$ for a long time $T \sim 20\pi/g$.

#### Plot
- Plot $\langle \sigma_z(t) \rangle$. Observe the initial rapid decay (collapse) followed by periods of quiescence and subsequent revivals of oscillation.

#### Investigate
- Isolate the array data for the first collapse. Fit the envelope to a Gaussian $e^{-t^2/2\tau_c^2}$. Extract $\tau_c$ and compare to the analytical $1/(g\sqrt{\bar{n}})$.

#### Learn
- The classical field causes Rabi oscillations, but the *discrete photon nature* of the field causes the dephasing (collapse) and rephasing (revival).

---

### Day 48 — Spectral Extraction (FFT)

#### Build
- Take the highly complex, multi-frequency $\langle \sigma_z(t) \rangle$ time-series array from Day 47.

#### Simulate
- Pass the data through `scipy.fft.fft`.

#### Plot
- Plot the power spectrum. You will see a discrete "comb" of peaks.

#### Investigate
- Use `scipy.signal.find_peaks` to programmatically extract the frequencies of the peaks.
- Plot these extracted frequencies against $\sqrt{n}$. Prove via linear fit that the frequencies strictly follow the quantized Rabi scaling $\Omega_n = 2g\sqrt{n+1}$.

#### Learn
- How to extract deep quantum physics (field quantization) hidden inside complex time-domain signals using standard signal processing.

---

### Day 49 — The RWA Breakdown

#### Build
- Define both the full Quantum Rabi model ($H_{Rabi}$) and the approximated Jaynes-Cummings model ($H_{JC}$).

#### Simulate
- Start in $|e, 0\rangle$. Set the coupling ratio $g/\omega = 0.01$ (weak). Evolve both and plot them. They match perfectly.
- Set $g/\omega = 0.3$ (ultrastrong). Evolve both.

#### Plot
- Plot the two evolutions overlayed. Observe the JC model completely failing to capture the fast, highly complex oscillations of the full Rabi model.

#### Investigate
- Sweep $g/\omega$ from $0.01$ to $0.5$. Calculate the maximum trace distance between the states over one period. Plot Error vs Coupling Ratio. Extract the exact threshold where the error exceeds $5\%$.

#### Learn
- A rigorous, computational understanding of when and why standard theoretical approximations fail.

---

### Day 50 — Dispersive Qubit Readout

#### Build
- Use $H_{JC}$. Set a massive detuning $\Delta = 10g$ (dispersive regime).

#### Simulate
- Initialize the cavity in $|\alpha=2\rangle$. Evolve twice: once with the qubit in $|g\rangle$, once with the qubit in $|e\rangle$.

#### Plot
- Plot the final Wigner functions for the cavity in both scenarios.

#### Investigate
- Observe that the coherent blob rotates clockwise for $|g\rangle$ and counter-clockwise for $|e\rangle$.
- Calculate the overlap integral between the two cavity states. Plot this overlap vs interaction time to determine exactly when the states become orthogonal (perfect distinguishability for measurement).

#### Learn
- The core mechanism behind modern superconducting qubit readout (cQED): mapping discrete qubit states onto distinguishable continuous-variable cavity phase shifts.

---

### Visual Goals

- Avoided crossing energy level diagrams
- Beautiful, long-time collapse and revival time-series plots
- FFT combs of quantized Rabi frequencies
- Error scaling phase diagrams for RWA breakdown
- Wigner plots of dispersively shifted cavity states

---

### Numerical Investigation

Explore:
- FFT peak finding algorithms on noisy/complex simulation data.
- Quantifying the exact error of theoretical approximations via Trace Distance.
- Fitting Gaussian envelopes to extract macroscopic coherence times.

---

### Research Connection

Connect to:
- Superconducting qubit readout (Circuit QED).
- Ultrastrong coupling regimes in polariton physics.
- Proof of field quantization (Haroche).

---

### Final Outcome

You can simulate light-matter interaction precisely, extract hidden frequencies from the dynamics, and you know exactly when standard theoretical models break down and require full numerical simulation.

---

## Block 11: Driven-Dissipative Systems & Spectra (Days 51–55)

### Main Goal
Move to frequency-space analysis of open quantum systems, extracting emission spectra (Mollow triplets) and calculating the eigenvalues of the Liouvillian to find critical slowing down.

---

### Big Project
Drive a lossy two-level atom heavily, compute its steady-state emission spectrum, extract the sideband properties, and analyze the full complex spectrum of the Liouvillian superoperator.

---

### Key Equations

$$
S(\omega) \propto \text{Re} \int_0^\infty \langle \sigma_+(t)\sigma_-(0) \rangle_{ss} e^{-i\omega t} dt
$$

$$
\mathcal{L}(\rho_{ss}) = 0
$$

---

### Day 51 — The Correlation Function

#### Build
- Set up a driven, lossy TLS: $\hat{H} = \Omega \sigma_x$, $\hat{C} = \sqrt{\Gamma}\sigma_-$.

#### Simulate
- Use `qutip.correlation_2op_1t` to calculate the steady-state two-time correlation function $\langle \sigma_+(t)\sigma_-(0) \rangle$.

#### Plot
- Plot the real and imaginary parts of the correlation function vs time delay $t$. Observe the damped oscillations.

#### Investigate
- Fit the decay envelope of the correlation function. Compare the extracted decay rate to the system's dissipation rate $\Gamma$.

#### Learn
- How the quantum regression theorem is implemented numerically to find multi-time correlations.

---

### Day 52 — The Mollow Triplet

#### Build
- Pass the correlation function data to `scipy.fft` (or use `qutip.spectrum` directly).

#### Simulate
- Compute the emission spectrum $S(\omega)$ for a strong drive $\Omega = 5\Gamma$.

#### Plot
- Plot the spectrum. You will see a central peak and two distinct sidebands (the Mollow Triplet).

#### Investigate
- Write a script to locate the sideband peaks. Extract their frequency distance from the center. Prove numerically that they sit exactly at $\pm 2\Omega$.
- Extract the Full Width at Half Maximum (FWHM) of the central peak and sidebands.

#### Learn
- How strongly driving a quantum system splits its energy levels (AC Stark shift) and completely alters its emission spectrum.

---

### Day 53 — Steady-State Solver Profiling

#### Build
- Construct a large driven-dissipative cavity system (e.g., $N=100$).

#### Simulate
- Use `qutip.steadystate` with three different internal algorithms: `direct`, `eigen`, and `iterative-gmres`.

#### Plot
- Sweep the dimension $N$. Plot the runtime of all three solvers on a log-log plot.

#### Investigate
- Extract the big-O scaling exponent for each method.
- Determine the threshold dimension where the `direct` dense linear algebra solver fails and sparse `iterative-gmres` becomes necessary.

#### Learn
- Advanced computational profiling. Finding the null space of a Liouvillian matrix is hard; you learn which solver to use when scaling up.

---

### Day 54 — Liouvillian Eigenvalues

#### Build
- Construct the full Liouvillian superoperator object `L = qutip.liouvillian(H, c_ops)`.

#### Simulate
- Compute all the complex eigenvalues $\lambda_i$ of `L`.

#### Plot
- Scatter plot the eigenvalues on the complex plane.
- Observe that they all have negative real parts (decaying), except for exactly one eigenvalue at the origin $0 + 0i$ (the steady state).

#### Investigate
- Find the eigenvalue with the *smallest non-zero real part*. This is the Asymptotic Decay Rate (ADR).
- Plot the ADR vs drive strength $\Omega$.

#### Learn
- The deep mathematical structure of open systems. The eigenvalues of the Liouvillian dictate every timescale in the system.

---

### Day 55 — Critical Slowing Down

#### Build
- Define a Kerr oscillator with two-photon driving (a system known to have a phase transition): $\hat{H} = \chi \hat{a}^{\dagger 2}\hat{a}^2 + \Omega(\hat{a}^2 + \hat{a}^{\dagger 2})$. Add single photon loss $\kappa$.

#### Simulate
- Compute the eigenvalues of the Liouvillian.

#### Plot
- Sweep the drive strength $\Omega$ across the known critical point.
- Plot the extracted ADR vs $\Omega$.

#### Investigate
- Observe that the ADR plummets toward zero at the critical point. This means the system takes infinitely long to reach the steady state (Critical Slowing Down).
- Extract the exact critical drive $\Omega_c$ by finding the minimum of the ADR curve.

#### Learn
- How to numerically detect driven-dissipative quantum phase transitions using pure matrix analysis, without needing to simulate dynamics over time.

---

### Visual Goals

- Damped correlation functions
- Mollow Triplet spectral plots with marked FWHM
- Log-log runtime solver benchmarks
- Complex plane scatter plots of Liouvillian eigenvalues
- Critical slowing down "dip" plots

---

### Numerical Investigation

Explore:
- Benchmarking null-space linear algebra solvers (`direct` vs `iterative`).
- Extracting exact spectral linewidths computationally.
- Identifying phase boundaries by mapping the Liouvillian gap.

---

### Research Connection

Connect to:
- Resonance fluorescence experiments.
- Dissipative quantum phase transitions.
- Open-system quantum simulation and cooling.

---

### Final Outcome

You are now a master of frequency-space and steady-state analysis. You can extract emission spectra, profile heavy linear algebra solvers, and detect phase transitions strictly from the spectrum of the Liouvillian.

---

## Block 12: Capstone Project — Squeezed Optomechanics (Days 56–60)

### Main Goal
Synthesize everything learned into a massive, multi-mode, parameterized research project. Build an optomechanical system, cool the mechanics, inject squeezed light, and run a high-resolution phase diagram sweep.

---

### Big Project
Simulate a high-frequency optical cavity coupled to a low-frequency mechanical mirror. Find the limits of sideband cooling, inject squeezed vacuum to break the quantum backaction limit, and generate a massive 2D optimization map using parallel processing.

---

### Key Equations

$$
\hat{H}_{int} = -g_0 \hat{a}^\dagger\hat{a} (\hat{b} + \hat{b}^\dagger)
$$

$$
\text{Limit:} \quad \langle \hat{b}^\dagger \hat{b} \rangle_{min} = \frac{\kappa^2}{16\omega_m^2}
$$

---

### Day 56 — The Cross-Kerr Interaction

#### Build
- Tensor an optical cavity mode $\hat{a}$ with a mechanical oscillator mode $\hat{b}$.
- Define $\hat{H}_{int} = -g_0 \hat{a}^\dagger\hat{a} (\hat{b} + \hat{b}^\dagger)$.

#### Simulate
- Initialize the cavity in a coherent state $|\alpha\rangle$ and the mechanics in vacuum. Evolve.

#### Plot
- Plot the steady-state mechanical displacement $\langle \hat{x}_m \rangle$ as a function of optical photon number $\langle \hat{n}_{opt} \rangle$.

#### Investigate
- Perform a linear fit. Verify that the mechanical equilibrium position shifts exactly proportionally to the radiation pressure force from the optical field.

#### Learn
- Setting up macroscopic interaction Hamiltonians where disparate energy scales ($\omega_{opt} \gg \omega_{mech}$) couple via radiation pressure.

---

### Day 57 — Optomechanical Sideband Cooling

#### Build
- Drive the optical cavity precisely at the red-sideband: $\Delta = \omega_{laser} - \omega_{cavity} = -\omega_m$.
- Add a hot thermal bath to the mechanical mode, and rapid decay $\kappa$ to the optical mode.

#### Simulate
- Solve for the steady-state density matrix.

#### Plot
- Plot the final mechanical phonon number $\langle \hat{b}^\dagger\hat{b} \rangle_{ss}$ vs the optical drive strength.

#### Investigate
- Observe that as drive increases, phonons decrease (cooling), but at extremely high drives, the phonon number rises again.
- Extract the absolute minimum achievable phonon number. Compare it to the theoretical quantum backaction limit $(\kappa/4\omega_m)^2$.

#### Learn
- The exact physics of sideband cooling, and how measurement backaction (shot noise heating) limits macroscopic ground-state cooling.

---

### Day 58 — Squeezed Injection Breakdown

#### Build
- Replace the standard optical vacuum bath with a broadband squeezed vacuum bath.
- Define the new squeezed collapse operators for the cavity.

#### Simulate
- Rerun the steady-state cooling sweep from Day 57.

#### Plot
- Plot the final phonon number vs drive strength for standard vacuum vs squeezed vacuum.

#### Investigate
- Verify numerically that injecting squeezed light at the correct angle suppresses the measurement backaction, allowing the mechanics to be cooled *below* the standard quantum limit.
- Extract the new minimum phonon limit.

#### Learn
- Advanced quantum engineering: utilizing engineered continuous-variable noise (squeezing) to actively suppress thermodynamic limits in a macroscopic system.

---

### Day 59 — Constructing the Phase Diagram

#### Build
- Wrap the entire optomechanical steady-state solver into a single functional block taking arguments: (Drive Strength $\Omega$, Squeezing Angle $\theta$).

#### Simulate
- Use `qutip.parallel_map` (or Python's `multiprocessing`) to run the solver across a massive 2D grid of $50 \times 50$ parameter combinations.

#### Plot
- Render the output matrix as a high-resolution 2D heatmap of Final Phonon Number.

#### Investigate
- Overlay contour lines indicating the exact boundaries of the "Ground State Cooling" regime ($\langle n \rangle < 1$).
- Programmatically locate the single global minimum in the matrix.

#### Learn
- Scaling a QuTiP script to utilize all CPU cores for massive parameter space exploration.

---

### Day 60 — The Final Extraction

#### Build
- Extract the global minimum parameter set $(\Omega_{opt}, \theta_{opt})$ from Day 59.

#### Simulate
- Run a final, high-resolution time-dynamic `mesolve` starting from a highly thermal state, using the optimal parameters.

#### Plot
- Generate a final animated Wigner function of the mechanical mode, watching it spiral from a massive, diffuse thermal blob down into a tight, pure, sub-quantum-limit state near the origin.

#### Investigate
- Calculate the entanglement entropy between the optical and mechanical modes at the steady state.
- Prove that the light and mirror are fundamentally entangled in the cooling process.

#### Learn
- Total mastery. You have built a complex, multi-mode, open quantum system, mapped its entire parameter space, found the optimal operating point, proved it beats standard limits, and extracted the fundamental entanglement generating the effect.

---

### Visual Goals

- Displacement vs photon number linear fits
- U-shaped cooling curves showing the backaction limit
- Side-by-side comparison plots of vacuum vs squeezed cooling
- Massive, high-resolution 2D heatmaps with optimal contour boundaries
- Final Wigner animation of a macroscopic object cooling to the ground state

---

### Numerical Investigation

Explore:
- Applying non-standard squeezed bath collapse operators.
- Using `parallel_map` to fully utilize multicore CPUs for matrix sweeps.
- Verifying the extraction of global minimums from noisy, massive arrays.

---

### Research Connection

Connect to:
- LIGO's macroscopic mirror cooling and squeezed injection.
- Creating macroscopic entangled states (optomechanical entanglement).
- PhD-level computational parameter search and optimization.

---

### Final Outcome

You have successfully completed a project that is roughly equivalent to reproducing a major optomechanics paper from *Physical Review Letters*. You are completely prepared to begin a PhD in computational quantum optics.