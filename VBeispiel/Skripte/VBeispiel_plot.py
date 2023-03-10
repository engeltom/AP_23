import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Angaben
path = "../Daten/VBeispiel_daten.csv"

# Schriftart
tex_fonts = {
    "text.usetex": True,
    "font.family": "serif",
    "axes.labelsize": 10,
    "font.size": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8
}
plt.rcParams.update(tex_fonts)

# Höhere Auflösung
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

# Daten einlesen
data = pd.read_csv(path)
xdata = data["num"]
ydata = np.log(data["val"])

# Plot
lp = sns.lineplot(x=xdata, y=ydata, color="black", label="Line", zorder=1)
sp = sns.scatterplot(x=xdata, y=ydata, color="red", marker="x", label="Scatter", zorder=2)
sp.set(xlabel=r"$x$", ylabel=r"$y$")

# Speichern / Anzeigen
plt.savefig("../Ressourcen/VBeispiel_plot.svg", format="svg")
plt.show()

"""
Dokumentation
https://seaborn.pydata.org/index.html
https://seaborn.pydata.org/tutorial/properties.html
"""