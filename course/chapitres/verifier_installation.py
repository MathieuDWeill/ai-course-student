"""Vérifie le Python du socle sans réseau, compte ni données."""
import importlib.util,sys
missing=[p for p in ['numpy','pandas','sklearn','ipykernel'] if importlib.util.find_spec(p) is None]
print('Python utilisé :',sys.executable)
print('Version Python :',sys.version.split()[0])
if missing:
    print('Modules absents :',', '.join(missing))
    print('Relancer l’installation de requirements.txt avec ce Python, selon le guide.')
    raise SystemExit(1)
print('PRÊT POUR LES EXEMPLES DU SOCLE')
print('Dans Jupyter, sélectionner le noyau Parcours IA avant exécution.')
