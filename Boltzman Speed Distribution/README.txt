# 2D Gas Simulation (Molecular Dynamics)

This project simulates a bunch of particles moving inside a 2D box and bouncing off the walls and each other.  
The idea was to see how thermodynamic behaviour shows up from simple Newtonian motion.

In short: particles move → collisions happen → pressure and temperature appear.

---

## What the simulation does

- ~10,000 particles inside a square box  
- Elastic wall collisions  
- Elastic particle–particle collisions  
- Time evolution using small timesteps  

From the motion, the code measures:

- Total kinetic energy  
- Temperature  
- Entropy (from the speed distribution)  
- Pressure from wall momentum transfer  

The main goal was to check whether the simulation follows the **2-D ideal gas law**.

---

## Why I made this

This started as a curiosity project while learning statistical mechanics.  
Instead of beginning with formulas, I wanted to start with particles and see if the formulas would show up on their own.

---

## How pressure is measured

Whenever particles hit a wall, they transfer momentum.  
By tracking the total momentum change per unit time and dividing by the wall length, the pressure can be computed directly from the simulation.

---

## Results (short version)

After an initial settling period:

- Energy stays constant (as expected for elastic collisions)
- Pressure becomes the same on all walls
- The measured pressure matches the theoretical prediction

Which means the simulation successfully reproduces the 2-D ideal gas relation.

---

## Tech used

Python, NumPy, PyTorch, Matplotlib, Pandas

---

## Running the simulation

Install dependencies:

pip install numpy torch matplotlib pandas

Then run the main script.

---

## Notes

This was built mainly as a learning project to understand kinetic theory and molecular dynamics from scratch.