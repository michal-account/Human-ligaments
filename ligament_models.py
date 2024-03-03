"""
>> zrodlo danych do generowania wykresow:
Funk J., et al.: Linear and Quasi-Linear Viscoelastic Characterization of Ankle Ligaments
https://www.researchgate.net/publication/12526194_Linear_and_Quasi-Linear_Viscoelastic_Characterization_of_Ankle_Ligaments

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# generowanie zbioru danych wejsciowych
#######################################

# ATiF
A = 5.52 # [N]
B = 22.63

### mozna zmienic
liczba_punktow_dosw = 30
########################

### mozna zmienic
poziom_szumu = 80.
##################


eps_dosw = np.linspace(0., 20., liczba_punktow_dosw) / 100. # [-]
szum = np.random.rand(eps_dosw.shape[0]) * poziom_szumu
F_dosw = A * (np.exp(B * eps_dosw) - 1.)
F_dosw += szum


# rozwiazanie
#############

def model_wiezadla(eps, A, B):
    ### nalezy odkomentowac wybrany model wiezadla
    ##############################################
    
    # model -> funkcja kwadratowa
#    F = A * eps * eps + B

    # model -> funkcja wykladnicza e^x
    F = A * (np.exp(B * eps) - 1.)
    return F

popt, pcov = curve_fit(model_wiezadla, eps_dosw, F_dosw)
print('>> uzyskane parametry A i B to:', popt)

# okreslenie jakosci otrzymanego modelu
#######################################

F_mod = model_wiezadla(eps_dosw, popt[0], popt[1])

roznica = F_mod-F_dosw
jakosc_modelu = np.sum(np.sqrt(roznica * roznica)) / eps_dosw.shape[0]

print('>> jakosc modelu to (mala wartosc oznacza dobry model):', jakosc_modelu)


# wykresy
#########

plt.plot(eps_dosw, F_dosw, 'r', label='doswiadczenie')
plt.plot(eps_dosw, F_dosw, 'ro')

plt.plot(eps_dosw, F_mod, 'g', label='model')
plt.plot(eps_dosw, F_mod, 'go')

plt.xlabel('eps [-]')
plt.ylabel('F [N]')
plt.legend()
plt.show()