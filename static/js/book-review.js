// Progressive enhancement: the complete parallel article works without JavaScript.
document.querySelectorAll('.bilingual-review').forEach((review) => {
  const toolbar = review.querySelector('.reading-toolbar');
  toolbar.hidden = false;
  toolbar.querySelectorAll('[data-reading-mode]').forEach((button) => {
    button.addEventListener('click', () => {
      review.dataset.mode = button.dataset.readingMode;
      toolbar.querySelectorAll('[data-reading-mode]').forEach((option) => {
        option.setAttribute('aria-pressed', String(option === button));
      });
    });
  });
});
