# norwegian-postalcodes-mapper
Mapping from Norwegian postalcodes to city and municipality. The package code is generated automatically with data fetched from https://www.bring.no/postnummerregister-ansi.txt (11.04.2024)

```getPostalCodeInfo('XXXX')``` will return an object with keys 'city' and 'municipality'. If postal code is unknown, both city and municipality will be 'UNKNOWN'

## Usage:
```
getPostalCodeInfo('2007')['city'] // 'KJELLER'
getPostalCodeInfo('2007')['municipality'] // 'LILLESTRØM'

getPostalCodeInfo('asdfhdf')['city'] // 'UNKNOWN'
getPostalCodeInfo('asdfhdf')['municipality'] // 'UNKNOWN'
```

