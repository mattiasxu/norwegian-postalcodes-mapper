const getPostalCodeInfo = require('./index.js');


console.log(getPostalCodeInfo('2007')['city']); // KJELLER;
console.log(getPostalCodeInfo('2007')['municipality']); // LILLESTRØM;
console.log(getPostalCodeInfo('asdb')); //

test('Known city is correct', () => {
  expect(getPostalCodeInfo('2007')['city']).toBe('KJELLER');
})

test('Known municipality is correct', () => {
    expect(getPostalCodeInfo('2007')['municipality']).toBe('LILLESTRØM');
})

test('Unknown postal code returns UNKNOWN city', () => {
    expect(getPostalCodeInfo('asdb')['city']).toBe('UNKNOWN');
})

test('Unknown postal code returns UNKNOWN municipality', () => {
    expect(getPostalCodeInfo('asdb')['municipality']).toBe('UNKNOWN');
})
