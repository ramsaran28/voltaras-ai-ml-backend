import matplotlib.pyplot as plt


def plot_latency(df, output_path: str):
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["latency_ms"], label="Latency (ms)")
    plt.axhline(300, linestyle="--", color="red", label="SLO 300ms")
    plt.xlabel("Time")
    plt.ylabel("Latency (ms)")
    plt.title("Latency Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
