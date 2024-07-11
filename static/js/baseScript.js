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
function loadPage(Page) {
  window.location.replace(Page);
}

// Load a page in new tab.
function loadNewTab(Page) {
  window.open(Page, "_blank");
}
