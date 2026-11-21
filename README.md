# 👁️ MotionWatch

**Jednoduchý strážca kamery: sleduje obraz a zapíše čas, keď sa v ňom pohne niečo väčšie.**

![Rok](https://img.shields.io/badge/rok-2017-blue) ![Python](https://img.shields.io/badge/Python-2.7-yellow) ![OpenCV](https://img.shields.io/badge/OpenCV-2.4-green) ![Stav](https://img.shields.io/badge/stav-archív-lightgrey)

> **Rok realizácie:** 2017 · **Tagy:** `opencv` `python` `motion-detection` `background-subtraction` `webcam` `surveillance` `computer-vision`

## O projekte

MotionWatch je krátky skript (okolo 40 riadkov), ktorý číta obraz z webkamery a porovnáva ho s „naučeným“ pozadím. Keď sa v zábere objaví alebo zmizne väčší pohybujúci sa objekt, vypíše do konzoly časovú značku. Dobrý základ pre domáci alarm alebo záznam len „zaujímavých“ momentov.

## Ako to funguje

1. Snímka z kamery sa prevedie na sivú.
2. **Odčítanie pozadia (MOG)** s pomalou rýchlosťou učenia `0.005` vytvorí masku pohybu.
3. V maske sa nájdu kontúry; berú sa len objekty väčšie ako **80 × 120 px**, aby sa ignoroval šum.
4. Okolo objektu sa nakreslí rámik a stred (centroid).
5. Keď sa zmení počet objektov, vypíše sa `Pohyb na zázname bol v čase <dátum a čas> objekt N`.

## Spustenie

Vyžaduje **Python 2.7 a OpenCV 2.4** (`cv2.BackgroundSubtractorMOG`).

```bash
python "detekcia zmeny.py"
```

Kláves `q` program ukončí.

## Poznámky

- Čas sa zapisuje v UTC (`gmtime`).
- V OpenCV 3/4 treba MOG nahradiť napr. `cv2.createBackgroundSubtractorMOG2()`.
- Súvisiace projekty: [PeopleSpotter](https://github.com/VRDragon/detekcia-ludi), [ColorTracker](https://github.com/VRDragon/sledovanie-farby).

## Autor

**Vratislav Režo** ([@VRDragon](https://github.com/VRDragon))
