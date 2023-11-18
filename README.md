# Artificial Intelligence Exam Project Repository

This repository contains the code and documentation for the Artificial Intelligence exam project. The project focuses on the topic of "Inference with Junction Trees on Belief Networks." Below, you will find information about the repository's structure and contents.

## Repository Structure

- **Main Branch:** This branch provides information about the dataset used, instructions on how to plot data, and a descriptive report of the code.

- **Software Module:** This module contains two main Python files:

    - `Inference.py`: This file includes classes for Junction Trees and Belief Networks, as well as methods for performing probabilistic inference.
    
    - `Main.py`: This file demonstrates the usage of the inference software and its capabilities.

## About the Project

The project's primary goal is to develop a software module for propagating information within Belief Networks. It utilizes an algorithm based on message passing within a manually constructed Junction Tree associated with the Belief Network. Please note that the part of the algorithm responsible for converting a Belief Network into its corresponding Junction Tree is not included in this repository. Users are expected to perform this transformation independently, especially for small networks.

## Testing

The functionality of the module has been rigorously tested on two example networks:

1. [earthquake.bn](https://github.com/ncullen93/pyBN/blob/master/data/earthquake.bn)
2. [simple.bn](https://github.com/ncullen93/pyBN/blob/master/data/simple.bn)

Additionally, there is an extra folder that provides insights into the structure of the Junction Trees associated with these simple networks.

Feel free to explore the code, documentation, and test cases provided in this repository. [Inference.py](https://github.com/francescobaio/junctionTrees_beliefNetworks/blob/main/README.inference.py)




