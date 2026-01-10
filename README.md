# NodeSolver
## Overview
Calculate the current and voltage over components. 
Uses a numerical method that allows solving with non-linear components such as diodes.

## Matematik på svenska
Varje nod bidrar med en ekvation och en variabel:

    + ekvation: kirchoffs lag
    + variabel: potential i nod

Varje dipol bidrar med en ekvation och en variabel

    + ekvation: förhållande mellan kopplade potentialer och passerande ström
    + variabel: genomgående ström

Viktigt:

    En nod jordas, och ger därmed helt enkelt bara residualen u - 0.
    Jag jordar den första noden som läggs till i nätverket.
    Denna nod applicerar vi ej kirchoffs lag på!