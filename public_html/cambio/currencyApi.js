async function getCotacao() {
    const api = "https://free.currconv.com/api/v7/convert?q=USD_EUR,USD_BRL&compact=ultra&apiKey=7181591a178d6b0c9a3d";
    const fetcher = await fetch(api);
    return await fetcher.json()
}

export default getCotacao;