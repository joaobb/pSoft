let api = "https://free.currconv.com/api/v7/convert?q=USD_EUR,USD_BRL&compact=ultra&apiKey=7181591a178d6b0c9a3d";
var fs = require('fs');
let fetx = fetch(api).then(ft => ft.json()).then(j => console.log(j))