async function obtenerDatos() {
    //const response = await fetch("");
    const json = await response.json();

    console.log(json); //devuelve toda la lista de objetos
    console.log(json.nombre) // devuelve el objeto nombre, y su valor.
    console.log(json.direccion.colonia);

    json.experiencia.forEach(elemento => {
        console.log(elemento.empresa);
    }); //navegar por arreglos

    console.log(json.direccion.pago_clases);
    console.log(json.direccion["pago_clases"]);
    console.log(json["direccion"]["calle"]); //obtengo clave/indice


}



obtenerDatos(); 