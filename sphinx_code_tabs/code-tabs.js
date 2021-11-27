const sphinx_code_tabs_onclick = function(button) {
	const select = button.parentNode;
	const book = select.parentNode;
	for (const button of select.children) {
    button.classList.toggle('selected', Object.is(button, button));
	}
  for (const page of book.children) {
    if (page.hasAttribute('data-id')) {
      page.classList.toggle('hidden', page.dataset.id != button.dataset.id);
		}
  }
};
