document.getElementById('btn_iniciar_sesion').addEventListener('click', iniciarSesion);
document.getElementById('btn_registro').addEventListener('click', registro);

window.addEventListener('resize', anchoPagina);


let contenedor__login__registro = document.querySelector('.contenedor_login_registro');
let formulario__login = document.querySelector('.formulario_login');
let formulario__registro = document.querySelector('.formulario_registro');

let caja__fondo__login = document.querySelector('.caja_fondo_login');
let caja__fondo__registro = document.querySelector('.caja_fondo_registro');


function anchoPagina(){
    if(window.innerWidth > 850){
        caja__fondo__login.style.display = 'block';
        caja__fondo__registro.style.display = 'block';
    }
    else{
        caja__fondo__registro.style.display = 'block';
        caja__fondo__registro.style.opacity = '1';
        caja__fondo__login.style.display = 'none';
        formulario__login.style.display = 'block';
        formulario__registro.style.display = 'none';
        contenedor__login__registro.style.left = '0px';
    }
}

anchoPagina();

function iniciarSesion(){


    if(window.innerWidth > 850){
        formulario__registro.style.display = 'none';
        contenedor__login__registro.style.left = '10px';
        formulario__login.style.display = 'block';
        caja__fondo__registro.style.opacity = '1';
        caja__fondo__login.style.opacity = '0';
    }
    else{
        formulario__registro.style.display = 'none';
        contenedor__login__registro.style.left = '0px';
        formulario__login.style.display = 'block';
        caja__fondo__registro.style.display = 'block';
        caja__fondo__login.style.display = 'none';
    }
}

function registro(){
    if(window.innerWidth > 850){
        formulario__registro.style.display = 'block';
        contenedor__login__registro.style.left = '410px';
        formulario__login.style.display = 'none';
        caja__fondo__registro.style.opacity = '0';
        caja__fondo__login.style.opacity = '1';
    }
    else{
        formulario__registro.style.display = 'block';
        contenedor__login__registro.style.left = '0px';
        formulario__login.style.display = 'none';
        caja__fondo__registro.style.display = 'none';
        caja__fondo__login.style.display = 'block';
        caja__fondo__login.style.opacity = '1';
    }
    
}