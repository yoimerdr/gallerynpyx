(function () {
  let cachedVersions = null;

  async function fetchVersions() {
    if (cachedVersions) {
      return cachedVersions;
    }

    const config = window.GALLERYNPYX_DOCS;
    if (!config || !config.versions_path) {
      return null;
    }

    try {
      const response = await fetch(config.versions_path + "/versions.json");
      if (!response.ok) {
        throw new Error("Failed to fetch versions");
      }
      cachedVersions = await response.json();
      return cachedVersions;
    } catch (error) {
      console.error("Error loading versions:", error);
      return null;
    }
  }

  function getDocsConfig() {
    const config = window.GALLERYNPYX_DOCS;

    if (!config || !Array.isArray(config.versions) || !config.versions.length) {
      return null;
    }

    return config;
  }

  function escapeForRegex(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function replaceVersion(pathname, currentVersion, nextVersion) {
    const pattern = new RegExp("(^|/)" + escapeForRegex(currentVersion) + "(?=/)");
    return pathname.replace(pattern, "$1" + nextVersion);
  }

  function findCurrentVersion(config) {
    const pathname = window.location.pathname;

    for (const version of config.versions) {
      if (pathname.indexOf("/" + version.slug + "/") !== -1) {
        return version.slug;
      }
    }

    return config.current_version || null;
  }

  function onVersionChange(event) {
    const select = event.currentTarget;
    const currentVersion = select.dataset.docsCurrentVersion;
    const nextVersion = select.value;

    if (!currentVersion || !nextVersion || currentVersion === nextVersion) {
      return;
    }

    const url = new URL(window.location.href);
    const nextPathname = replaceVersion(url.pathname, currentVersion, nextVersion);

    if (nextPathname === url.pathname) {
      return;
    }

    url.pathname = nextPathname;
    window.location.href = url.toString();
  }

  function createSelector(config, currentVersion) {
    const select = document.createElement("select");
    select.setAttribute("aria-label", "Version");
    select.dataset.docsCurrentVersion = currentVersion;

    for (const version of config.versions) {
      const option = document.createElement("option");
      option.value = version.slug;
      option.textContent = version.label;
      option.selected = version.slug === currentVersion;
      select.appendChild(option);
    }

    select.addEventListener("change", onVersionChange);
    return select;
  }

  async function initVersionSelector() {
    const config = window.GALLERYNPYX_DOCS;
    const versions = await fetchVersions();

    if (!config || !versions || !versions.length) {
      return;
    }

    const search = document.querySelector(".wy-side-nav-search");
    const home = search && search.querySelector("a.icon-home, a");

    if (!search || !home || search.querySelector(".local-switch-menus")) {
      return;
    }

    const currentVersion = findCurrentVersion({ versions, current_version: config.current_version });

    if (!currentVersion) {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "switch-menus local-switch-menus";

    const versionSwitch = document.createElement("div");
    versionSwitch.className = "version-switch";
    versionSwitch.appendChild(createSelector({ versions }, currentVersion));
    wrapper.appendChild(versionSwitch);

    home.insertAdjacentElement("afterend", wrapper);
  }

  function init() {
    initVersionSelector().catch(err => console.error("Version selector error:", err));
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  }
  else {
    init();
  }
})();
