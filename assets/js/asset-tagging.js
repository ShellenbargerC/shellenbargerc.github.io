(() => {
  'use strict';
  const rows = [...document.querySelectorAll('tbody tr')];
  const search = document.querySelector('#asset-search');
  search.addEventListener('input', () => {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    rows.forEach(row => {
      const text = [...row.cells].slice(0, 5).map(cell => cell.textContent).join(' ').toLocaleLowerCase();
      row.hidden = !text.includes(query);
      if (!row.hidden) visible++;
    });
    document.querySelector('#count').textContent = `${visible} of ${rows.length} assets`;
    document.querySelector('#no-results').hidden = visible !== 0;
  });
  document.addEventListener('click', async event => {
    const preview = event.target.closest('button[data-preview]');
    if (preview) {
      document.querySelector('#preview-frame').src = preview.dataset.preview;
      document.querySelector('#preview-frame').title = `${preview.dataset.asset} asset webpage`;
      document.querySelector('#preview-title').textContent = `Asset preview · ${preview.dataset.asset}`;
      document.querySelector('#preview-open').href = preview.dataset.preview;
      document.querySelector('#preview-copy').dataset.copy = preview.dataset.preview;
      rows.forEach(row => row.classList.toggle('selected', row.contains(preview)));
      const title = document.querySelector('#preview-title');
      title.tabIndex = -1;
      title.focus({preventScroll: true});
      document.querySelector('#asset-preview').scrollIntoView({block: 'start'});
    }
    const copy = event.target.closest('button[data-copy]');
    if (!copy) return;
    const url = new URL(copy.dataset.copy, document.baseURI).href;
    const status = document.querySelector('#status');
    const fallback = document.querySelector('#copy-fallback');
    fallback.hidden = true;
    try {
      await navigator.clipboard.writeText(url);
      status.textContent = `Copied asset link: ${url}`;
    } catch {
      const input = document.querySelector('#asset-url');
      input.value = url;
      fallback.hidden = false;
      input.focus();
      input.select();
      status.textContent = 'Select and copy the link below.';
    }
  });
})();
