import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import pandas as pd
from iminuit import Minuit
from iminuit.cost import LeastSquares  # Cost Function

# Setup Colormap
maxColorPerPlot = 3
colormap = mpl.colormaps["plasma"](np.linspace(0, 1, maxColorPerPlot))
# Konstanten um Code lesbarer zu machen
MESSWERTE = 1
FITS = 0

# Read in Data
x, x_err, y, y_err = np.genfromtxt("content/tables/txt/data.txt", unpack=True)

x = unp.uarray(x, x_err)
y = unp.uarray(y, y_err)


def f(x, a, b, c):  # Funktion, die gefittet werden soll
    return a * x * unp.sin(b * x) + c

# Parameters a, b, c, might need educated guessing as start values
a = 5
b = np.pi
c = 10 

# Fit der Funktion an die Daten x, y
loss = LeastSquares(unp.nominal_values(x), unp.nominal_values(y), unp.std_devs(y), f)
m = Minuit(loss, a=a, b=b, c=c)  # starting value for l
m.migrad()  # finds minimum of least_squares function
print(m.hesse())  # accurately computes uncertainties

# Feiner linspace für smoothe plots
x_plot = np.linspace(unp.nominal_values(x)[0], unp.nominal_values(x)[-1], 1000)

# Funktion von x_plot auswerten
y_plot = unp.nominal_values(f(x_plot, *m.values))

# Breite des Konfidenzintervalls
y_conf = unp.nominal_values(unp.sqrt((1 / len(x)) * np.sum((y - f(x, *m.values)) ** 2)))
# darkorange, crimson, deepskyblue, royalblue, firebirck, maroon, blueviolet, indigo, gold, darkgoldenrod, dodgerblue, navy

fig, ax = plt.subplots(1,1)
ax.plot(
    x_plot, 
    y_plot, 
    label="Regression mit Konfidenzintervall", 
    color=colormap[FITS], 
    alpha=1, 
    linestyle="-", 
    linewidth=None, # Default aus matplotlibrc nutzen
    marker="",
    ms=None,
    )
ax.fill_between( # Nicht unbedingt sinnvoll wie hier verwendet, nur showcase
    x_plot,
    (y_plot - y_conf),
    (y_plot + y_conf),
    color=colormap[FITS],
    alpha=0.25,
)
ax.errorbar(
    unp.nominal_values(x),
    unp.nominal_values(y),
    xerr = x_err,
    yerr = y_err,
    label = "Daten", 
    alpha=1, 
    linestyle="", 
    linewidth=None, # Default aus matplotlibrc nutzen
    marker="x",
    ms=None,
    color=colormap[MESSWERTE],
)
ax.grid(True, "major", "both", linestyle = "--")
ax.set_xlabel(r"$x~\text{/}~\unit{\kilo\meter}$", ha="right", x=1)
ax.set_ylabel(r"$y~\text{/}~\unit{\nano\meter}$", ha="right", y=1)
# ax.set_xscale("symlog", base=10)
# ax.set_yscale("symlog", base=10)
# ax.set_xlim([0,1])
# ax.set_ylim([0,1])
# ax.set_xticks(ticks=[1,2,np.pi,4], labels=["1","2",r"$\pi$","4"])
# ax.set_yticks(ticks=[1,2,np.pi,4], labels=["1","2",r"$\pi$","4"])
ax.minorticks_on()
ax.legend(loc="best")
fig.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)  # Padding der Grafik
fig.savefig("build/plot.pdf")
fig.clf()

file = open("build/values.txt", "w")
file.write("Überschrift" + "\n")
file.write("Params = " + str(m.values) + "\n")
file.write("Errors = " + str(m.errors) + "\n")
file.write("\n")
file.write("val_1_m = " + str(2) + "\n")
file.write("val_1_std = " + str(3) + "\n")
file.write("\n")
file.write("\n")
file.write("val_2_a = " + str(0) + "\n")
file.write("val_2_b = " + str(1) + "\n")
file.write("\n")
file.write("val_2_m = " + str(2) + "\n")
file.write("val_2_std = " + str(3) + "\n")
file.write("\n")
file.write("\n")
file.write("\n")
file.write("--------------------------------------------")
file.write("\n")
file.write("\n")
file.write("\n")
file.write("Überschrift 2")
file.close()

# Create String Table from Values
x_range =range(len(x))
x_table = {}
for i in x_range:
    x_table[i] = "{:L}".format(x[i])
    if x_table[i].find(r" \times 10^{") == -1:
        x_table[i] = (
            x_table[i].replace(r"\left(", r"").replace(r" \pm ", r"(")
            + r")"
        )
    else:
        x_table[i] = (
            x_table[i].replace(r"\left(", r"")
            .replace(r" \pm ", r"(")
            .replace(r"\right", r"")
            .replace(r" \times 10^{", r"e")
            .replace(r"}", r"")
        )
        
y_range =range(len(y))
y_table = {}
for i in y_range:
    y_table[i] = "{:L}".format(y[i])
    if y_table[i].find(r" \times 10^{") == -1:
        y_table[i] = (
            y_table[i].replace(r"\left(", r"").replace(r" \pm ", r"(")
            + r")"
        )
    else:
        y_table[i] = (
            y_table[i].replace(r"\left(", r"")
            .replace(r" \pm ", r"(")
            .replace(r"\right", r"")
            .replace(r" \times 10^{", r"e")
            .replace(r"}", r"")
        )

# Save Table
datadict = {r"$x$": x_table, r"$y$": y_table}
df = pd.DataFrame(datadict)
styler = df.style.format(formatter=None, na_rep=None, precision=None, decimal=".", thousands=None, escape=None, hyperlinks="latex")
styler.use({"hide_index": True})
table = styler.to_latex(
    hrules=True,
    siunitx=True,
    column_format="S[table-format=2.3(1.3)] S[table-format=-2.3(2.3)]",
    environment="longtable",
    caption="Messwerte",
    label="tab:mess",
    position="H",
)
file = open("build/data.tex", "w")
file.write(
    table.replace("\\textbackslash ", "\\")
    .replace("\\$", "$")
    .replace("\\{", "{")
    .replace("\\}", "}")
    .replace("\\textasciicircum ", "^")
)
file.close()