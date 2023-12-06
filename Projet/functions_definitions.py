import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def csv_plot(file_path, file_name):

    data = pd.read_csv(file_path).drop(pd.read_csv(file_path).columns[0], axis = 1)

    deplacements = data['Axial_Disp. [mm]']
    rotations = data['Rotation']
    moments = data['Base moment [kN.m]']

    plt.plot(rotations, moments, linestyle='-', linewidth=1, color='green', label='Moments vs Rotations')

    # Ajouter des labels et un titre
    plt.xlabel('Déplacements [mm]')
    plt.ylabel('Moments [kN.m]')
    plt.title(f'Relation entre Moments et Déplacements (Diagramme de lignes), file: {file_name}')
    plt.legend()

    # Afficher le graphique
    plt.show()

    return None



def csv_plot_export(file_path, file_name):

    data = pd.read_csv(file_path).drop(pd.read_csv(file_path).columns[0], axis = 1)

    deplacements = data['Axial_Disp. [mm]']
    rotations = data['Rotation']
    moments = data['Base moment [kN.m]']

    plt.plot(rotations, moments, linestyle='-', linewidth=1, color='green', label='Moments vs Rotations')

    # Ajouter des labels et un titre
    plt.xlabel('Déplacements [mm]')
    plt.ylabel('Moments [kN.m]')
    plt.title(f'Relation entre Moments et Déplacements (Diagramme de lignes), file: {file_name}')
    plt.legend()

    # Afficher le graphique
    plt.show()

    return None


def printgraph(x,y,xname,yname,unit1, unit2):
    plt.figure(figsize=(7, 5))
    plt.plot(x,y,'-o', mfc="w")
    
    # Show a straight line
    # plt.axline((x[0], y[0]), (x[1], y[1]))

    plt.title(f'{yname} as a function of {xname}')
    plt.xlabel(f"{xname} [{unit1}]")
    plt.ylabel(f"{yname} [{unit2}]")

    plt.text(max(x)*0.5, max(y)*0.9, f"$x_{{max}}={max(x):.6e}$\n$y_{{max}} = {max(y):.6e}$")
    
    plt.show()

    return None