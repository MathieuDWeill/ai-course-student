# Google Trends Weak Signals - France

## What this dataset is

Weekly Google Trends snapshots for France, covering three public search signals:

- `chatgpt`
- `iphone`
- `meteo`

Files included:

- `iot_FR_today_12-m_chatgpt_iphone_meteo.csv`: last 12 months, weekly values.
- `iot_FR_today_5-y_chatgpt_iphone_meteo.csv`: last 5 years, weekly values.

The dataset is designed for data science teaching, exploratory analysis, time-series storytelling, and simple public Kaggle notebooks.

## Why it matters

Google Trends is useful for studying attention signals: how public interest changes over time, how topics compare, and how peaks appear around product, technology, or seasonal events.

This dataset is small, readable, and reproducible enough for:

- beginner-friendly EDA;
- pandas cleaning exercises;
- visualization storytelling;
- baseline time-series analysis;
- public portfolio notebooks.

## Fields

| Field | Description |
|---|---|
| `date` | Weekly timestamp for the Google Trends observation. |
| `chatgpt` | Relative search interest for ChatGPT in France. |
| `iphone` | Relative search interest for iPhone in France. |
| `meteo` | Relative search interest for weather-related searches in France. |

Values are Google Trends indexes normalized from 0 to 100 within the query context and timeframe.

## How to use

```python
import pandas as pd

df = pd.read_csv("/kaggle/input/google-trends-weak-signals-france/iot_FR_today_5-y_chatgpt_iphone_meteo.csv")
df["date"] = pd.to_datetime(df["date"])
df.head()
```

Example analysis:

```python
signals = ["chatgpt", "iphone", "meteo"]
df.set_index("date")[signals].rolling(4).mean().plot(figsize=(12, 5))
```

## Practical use cases

- Compare stable seasonal demand (`meteo`) with product attention (`iphone`) and technology adoption (`chatgpt`).
- Teach EDA with small, understandable time series.
- Build a notebook story around public attention shifts.
- Create simple features such as rolling averages, peaks, growth rates, and trend changes.
- Practice clear limitations writing for public notebooks.

## Limitations

- Google Trends measures relative search interest, not market size, revenue, adoption, or causality.
- Values are normalized by Google and depend on query context, region, and timeframe.
- The dataset is a snapshot, not a live API feed.
- Weekly granularity is useful for teaching but not for high-frequency analysis.
- Topic interpretation should be cautious, especially for ambiguous terms.

## Suggested Kaggle notebook follow-up

Recommended first notebook:

**From Search Signals to Data Story: Google Trends EDA in France**

Structure:

1. Load and validate the data.
2. Compare 12-month and 5-year views.
3. Smooth signals with rolling averages.
4. Identify peaks and shifts.
5. Write one decision-oriented insight.
6. Document limitations clearly.
