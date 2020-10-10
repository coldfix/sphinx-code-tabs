const onclick = function(event) {
	const select = this.parentNode;
	const book = select.parentNode;
	for (const button of select.children) {
    button.classList.toggle('selected', Object.is(button, this));
	}
  for (const page of book.children) {
    if (page.hasAttribute('data-id')) {
      page.classList.toggle('hidden', page.dataset.id != this.dataset.id);
		}
  }
};

window.addEventListener('load', function() {
  for (const book of document.querySelectorAll('div.code-tabs')) {
    let i = 0;
    let navbar = document.createElement('ul');
    for (const page of book.children) {
      const button = document.createElement('li');
      page.setAttribute('data-id', i);
			button.setAttribute('data-id', i);
      button.onclick = onclick;
      button.innerText = page.getAttribute('data-title');
      button.classList.toggle('selected', i == 0);
      page.classList.toggle('hidden', i != 0);
      navbar.appendChild(button);
      ++i;
    }
    book.prepend(navbar);
  }
}, false);
