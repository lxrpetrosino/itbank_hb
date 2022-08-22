const form = document.querySelector('.form-login')
const inputs = document.querySelectorAll('.form_input')

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo.
	contraseña: /^.{4,12}$/ // 4 a 12 digitos.
}

const campos = {
	usuario: false,
	contraseña: false
}

const validarFormulario = (e) => {
	if (e.target.name === 'usuario') {
		validarCampo(expresiones.usuario, e.target, 'usuario');
	}
	if (e.target.name === 'contraseña') {
		validarCampo(expresiones.contraseña, e.target, 'contraseña');
	}
}

const validarCampo = (expresiones, input, campo) => {
	if (expresiones.test(input.value)) {
		document.querySelector(`.grupo__${campo}`).classList.remove('incorrecto');
		document.querySelector(`#${campo}`).classList.remove('error-border');
		document.querySelector(`.grupo__${campo}`).classList.add('correcto');
		document.querySelector(`#${campo}`).classList.add('correcto-border');
		document.querySelector(`.grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`.grupo__${campo} i`).classList.remove('fa-times-circle');
		campos[campo] = true;
	} else {
		document.querySelector(`.grupo__${campo}`).classList.add('incorrecto');
		document.querySelector(`#${campo}`).classList.add('error-border');
		document.querySelector(`.grupo__${campo}`).classList.remove('correcto');
		document.querySelector(`#${campo}`).classList.remove('correcto-border');
		document.querySelector(`.grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`.grupo__${campo} i`).classList.add('fa-times-circle');
		campos[campo] = false;

	}

}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
})

form.addEventListener('submit', (e) => {
	e.preventDefault();

	if (campos.usuario && campos.contraseña) {
		form.reset();
	}

	document.querySelectorAll('.correcto').forEach((icono) => {
	icono.classList.remove('correcto');
	});	

	document.querySelectorAll('.correcto-border').forEach((icono) => {
	icono.classList.remove('correcto-border');
	});	
})

