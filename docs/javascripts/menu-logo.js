document.addEventListener("DOMContentLoaded", function () {
  const basePath = "/oss_toolchainmap";

  var navHeader = document.querySelector(
    ".md-sidebar--primary .md-sidebar__inner .md-header-nav"
  );
  if (!navHeader) return;

  var logoWrapper = navHeader.querySelector(".md-logo");
  var logoImg = logoWrapper ? logoWrapper.querySelector("img") : null;
  var titleLink = navHeader.querySelector(".md-header-nav__title a");

  if (!logoWrapper || !logoImg || !titleLink) return;

  var menuLogoUrl =
    window.location.origin +
    basePath +
    "/assets/logotype/site/logo_menu.png";

  logoImg.src = menuLogoUrl;
  logoImg.removeAttribute("srcset");

  var wrapper = document.createElement("div");
  wrapper.className = "menu-logo-title";

  wrapper.appendChild(titleLink);
  wrapper.appendChild(logoWrapper);

  navHeader.innerHTML = "";
  navHeader.appendChild(wrapper);
});
