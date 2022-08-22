const button = document.querySelector('.hamburger-menu')
const leftBar = document.querySelector('.left-bar')
const content = document.querySelector('.section-grid')
const cotiza = document.querySelector('.cotizaciones')


button.addEventListener('click', () => {
	if (leftBar.classList.contains('hidden')) {
		leftBar.classList.remove('hidden');

		/*remove section grid*/
		content.classList.add('hidden');
		content.classList.remove('section-grid')

		/*remove cotizaciones*/
		cotiza.classList.add('hidden');
		cotiza.classList.remove('cotizaciones')

	} else {
		leftBar.classList.add('hidden');

		/*add section grid*/
		content.classList.remove('hidden');
		content.classList.add('section-grid')

		/*add cotizaciones*/
		cotiza.classList.remove('hidden')
		cotiza.classList.add('cotizaciones');
	}
})
