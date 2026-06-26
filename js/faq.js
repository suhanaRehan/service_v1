document.addEventListener('DOMContentLoaded', () => {
  const accordions = document.querySelectorAll('.accordion-item');

  accordions.forEach((item) => {
    const button = item.querySelector('.accordion-button');
    const panel = item.querySelector('.accordion-panel');

    if (!button || !panel) return;

    button.addEventListener('click', () => {
      const isOpen = item.classList.toggle('open');
      if (isOpen) {
        panel.style.maxHeight = panel.scrollHeight + 'px';
      } else {
        panel.style.maxHeight = null;
      }
    });
  });

  window.addEventListener('resize', () => {
    accordions.forEach((item) => {
      const panel = item.querySelector('.accordion-panel');
      if (item.classList.contains('open') && panel) {
        panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  });
});
