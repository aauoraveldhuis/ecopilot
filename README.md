# Ecopilot
Kandidatarbete EENX16-23-27b

ACADOS BRANCH----------------------------------
Denna branch är dedikerad till implementationen av Acados. Filen som ändrats är controller.py där begränsnings- och kostnadsfuntionerna gjorts om för att acados ska kunna tolka dem. Dessa ändringar gjordes i slutet av projektet och då det inte fanns så mycket tid va det vissa problem som inte hann lösas. Bland annat uppstod problem med att importera metoder från Acados_template så programmet gick inte att testköras för att se vad som blev fel och vad som fungerade.

De metoder som ändrats är: 
setStateEqconstraints()
setInEqConstraints()
setTrafficConstraints()
setCost()
setController()
