# Ecopilot
Kandidatarbete EENX16-23-27b

ACADOS BRANCH-----------------------------------------------------------------------------------

Denna branch är dedikerad till implementationen av Acados. Filen som ändrats är controller.py där begränsnings- och kostnadsfuntionerna gjorts om för att acados ska kunna tolka dem. Denna implementation är inte komplett och exkeverades inte på min dator. Det uppstod problem med att importera metoder från Acados_template på slutet så det blev svårt att testa programmet.

De metoder som ändrats i controller.py är: 

setStateEqconstraints()

setInEqConstraints()

setTrafficConstraints()

setCost()

setController()

----------------------------------------------------------------------------------------------
