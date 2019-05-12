const model = {
    "dollar" : null,
    "real" : null,
    "euro" : null,

    cambReal: function cambReal(price) {
        this.dollar = this.real / price["USD_BRL"];
        this.euro = this.dollar * price["USD_EUR"];
    },

    cambDollar : async function cambDollar(price) {
        this.real = this.dollar * price["USD_BRL"];
        this.euro = this.dollar * price["USD_EUR"];
    },

    cambEuro: function cambEuro(price) {
        this.dollar = this.euro / price["USD_EUR"] 
        this.real = this.dollar * price["USD_BRL"];
    }
};

export default model;