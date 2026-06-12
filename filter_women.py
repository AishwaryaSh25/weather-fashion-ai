import pandas as pd

df = pd.read_csv(
    "styles.csv",
    on_bad_lines="skip"
)

women_df = df[
    df["gender"].isin(
        ["Women", "Girls"]
    )
]

women_df.to_csv(
    "women_fashion.csv",
    index=False
)

print(
    "Total women products:",
    len(women_df)
)