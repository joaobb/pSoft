const model = {
    cambReal: function cambReal(value, price) {
        return {
            "dollar" : value / price["USD_BRL"],
            "euro" : (value / price["USD_BRL"]) * price["USD_EUR"]
        };
    },

    cambDollar : function cambDollar(value, price) {
        return {
            "real" : value * price["USD_BRL"] | "",
            "euro" : value * price["USD_EUR"]
        };
    },

    cambEuro: function cambEuro(value, price) {
        return {
            "real" : (value / price["USD_EUR"]) * price["USD_BRL"],
            "dollar" : value / price["USD_EUR"] 
        };
    },
};

export default model;