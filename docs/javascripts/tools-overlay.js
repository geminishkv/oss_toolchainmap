document.addEventListener("DOMContentLoaded", function () {
  const trigger = document.querySelector("[data-tools-overlay-trigger]");
  const overlay = document.querySelector("[data-tools-overlay]");

  if (!trigger || !overlay) {
    console.warn("[tools-overlay] trigger or overlay not found");
    return; 
  }

  var backdrop = overlay.querySelector(".tools-overlay__backdrop");
  var closeBtn = overlay.querySelector(".tools-overlay__close");

  function openOverlay(evt) {
    evt.preventDefault();
    overlay.classList.add("is-visible");
  }

  function closeOverlay(evt) {
    if (evt) evt.preventDefault();
    overlay.classList.remove("is-visible");
  }

  trigger.addEventListener("click", openOverlay);
  backdrop.addEventListener("click", closeOverlay);
  closeBtn.addEventListener("click", closeOverlay);

  document.addEventListener("keydown", function (evt) {
    if (evt.key === "Escape") {
      closeOverlay();
    }
  });
});