const debounce = (func, delay) => { 
    let debounceTimer 
    return function() { 
        const context = this
        const args = arguments 
        clearTimeout(debounceTimer) 
        debounceTimer = setTimeout(() => func.apply(context, args), delay) 
    } 
}

function check_grammar(el) {
	console.log("checking grammar...")
}

function add_grammar_event(el) {

	el.addEventListener("keydown", debounce(() => {
			check_grammar(el)
		}, 1000)
	)
}

document.querySelectorAll('textarea')
	.forEach(el => {
		if(el.offsetHeight < 40) return;

		add_grammar_event(el);
	})

document.querySelectorAll('input[type=text]')
	.forEach(el => {
		if(el.offsetHeight < 40) return;

		add_grammar_event(el);
	})
