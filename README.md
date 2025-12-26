# Baseball Analytics in Python

Translating baseball analytics concepts from "Analyzing Baseball Data with R" to Python.

## About

This repository contains Python implementations of statistical analyses from the book "Analyzing Baseball Data with R", translated into Python's data science stack (pandas, matplotlib, seaborn, scikit-learn).

**Chapters:** 
- Starting from Chapter 4 (Chapters 1-3 focuses on R installation and basics)  

**Data:**
- Extended through 2024 season (book uses data through 2022) so some metrics will slightly differ from the book

## Installation

```bash
pip install -r requirements.txt
```

## Notebooks

- [04 - The Relation Between Runs and Wins](notebooks/04_runs_and_wins.ipynb) - Linear regression, Pythagorean expectation
- [05 - Value of Plays Using Run Expectancy](notebooks/05_run_expectancy.ipynb) - Run expectancy matrices, base-out states
- [06 - Balls and Strikes Effects](notebooks/06_balls_and_strikes_effects.ipynb) - Count effects on batting outcomes/pitch sequencing analysis
- [07 - Catcher Framing](notebooks/07_catcher_framing.ipynb) - Measuring catcher pitch framing ability and strike zone boundaries

## Credit

- **Book:** [Analyzing Baseball Data with R](https://a.co/d/7Mjuz71) by Max Marchi, Jim Albert, and Benjamin S. Baumer
- **Book Website:** [Baseball With R (3rd Edition)](https://beanumber.github.io/abdwr3e/)
- **Original R Code:** [Baseball R Repository](https://github.com/beanumber/baseball_R)

All Python code is original but examples directly follow the book
