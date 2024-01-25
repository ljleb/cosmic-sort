# Cosmic Sort
Cosmic sort is a parallel [bogosort](https://en.wikipedia.org/wiki/Bogosort) implementation that relies on cosmic solar radiation to randomly flip bits in memory.

## Features

- Bit-Wise Parallellization: Every bit in memory has the same chance to be simultaneously flipped
- Proper Output: Unlike traditional implementations, the output of the algorithm will never contain garbage as the algorithm keeps track of memory corruption and restores exceptional values to reflect the input distribution
