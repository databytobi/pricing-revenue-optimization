import numpy as np
import pandas as pd

np.random.seed(42)

def generate_pricing_data(n=3000):
    segments = ["Student", "Regular", "Premium"]

    elasticity = {
        "Student": -1.8,
        "Regular": -1.1,
        "Premium": -0.4
    }

    base_price = {
        "Student": 10,
        "Regular": 15,
        "Premium": 25
    }

    rows = []

    for _ in range(n):
        segment = np.random.choice(segments)
        price = round(np.random.normal(base_price[segment], 2), 2)
        competitor_price = round(price * np.random.uniform(0.9, 1.1), 2)
        promotion = np.random.choice([0, 1], p=[0.7, 0.3])

        base_demand = 120
        demand = (
            base_demand
            * (price / base_price[segment]) ** elasticity[segment]
            * (1.2 if promotion else 1)
            * np.random.normal(1, 0.1)
        )

        units_sold = max(int(demand), 0)

        rows.append([
            segment,
            price,
            competitor_price,
            promotion,
            units_sold
        ])

    return pd.DataFrame(
        rows,
        columns=[
            "segment",
            "price",
            "competitor_price",
            "promotion",
            "units_sold"
        ]
    )


if __name__ == "__main__":
    df = generate_pricing_data()
    df.to_csv("data/raw/simulated_pricing_data.csv", index=False)
    print("✅ Simulated pricing data saved to data/raw/")