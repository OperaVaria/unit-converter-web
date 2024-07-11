// Base JavasScript for functionality present on all pages.

// Declare constants:
const resetBtn = document.getElementById("reset-btn");
const githubBtn = document.getElementById("github-btn");

// Add event listeners:

// Calculator reset button.
if (resetBtn) {
  resetBtn.addEventListener("click", () => {
    window.location.reload(true);
  });
}

// Source code button.
if (githubBtn) {
  githubBtn.addEventListener("click", () => {
    loadNewTab("https://github.com/OperaVaria/unit-converter-web");
  });
}

// General link buttons.
document.querySelectorAll(".link-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    loadPage(btn.getAttribute("data-target"));
  });
});

// Page opening functions:

// Load a page, same tab.
<<<<<<< HEAD
function loadPage(page) {
  let safePage = encodeURI(page);
  window.location.assign(safePage);
=======
function loadPage(Page) {
  window.location.replace(Page);
>>>>>>> 0408d5f01ba7dbaaee1b7beed05a940ecab6418c
}

// Load a page in new tab.
function loadNewTab(page) {
  let safePage = encodeURI(page);
  window.open(safePage, "_blank");
}
