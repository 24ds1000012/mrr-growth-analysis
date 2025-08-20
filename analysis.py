"""
SaaS MRR Growth Analysis
Author: 24ds1000012@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("mrr_growth_2024.csv")
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
    plt.axhline(y=target, linestyle="--", label="Industry Target (15%)")
    plt.axhline(y=avg, linestyle=":", label=f"Avg Growth ({avg}%)")
    plt.xticks(df["Quarter_Num"], df["Quarter"])
    plt.title("MRR Growth by Quarter (2024) vs Target")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth (%)")
    plt.legend()
    plt.grid(True, axis="y")
    plt.tight_layout()
    plt.savefig("mrr_growth_vs_target.png", dpi=200)

    # Simple projection
    next_q = pd.DataFrame({
        "Quarter": ["Q1 2025", "Q2 2025"],
        "Base_Trend": [df["MRR_Growth"].iloc[-1] * 0.95, df["MRR_Growth"].iloc[-1] * 0.95],
    })
    next_q["New_Segments_Lift"] = [2.0, 2.5]
    next_q["Projected_Growth"] = next_q["Base_Trend"] + next_q["New_Segments_Lift"]
    print("\nProjection with Market Expansion:")
    print(next_q)

    next_q.to_csv("projection_2025.csv", index=False)

if __name__ == "__main__":
    main()
