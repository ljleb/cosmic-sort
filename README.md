# Cosmic Sort
Cosmic sort is a parallel [bogosort](https://en.wikipedia.org/wiki/Bogosort) implementation that relies on cosmic rays to randomly flip bits in memory.

## Features

- Bitwise Parallellization: Every bit in memory has the same chance to be simultaneously flipped at any time
- Proper Output: Unlike traditional implementations (see for example [this one](https://github.com/cincottash/CosmicRaySort)), the output of the algorithm will never contain garbage as the algorithm keeps track of memory corruption and restores exceptional values to reflect the input distribution


## Todo

- [ ] code section redundancy: take into consideration corruption of the python interpreter memory
