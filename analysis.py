"""
SaaS MRR Growth Analysis
Author: 24ds1000012@ds.study.iitm.ac.in
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data_path = Path(__file__).parent / "mrr_growth_2024.csv"
    df = pd.read_csv(data_path)
    df["Quarter_Num"] = df.index + 1

    avg = round(df["MRR_Growth"].mean(), 2)
    target = 15.0

    # Print key stats
    print("Quarterly MRR Growth (2024):")
    print(df[["Quarter", "MRR_Growth"]])
    print(f"Average Growth: {avg}")
    print(f"Industry Target: {target}")
    print(f"Gap to Target: {round(target - avg, 2)}")

    # Plot
    plt.figure()
    plt.plot(df["Quarter_Num"], df["MRR_Growth"], marker="o")
    plt.axhline(y=target, linestyle="--")
    plt.axhline(y=avg, linestyle=":")
    plt.xticks(df["Quarter_Num"], df["Quarter"])
    plt.title("MRR Growth by Quarter (2024) vs Target")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth (%)")
    plt.grid(True, axis="y")
    out_path = Path(__file__).parent / "mrr_growth_vs_target.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    print(f"Saved figure to {out_path}")

    # Simple projection for 'expand into new market segments' scenario
    # Assume entering 2 new segments adds +2.0pp and +2.5pp to next two quarters
    # purely illustrative to show how to hit target
    next_q = pd.DataFrame({
        "Quarter": ["Q1 2025", "Q2 2025"],
        "Base_Trend": [df["MRR_Growth"].iloc[-1] * 0.95, df["MRR_Growth"].iloc[-1] * 0.95],  # slight reversion
    })
    next_q["New_Segments_Lift"] = [2.0, 2.5]
    next_q["Projected_Growth"] = next_q["Base_Trend"] + next_q["New_Segments_Lift"]
    print("\nProjection with Market Expansion:")
    print(next_q)

    proj_path = Path(__file__).parent / "projection_2025.csv"
    next_q.to_csv(proj_path, index=False)
    print(f"Saved projection to {proj_path}")

if __name__ == "__main__":
    main()