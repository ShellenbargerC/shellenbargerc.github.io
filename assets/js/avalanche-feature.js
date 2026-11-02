/* Folder creation dates come from the first Git commit adding their contents. */
(function () {
  'use strict';
  function latestAvalancheFolder(folders) {
    const normalize = value => value.toLowerCase().replace(/[^a-z0-9]/g, '');
    const projects = folders.filter(folder => folder.path.startsWith('independent/') && folder.path.split('/').length === 2);
    const root = projects.find(folder => [folder.title, folder.path.split('/').pop()].some(value => normalize(value || '') === 'avalanchenetworkinfrastructure'))
      || projects.find(folder => normalize(folder.path.split('/').pop()) === 'avalanchenetworksimulation')
      || projects.find(folder => normalize(folder.title || folder.path.split('/').pop()).startsWith('avalanche'));
    if (!root) return null;
    // Only immediate subfolders qualify; individual files and deeper folders cannot win.
    const children = folders.filter(folder => folder.path.startsWith(root.path + '/') && folder.path.split('/').length === 3);
    children.sort((a, b) => (Number(b.createdAt) || 0) - (Number(a.createdAt) || 0)
      || b.path.localeCompare(a.path, undefined, { numeric: true }));
    return children[0] || root;
  }
  const card = document.querySelector('#avalanche-feature');
  if (!card) return;
  fetch('content-index.json').then(response => {
    if (!response.ok) throw Error('Index unavailable');
    return response.json();
  }).then(index => {
    const target = latestAvalancheFolder(index.folders || []);
    if (target) card.href = 'files.html?folder=' + encodeURIComponent(target.path);
  }).catch(() => { /* The card retains its ordinary project-folder link. */ });
})();
