# velgix

Couteau suisse Python pour la Belgique.

## Installation

pip install velgix

## Utilisation

### Jours feries

from velgix import holidays
feries = holidays.feries(2026)
holidays.est_ferie(date(2026, 7, 21))  # True

### TVA et NISS

from velgix import numbers
numbers.tva_valide("BE0411905847")  # True

### Codes postaux

from velgix import postal
postal.ville("1000")  # "Bruxelles"

## Tests

pytest

## Licence

MIT
