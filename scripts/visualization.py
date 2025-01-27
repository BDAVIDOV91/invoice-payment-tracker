import os
import sys

import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scripts.query_utils as qu


def plot_paid_vs_overdue():
    paid_invoices = qu.get_paid_invoices()
    overdue_invoices = qu.get_overdue_invoices()

    labels = ["Paid", "Overdue"]
    sizes = [len(paid_invoices), len(overdue_invoices)]
    colors = ["#4CAF50", "#FF5733"]
    explode = (0.1, 0)  # explode the 1st slice (Paid)

    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )

    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Paid vs Overdue Invoices")
    plt.show()


if __name__ == "__main__":
    plot_paid_vs_overdue()
