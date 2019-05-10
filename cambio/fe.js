import model from "./cambio.js";

var cotacao;

async function getCotacao() {
    const api = "https://free.currconv.com/api/v7/convert?q=USD_EUR,USD_BRL&compact=ultra&apiKey=7181591a178d6b0c9a3d";
    const fetcher = await fetch(api);
    cotacao = await fetcher.json()
}

getCotacao()

const $real = document.querySelector("#real");
const $dollar = document.querySelector("#dollar");
const $euro = document.querySelector("#euro");

function real() {
    let res = model.cambReal($real.value, cotacao);
    $dollar.value = res["dollar"].toFixed(2);
    $euro.value = res["euro"].toFixed(2);
}

function dollar() {
    let res = model.cambDollar($dollar.value, cotacao);
    $real.value = res["real"].toFixed(2);
    $euro.value = res["euro"].toFixed(2);
}

function euro() {
    let res = model.cambEuro($euro.value, cotacao);
    $real.value = res["real"].toFixed(2);
    $dollar.value = res["dollar"].toFixed(2);
}

$real.onkeyup = real;
$dollar.onkeyup = dollar;
$euro.onkeyup = euro;

