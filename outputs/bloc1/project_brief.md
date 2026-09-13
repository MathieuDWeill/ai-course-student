# Bloc 1 Project Brief

Decision question: which public attention signal deserves monitoring for product decisions?

Key evidence:
         rows  average  median  peak  latest  latest_vs_median
signal                                                        
chatgpt   262     2.90     2.0    13      12              10.0
iphone    262     8.00     8.0    16       8               0.0
meteo     262    44.96    42.0   100      27             -15.0

Model check:
            model  accuracy  f1
         baseline       0.0 0.0
logistic_pipeline       1.0 1.0

Recommendation: use the cleaned Google Trends pipeline as a lightweight weak-signal review, not as proof of demand.
