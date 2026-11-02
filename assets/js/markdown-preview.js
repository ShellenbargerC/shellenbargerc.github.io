/* Markdown reading view. Marked 17.0.5 supplies tokens; DOM nodes are built
   explicitly so raw HTML, event handlers, and executable URLs cannot run. */
(function () {
  'use strict';

  function render(file, options = {}) {
    if (!window.marked) throw new Error('Markdown parser unavailable');
    const article = document.createElement('article');
    article.className = 'markdown-body';
    article.id = 'markdown-preview';
    article.setAttribute('aria-label', 'Formatted Markdown');
    const headings = new Map();
    const counts = new Map();
    const base = new URL(options.encodedPath(file.url), location.href);

    function node(tag, text) {
      const element = document.createElement(tag);
      if (text !== undefined) element.textContent = text;
      return element;
    }
    function decode(text) {
      const value = String(text || '');
      if (!value.includes('&')) return value;
      const textarea = document.createElement('textarea');
      textarea.innerHTML = value.replace(/</g, '&lt;').replace(/>/g, '&gt;');
      return textarea.value;
    }
    function safeUrl(value, image = false) {
      const raw = decode(value).trim();
      if (image && /^data:image\/(?:png|jpeg|gif|webp|avif);base64,[a-z\d+/=\s]+$/i.test(raw)) return raw;
      try {
        const url = new URL(raw, base);
        const allowed = image ? ['http:', 'https:'] : ['http:', 'https:', 'mailto:'];
        return allowed.includes(url.protocol) ? url.href : null;
      } catch (_) { return null; }
    }
    function slug(text) {
      return text.toLowerCase().replace(/[^\p{L}\p{N}_\s-]/gu, '').trim().replace(/\s/g, '-');
    }
    function text(parent, value) {
      parent.append(document.createTextNode(decode(value)));
    }
    function addLink(token, parent) {
      const raw = decode(token.href || '').trim();
      const href = safeUrl(raw);
      if (!href) { inline(token.tokens || [], parent); return; }
      const link = node('a');
      link.href = href;
      if (token.title) link.title = decode(token.title);
      inline(token.tokens || [], link);
      if (raw.startsWith('#')) {
        // Scroll within this preview without replacing File Library's file hash.
        link.addEventListener('click', event => {
          let fragment;
          try { fragment = decodeURIComponent(raw.slice(1)); } catch (_) { fragment = raw.slice(1); }
          const target = headings.get(fragment) || headings.get(slug(fragment));
          if (target) { event.preventDefault(); target.scrollIntoView({ block: 'start' }); }
        });
      } else {
        const resolved = new URL(href);
        const target = (options.files || []).find(candidate => {
          const candidateUrl = new URL(options.encodedPath(candidate.url), location.href);
          return resolved.origin === candidateUrl.origin && resolved.pathname === candidateUrl.pathname;
        });
        if (target) {
          const view = new URL('files.html', location.href);
          const folder = target.path.split('/').slice(0, 2).join('/');
          if (folder.includes('/')) view.searchParams.set('folder', folder);
          view.hash = encodeURIComponent(target.path);
          link.href = view.href;
        } else if (resolved.protocol !== 'mailto:' && resolved.origin !== location.origin) {
          link.target = '_blank';
          link.rel = 'noopener noreferrer';
        }
      }
      parent.append(link);
    }
    function checkbox(token, parent) {
      const input = node('input');
      input.type = 'checkbox';
      input.disabled = true;
      input.checked = Boolean(token.checked);
      input.setAttribute('aria-label', token.checked ? 'Completed task' : 'Incomplete task');
      parent.append(input, document.createTextNode(' '));
    }
    function inline(tokens, parent) {
      for (const token of tokens) {
        switch (token.type) {
          case 'strong': case 'em': case 'del': {
            const element = node(token.type); inline(token.tokens || [], element); parent.append(element); break;
          }
          case 'codespan': parent.append(node('code', token.text)); break;
          case 'br': parent.append(node('br')); break;
          case 'checkbox': checkbox(token, parent); break;
          case 'link': addLink(token, parent); break;
          case 'image': {
            const src = safeUrl(token.href, true);
            if (!src) { text(parent, token.text); break; }
            const image = node('img'); image.src = src; image.alt = decode(token.text);
            image.loading = 'lazy'; image.decoding = 'async';
            if (token.title) image.title = decode(token.title);
            parent.append(image); break;
          }
          case 'html': text(parent, token.raw); break;
          default:
            if (token.tokens) inline(token.tokens, parent);
            else text(parent, token.text === undefined ? token.raw : token.text);
        }
      }
    }
    function table(token, parent) {
      const wrapper = node('div'); wrapper.className = 'markdown-table';
      wrapper.tabIndex = 0; wrapper.setAttribute('role', 'region'); wrapper.setAttribute('aria-label', 'Scrollable table');
      const element = node('table'); const head = node('thead'); const row = node('tr');
      function cell(data, tag, index) {
        const result = node(tag); inline(data.tokens || [], result);
        if (tag === 'th') result.scope = 'col';
        const align = token.align && token.align[index];
        if (['left', 'center', 'right'].includes(align)) result.style.textAlign = align;
        return result;
      }
      token.header.forEach((data, index) => row.append(cell(data, 'th', index)));
      head.append(row); element.append(head); const body = node('tbody');
      for (const data of token.rows) {
        const row = node('tr'); data.forEach((value, index) => row.append(cell(value, 'td', index))); body.append(row);
      }
      element.append(body); wrapper.append(element); parent.append(wrapper);
    }
    function blocks(tokens, parent) {
      for (const token of tokens) {
        switch (token.type) {
          case 'space': case 'def': break;
          case 'heading': {
            const heading = node('h' + Math.max(1, Math.min(6, token.depth)));
            inline(token.tokens || [], heading);
            const stem = slug(heading.textContent); const count = counts.get(stem) || 0; counts.set(stem, count + 1);
            const key = stem + (count ? '-' + count : ''); heading.id = 'markdown-heading-' + key;
            headings.set(key, heading); parent.append(heading); break;
          }
          case 'paragraph': { const p = node('p'); inline(token.tokens || [], p); parent.append(p); break; }
          case 'text': if (token.tokens) inline(token.tokens, parent); else text(parent, token.text); break;
          case 'code': {
            const pre = node('pre'); const code = node('code', token.text);
            const language = (token.lang || '').split(/\s/)[0];
            if (/^[a-z\d_+-]+$/i.test(language)) code.className = 'language-' + language;
            pre.append(code); parent.append(pre); break;
          }
          case 'blockquote': { const quote = node('blockquote'); blocks(token.tokens || [], quote); parent.append(quote); break; }
          case 'list': {
            const list = node(token.ordered ? 'ol' : 'ul');
            if (token.ordered && Number.isSafeInteger(token.start)) list.start = token.start;
            for (const item of token.items) {
              const li = node('li'); if (item.task) li.className = 'markdown-task';
              blocks(item.tokens || [], li); list.append(li);
            }
            parent.append(list); break;
          }
          case 'checkbox': checkbox(token, parent); break;
          case 'table': table(token, parent); break;
          case 'hr': parent.append(node('hr')); break;
          case 'html': { const p = node('p'); text(p, token.raw); parent.append(p); break; }
          default: if (token.tokens) blocks(token.tokens, parent); else text(parent, token.text || token.raw);
        }
      }
    }
    const source = String(file.preview || '').replace(/^[\u200B-\u200F\uFEFF]+/, '');
    blocks(window.marked.lexer(source, { gfm: true, breaks: false }), article);
    if (!article.childNodes.length) article.append(node('p', '(Empty file)'));
    return article;
  }
  window.PortfolioMarkdown = { render };
})();
