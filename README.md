# NodeSolver
## Overview
Calculate the current and voltage over components. 
Uses a numerical method that allows solving with non-linear components such as diodes.

## Matematik på svenska
Koncept:
    Varje nod bidrar med en ekvation och en variabel:
    + ekvation: kirchoffs lag
    + variabel: potential i nod

    Varje komponent bidrar med en ekvation och en variabel
    + ekvation: förhållande mellan kopplade spänningar och passerande ström
    + variabel: genomgående ström

    Viktigt: En nod jordas, och ger därmed helt enkelt bara funktionen u - 0.
    Jag jordar den första noden som läggs till i nätverket.

Hur:
    För att lösa ett olinjärt ekvationsystem gör vi om ekvationer till funktioner 
    som ska vara 0. Sedan löser vi med JFNKsolver (Jacobian Free Newton-Krylov).

    För att gå från nätverk till ekvationsystem använder vi klassen Network.

GUI:
Skapa draggables. Noder är också draggables. Dessa har alla sockets, som kopplas ihop. 
För att kunna skapa ekvationer måste det finnas tvåpoler med passerande ström mellan 
alla noder. Därför introducerar vi SilentNode, som är hur mycket ström som passerar mellan två noder.