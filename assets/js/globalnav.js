(() => {
  const nav = document.querySelector('.globalnav');
  if (!nav) return;
  const toggle = nav.querySelector('.globalnav-toggle');
  const overlay = nav.querySelector('.globalnav-overlay');
  const desktop = window.matchMedia('(min-width:834px)');
  let returnFocus = null;
  const close = ({ restoreFocus = true } = {}) => {
    if (!nav.classList.contains('is-open')) return;
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('globalnav-open');
    if (restoreFocus && returnFocus) returnFocus.focus();
  };
  const open = () => {
    returnFocus = document.activeElement;
    nav.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.classList.add('globalnav-open');
    overlay.querySelector('a')?.focus();
  };
  toggle.addEventListener('click', () => nav.classList.contains('is-open') ? close() : open());
  overlay.addEventListener('click', event => { if (event.target.closest('a')) close({ restoreFocus:false }); });
  document.addEventListener('keydown', event => {
    if (!nav.classList.contains('is-open')) return;
    if (event.key === 'Escape') { event.preventDefault(); close(); return; }
    if (event.key !== 'Tab') return;
    const focusable = [...overlay.querySelectorAll('a:not([disabled])')];
    const first = focusable[0], last = focusable.at(-1);
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  });
  desktop.addEventListener('change', event => { if (event.matches) close({ restoreFocus:false }); });
})();
