import model from "./cambio.js";

var cotacao = {};

var getPrice = async function() {
    const api = "https://free.currconv.com/api/v7/convert?q=USD_EUR,USD_BRL&compact=ultra&apiKey=7181591a178d6b0c9a3d";
    const fetcher = await fetch(api);
    cotacao = await fetcher.json();
}()

function real() {
    model.real = $real.value;
    model.cambReal(cotacao);
    $dollar.value = model.dollar.toFixed(2);
    $euro.value = model.euro.toFixed(2);
}

function dollar() {
    model.dollar = $dollar.value;
    model.cambDollar(cotacao);
    $real.value = model.real.toFixed(2);
    $euro.value = model.euro.toFixed(2);
};

function euro() {
    model.euro = $euro.value;
    model.cambEuro(cotacao);
    $real.value = model.real.toFixed(2);
    $dollar.value = model.dollar.toFixed(2);
}

const $real = document.querySelector("#real");
const $dollar = document.querySelector("#dollar");
const $euro = document.querySelector("#euro");

$real.onkeyup = real;
$euro.onkeyup = euro;
$dollar.onkeyup = dollar;

