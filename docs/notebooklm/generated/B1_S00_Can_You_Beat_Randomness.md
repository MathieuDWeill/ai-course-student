# B1_S00 — Can You Beat Randomness?

Source notebook: `notebooks/01_python_data_science/B1_S00_Can_You_Beat_Randomness.ipynb`

## Decision Problem

Not explicitly stated.

## Key Concepts

- data quality
- exploratory analysis
- model validation
- business decision

## Course Notes

# B1_S00 — Can You Beat Randomness?

## Opening hook

**Can you beat randomness?**

EuroMillions looks simple: 5 main numbers, 2 Lucky Stars, one draw, one dream.

But before learning pandas, visualization, or machine learning, students need a more important lesson:

> Humans are pattern-making machines. Randomness is where that instinct becomes dangerous.

Questions for the room:

- Do some numbers come out more often?
- Are there hot numbers?
- Are there cursed numbers?
- Can we detect a real pattern?
- Or are we just seeing shapes in noise?

This notebook is **not** about predicting lottery numbers. It is about learning why Data Science often starts by proving that a pattern is fake.

## Decision problem

When we see historical data, how do we know whether a visible pattern is meaningful or just randomness doing what randomness does?

Dataset: **EuroMillions Historical Data** by Duarte Pereira da Cruz on Kaggle. It contains historical EuroMillions draws from 2004 to present, including draw dates, five main numbers, two Lucky Stars, and jackpot/rollover context when available.

## Load the Kaggle dataset

On Kaggle, add the dataset **EuroMillions Historical Data** to the notebook input. Locally, place the CSV anywhere under `data/`, `datasets/`, `kaggle/`, or the repo root.

The notebook intentionally fails with a clear message if the dataset is missing. We do not generate fake lottery history.

## Prepare draw columns

Kaggle datasets can evolve. Instead of hard-coding one schema too aggressively, we detect likely main-number and Lucky Star columns from names and values.

# 1. Frequency analysis

The first temptation is simple: count which numbers came out most often.

This is where intuition starts whispering: “that number wins more.”

The statistical question is sharper:

> Is the difference surprising, or is it normal variation?

## Does one number really “win more”?

A number can be above average without being special.

In random systems, someone is always first. Someone is always last. That does not mean the leader has a hidden force.

# 2. Hot numbers vs cold numbers

Hot/cold lists are seductive because they turn noise into a story.

But a story is not evidence.

## Gambler’s fallacy

The gambler’s fallacy says: “This number has not appeared for a while, so it is due.”

But in a fair draw, the machine does not remember.

An overdue number is not a promise. It is a feeling.

# 3. Human bias

Even if randomness is fair, humans can still play badly.

Why?

- **Birthdays effect:** many people choose 1–31, ignoring 32–50.
- **Favorite numbers:** people cluster around memorable numbers.
- **Pattern preference:** sequences, diagonals, symmetry, and “nice looking” tickets feel meaningful.
- **Narrative bias:** we invent explanations after seeing results.

This does not change the draw probability. It changes how many people may share a prize if common numbers win.

Reflection question:

Even if every combination has the same probability, why might a human-selected ticket be strategically worse than a random ticket?

# 4. Monte Carlo simulation

Now we compare intuition with pure randomness.

If the real draw is fair, simulated random draws should also produce “hot” numbers, “cold” numbers, and overdue numbers.

That is the point: randomness naturally creates patterns that look suspicious.

# 5. Statistical interpretation

Key ideas:

**Law of large numbers**  
As the number of draws grows, frequencies tend to move closer to expected proportions. But “closer” does not mean “perfectly equal.”

**Variance**  
Random systems fluctuate. Variation is not automatically signal.

**Randomness illusion**  
Humans expect randomness to look balanced. Real randomness often looks streaky, clustered, and unfair.

**False signal detection**  
A core Data Science skill is not finding patterns. It is testing whether the pattern deserves belief.

# Final lesson

Data Science is often not about finding patterns.

It is about proving that some patterns are fake.

Students should leave remembering:

> **Randomness is not intuitive. Data Science starts when intuition fails.**

## Practical Activities

### Code activity 1

create charts

### Code activity 2

load course data

### Code activity 3

run a practical notebook step

### Code activity 4

save reusable artifacts

### Code activity 5

create charts

### Code activity 6

save reusable artifacts

### Code activity 7

save reusable artifacts

### Code activity 8

save reusable artifacts

### Code activity 9

save reusable artifacts

### Code activity 10

create charts

### Code activity 11

save reusable artifacts

## Expected Outputs

- No saved output artifact detected.

## Reflection Questions

- # B1_S00 — Can You Beat Randomness?
- Do some numbers come out more often?
- Are there hot numbers?
- Are there cursed numbers?
- Can we detect a real pattern?
