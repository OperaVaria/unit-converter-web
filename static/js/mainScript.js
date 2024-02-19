// Main JavasScript for functionality present on all pages.

// Declare constant variables:
const yearLocation = document.getElementById("year-location");

// Insert current year into copyright info if element exists.
if (document.body.contains(yearLocation)) {
  let currentYear = new Date().getFullYear();
  yearLocation.innerHTML = currentYear;
}

// Load a page, same tab.
function loadPage(Page) {
  window.location.href = Page;
}

// Load a page in new tab.
function loadNewTab(Page) {
  window.open(Page, "_blank");
}
