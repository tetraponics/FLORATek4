// FLORATek 4 Custom Version Selector
document.addEventListener(
  "readthedocs-addons-data-ready",
  function (event) {
    const config = event.detail.data();

    // Only add selector if we have multiple versions
    if (config.versions.active.length > 1) {
      
      // Create the version selector HTML with custom label
      const versionSelector = `
        <div class="floratek-version-selector" style="margin: 15px 0; padding: 10px; background-color: #f8f9fa; border-radius: 4px;">
          <label style="display: block; font-size: 0.85em; color: #666; margin-bottom: 5px; font-weight: bold;">
            FLORATek 4 SW Version:
          </label>
          <select onchange="window.location.href=this.value" style="width: 100%; padding: 5px; border: 1px solid #ccc; border-radius: 3px; font-size: 0.9em;">
            <option value="${config.versions.current.urls.documentation}">
              ${config.versions.current.slug}
            </option>
            ${config.versions.active
              .filter(v => v.slug !== config.versions.current.slug)
              .map(version => `
                <option value="${version.urls.documentation}">
                  ${version.slug}
                </option>
              `).join('')}
          </select>
        </div>
      `;

      // Try to insert into sidebar near search box
      const searchBox = document.querySelector('.wy-side-nav-search');
      if (searchBox) {
        searchBox.insertAdjacentHTML('afterend', versionSelector);
      } else {
        // Fallback: insert at top of sidebar
        const sidebar = document.querySelector('.wy-side-scroll');
        if (sidebar) {
          sidebar.insertAdjacentHTML('afterbegin', versionSelector);
        }
      }
    }
  }
);
