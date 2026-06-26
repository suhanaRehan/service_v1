
const megaToggle = document.querySelector('.mega-toggle');
const megaMenu = document.getElementById('megaMenu');
const accordionButtons = document.querySelectorAll('.mobile-nav .accordion-button');

if (megaToggle && megaMenu) {
  megaToggle.addEventListener('mouseover', () => megaMenu.classList.add('open'));
  megaToggle.addEventListener('focus', () => megaMenu.classList.add('open'));
  document.addEventListener('click', (e) => {
    if (!megaMenu.contains(e.target) && e.target !== megaToggle) {
      megaMenu.classList.remove('open');
    }
  });
}

accordionButtons.forEach((button) => {
  const panel = button.nextElementSibling;
  if (!panel) return;
  button.addEventListener('click', () => {
    const isOpen = button.classList.toggle('active');
    if (isOpen) {
      panel.style.maxHeight = panel.scrollHeight + 'px';
    } else {
      panel.style.maxHeight = null;
    }
  });
});
