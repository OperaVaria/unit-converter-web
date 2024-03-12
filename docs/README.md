# Mértékegységváltó a történeti tudományok számára – webalkalmazás

E webalkalmazás egy könnyen használható átváltó történelmi mértékegységek számára.
Célja, hogy segítse mind a kutatókat, mind az eligazodni vágyókat a múlt
mértékegységeinek konvertálásában. Szemben az interneten elérhető más átváltókkal,
jelen projektben minden információ megbízható szakirodalmi forrásból származik,
eredetük a mértékegység-adatbázisban részletesen jelölve van és ellenőrizhető.
A felületen megjelenő rövid információk ellátják a felhasználót a kiválasztott
mértékegységek és mértékegységrendszerek alapvető kontextusával. Az alkalmazás
elérhető magyar és angol felülettel egyaránt.

## Adatbázis

Az adatbázis pillanatnyilag főképp a történelmi Ausztriához és Magyarországhoz
kapcsolódó mértékegységrendszereket tartalmaz, csakúgy, mint az ókori görög és
római mértékeket; ugyanakkor bármely mértékegységrendszer bevezethető,
ezek hozzáadása folyamatos. Minden modern metrikus és lényegi angolszász mértékegység
szerepel viszonyítás végett. Az adatbázis tartalma külön hozzáférhető a "database"
mappában sqlite, csv és json formátumban egyaránt. Az ógörög szavak átírásakor
az úgynevezett "tudományos" átírást alkalmaztuk.

## Technikai háttér

Projektünk a [Flask](https://github.com/pallets/flask/) web frameworkre épül,
Python backenddel és hagyományos, reszponzív HTML-CSS-JS frontenddel.
Az extra funkcionalitás a következő Flask kiegészítőkkel valósult meg:

- Lokalizáció a [Flask-Babel](https://github.com/python-babel/flask-babel) segítségével.
- A nyelvválasztást az alkalmazás [Flask-Sessions](https://github.com/pallets-eco/flask-session) szerver oldali munkamenetekkel rögzíti.
- Minifikáció a [Flask-Minifyjal](https://github.com/mrf345/flask_minify).
- HTTP biztonsági fejlécek a [Flask-Talismannal](https://github.com/GoogleCloudPlatform/flask-talisman).

A frontend elkészítéséhez külső weboldal-sablon nem került felhasználásra. Az
egyedi legördülő menük a [Choices.js](https://github.com/Choices-js/Choices)
plugin integrálásával készültek. Az alkalmazás a HTML oldalak generálásában
nagyban támaszkodik a Jinja sablon motorra, a lehető legoptimálisabb weboldal-kódolás elérése érdekében.
A mértékegység-adatbázis az SQLite adatbázismotor segítségével épült.

E projekt a korábbi, [Python asztali alkalmazásunk](https://github.com/OperaVaria/unit-converter)
online implementációja és továbbfejlesztése.

# Unit Converter for Historical Studies - web application

This web application is an easy-to-use converter for historical measurement units.
Its aim is to assist both researchers and regular users with the conversion of units
from the past. Contrary to other converters available on the internet,
in the present project all information is derived from reliable literature,
their source is duly noted and verifiable in the unit database. Short information
notices on the interface provide the user with the basic context of the selected
unit or unit system. The application is available with both English
and Hungarian interfaces.

## Database

Currently the database features mostly unit systems connected to the historical
Austria and Hungary, as well as the Ancient Greek and Roman measurements;
however any unit system can be implemented, their addition is continuous.
All modern metric and relevant Anglo-American units are present for reference.
The contents of the database are accessible separately in the "database" folder
in either sqlite, csv, or json formats. The Ancient Greek words were transliterated
following the ALA-LC romanization standard.

## Technical background

Our project is built on the [Flask](https://github.com/pallets/flask/) web framework,
with a Python backend and a conventional, responsive HTML-CSS-JS frontend.
Extra functionality has been added with the following Flask extensions:

- Localization with the aid of [Flask-Babel](https://github.com/python-babel/flask-babel).
- The language selection is stored in server-side [Flask-Sessions](https://github.com/pallets-eco/flask-session).
- Minifications with [Flask-Minify](https://github.com/mrf345/flask_minify).
- HTTP security headers with [Flask-Talisman](https://github.com/GoogleCloudPlatform/flask-talisman).

No external website templates were utilized for the creation of the front-end.
The custom drop-down menus were made with the integration of the
[Choices.js](https://github.com/Choices-js/Choices) plugin.
The application relies greatly on the Jinja template engine in
generating the HTML pages to achieve the most optimal website coding. The unit
database was built with the aid of the SQLite database engine.

This project is the improved version and online implementation of our previous,
[Python desktop application](https://github.com/OperaVaria/unit-converter).

## Egyéb információk - Other Information

Tesztelve/Tested on: Firefox 123.0, Google Chrome 122.0 (Windows 11 and Android ver.)

Favicon: "Scale Unbalanced" by Templarian from [SVG Repo](https://www.svgrepo.com/svg/370577/scale-unbalanced), PD Licence.

**[Elérhetőség/Contact](mailto:lcs_it@proton.me)**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
