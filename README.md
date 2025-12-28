# Baseball Analytics in Python

## About

This repository translates baseball analytics concepts from "*Analyzing Baseball Data with R*" to Python using pandas, matplotlib, seaborn, statsmodels, pygam, pybaseball, and scikit-learn.

**Chapters:** 
- Starting from Chapter 4 (Chapters 1-3 cover R installation and basics)
- Chapters 4-8 complete (Chapters 9, 10, and 13 forthcoming) 

**Data:**
- Extended through 2024 season (book uses data through 2022) so some metrics may differ slightly

## Installation

```bash
pip install -r requirements.txt
```

## Notebooks

- [04 - The Relation Between Runs and Wins](notebooks/04_runs_and_wins.ipynb) - Linear regression, Pythagorean expectation
- [05 - Value of Plays Using Run Expectancy](notebooks/05_run_expectancy.ipynb) - Run expectancy matrices, base-out states
- [06 - Balls and Strikes Effects](notebooks/06_balls_and_strikes_effects.ipynb) - Count effects on batting outcomes/pitch sequencing analysis
- [07 - Catcher Framing](notebooks/07_catcher_framing.ipynb) - Measuring catcher pitch framing ability and strike zone boundaries
- [08 - Career Trajectories](notebooks/08_career_trajectories.ipynb) - Modeling player performance over age

## Credit

- **Book:** [Analyzing Baseball Data with R](https://a.co/d/7Mjuz71) by Max Marchi, Jim Albert, and Benjamin S. Baumer
- **Book Website:** [Baseball With R (3rd Edition)](https://beanumber.github.io/abdwr3e/)
- **Original R Code:** [Baseball R Repository](https://github.com/beanumber/baseball_R)

**This project is independent and all Python code is original but examples directly follow the book.  Please support the authors and their work.**
