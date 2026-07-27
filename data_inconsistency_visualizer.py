# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:46:26 2022

@author: Ganesh Gajjala

Script to visualize data inconsistency distributions using a donut chart.
"""

import matplotlib.pyplot as plt


def plot_inconsistency_donut():
    """Generates and saves a donut chart of data inconsistencies."""
    # Global plot configurations
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["figure.dpi"] = 300

    # Data configuration
    pie_labels = [
        "Bohrintervalle mit \ninkorrekte Orts- oder \nTiefeninformationen \n(4.98%)",
        "Inkonsistenz im \nMassenprozentsatz \n(3.1%)",
        "Kurzformen nicht\nvorhanden \n(3.03%)",
        "Überlappung der\nKornfraktionen \n(2.25%)",
        "\nKurzformen mit\nvereinzelt (1.63%)",
        "Nicht plausible Kornübergänge (0.25%)",
        "Wiederholung der Kurzform (0.23%)",
        "Keine Hauptbestandteile (0.015%)",
    ]

    pie_share = [61930, 38518, 37749, 27937, 20359, 3155, 2854, 182]

    # Visual design elements
    colors = [
        "dimgrey",
        "grey",
        "darkgrey",
        "silver",
        "lightgrey",
        "gainsboro",
        "gainsboro",
        "black",
    ]

    explode_tuple = (0.025, 0.025, 0.025, 0.025, 0.025, 0.075, 0.215, 0.35)

    # Figure initialization
    fig, axes_object = plt.subplots(figsize=(7, 6), dpi=240)

    # Plotting the base pie chart
    axes_object.pie(
        pie_share,
        explode=explode_tuple,
        colors=colors,
        labels=pie_labels,
        textprops={"fontsize": 10},
        startangle=90,
    )

    # Converting the pie chart into a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc="white")
    fig.gca().add_artist(centre_circle)

    # Formatting and aesthetics
    axes_object.axis("equal")

    plt.title(
        label="Verteilung von Inkonsistenzen",
        loc="center",
        fontname="Times New Roman",
        pad=25,
        fontsize=16,
        fontweight="bold",
        color="black",
    )

    plt.tight_layout()

    # Save and display the visualization
    plt.savefig("donut.jpg")
    plt.show()


if __name__ == "__main__":
    plot_inconsistency_donut()
