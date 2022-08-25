let cardCotizaciones = document.querySelector(".cotizaciones");

const regex = /(Dolar)\s[B]/gm;
const regex2 = /(Dolar)\s[OCt]/gm;

let i = 0;


fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
.then(data => data.json())
.then(data => data.forEach(element => {
    if (regex.test(element.casa.nombre) || regex2.test(element.casa.nombre)) {

        const usd = {
            nombre: element.casa.nombre === 'Dolar Contado con Liqui' ? 'Dolar CCL' : (element.casa.nombre === 'Dolar turista' ? "Dolar Turista" : element.casa.nombre),
            compra: Number.parseFloat(element.casa.compra.replace(',', '.')),
            venta: Number.parseFloat(element.casa.venta.replace(',', '.')),
            variacion: Number.parseFloat(element.casa.variacion.replace(',', '.'))
        };

        const noCompra = isNaN(usd.compra) ? '' : `Compra <span>$${usd.compra}</span>`;

        const Items = (usd) => {
            return `<div class="dolar-div div-${i++}">
                        <p class="dolar-nombre">${usd.nombre}</p>
                        <p class="dolar-compra">${noCompra}</p>
                        <p class="dolar-venta">Venta <span>$${usd.venta}</span></p>
                        <div class="variacion">
                            <p class="variacion">Variación <span>${usd.variacion}%</span></p>
                        </div>
                    </div>`
        }

        cardCotizaciones.innerHTML += Items(usd);
    }
}))
