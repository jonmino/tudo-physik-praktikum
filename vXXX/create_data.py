#### Skript to create fake data for the example
import numpy as np
import uncertainties.unumpy as unp

fak = 1
rnd = np.random.default_rng(42)
x = 20 * rnd.random(150)
x.sort()
x_err = abs(rnd.normal(0.1, 0.5, len(x)))
a = 5
b = np.pi
c = 10

y = a * x * np.sin(b * x) + c + rnd.normal(1, 5 * fak, len(x))
y_err = abs(rnd.normal(0.1, 5, len(x))) * fak
x = unp.uarray(x, x_err)
y = unp.uarray(y, y_err)

# Never save to any folder other than build, this is just to create some fake measurement data
np.savetxt(
    "content/tables/txt/data.txt",
    np.column_stack(
        [unp.nominal_values(x), unp.std_devs(x), unp.nominal_values(y), unp.std_devs(y)]
    ),
    header="x x_err y y_err",
)