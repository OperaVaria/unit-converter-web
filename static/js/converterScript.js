// Additional JavaScript for converter functionality.

// Declare constant variables:
const inputSystemInfo = document.getElementById("input-system-info");
const outputSystemInfo = document.getElementById("output-system-info");
const inputUnitInfo = document.getElementById("input-unit-info");
const outputUnitInfo = document.getElementById("output-unit-info");
const valueBox = document.getElementById("input-value-box");
const convertButton = document.getElementById("convert-btn");
const resultField = document.getElementById("result-field");
const symbolField = document.getElementById("symbol-field");

// Choices.js setup.

// Global settings for Choices objects.
let choicesGlobSet = {
  allowHTML: false,
  noResultsText: noResult,
  position: "bottom",
  searchFields: ["label"],
  searchPlaceholderValue: searchPlaceholder,
  shouldSort: false,
};
// Create Choices objects.
const inputSystemMenu = new Choices(
  document.getElementById("input-system-menu"),
  choicesGlobSet
);
const outputSystemMenu = new Choices(
  document.getElementById("output-system-menu"),
  choicesGlobSet
);
const inputUnitMenu = new Choices(
  document.getElementById("input-unit-menu"),
  choicesGlobSet
);
const outputUnitMenu = new Choices(
  document.getElementById("output-unit-menu"),
  choicesGlobSet
);

// Tasks on load: corrects soft reloading imperfections.
window.addEventListener("load", windowLoad);
function windowLoad() {
  // Disable unit menus.
  inputUnitMenu.disable();
  outputUnitMenu.disable();
  // (Re)select placeholder items.
  inputSystemMenu.setChoiceByValue("");
  outputSystemMenu.setChoiceByValue("");
  inputUnitMenu.setChoiceByValue("");
  outputUnitMenu.setChoiceByValue("");
  // Reset input value box to placeholder.
  valueBox.value = "";
}

// Long fetch function:
function submitValue(id, value) {
  /* Request content setup.
     Different structure for converter and swap
     button request.
     (Swap button request has units swapped) */
  if (id === "convert-btn") {
    var subData = {
      sender: id,
      inputValue: valueBox.value,
      inputUnit: inputUnitMenu.getValue(true),
      outputUnit: outputUnitMenu.getValue(true),
    };
  } else if (id === "swap-btn") {
    var subData = {
      sender: id,
      inputValue: valueBox.value,
      inputUnit: outputUnitMenu.getValue(true),
      outputUnit: inputUnitMenu.getValue(true),
    };
  } else {
    var subData = {
      sender: id,
      value: value,
    };
  }

  // Create and send request json.
  fetch(`${window.origin}/fetch-traffic`, {
    method: "POST",
    body: JSON.stringify(subData),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
    }),
  })
    // Response handling based upon sender.
    .then((response) => {
      response
        .json()
        .then((data) => {
          switch (data.reqSender) {
            case "input-system-menu":
              // Call setup function.
              setElements(inputSystemInfo, inputUnitMenu, data);
              break;
            case "output-system-menu":
              // Call setup function.
              setElements(outputSystemInfo, outputUnitMenu, data);
              break;
            case "input-unit-menu":
              // Set input unit info box with animation.
              animatedFade(inputUnitInfo, data.info);
              break;
            case "output-unit-menu":
              // Set output unit info box with animation.
              animatedFade(outputUnitInfo, data.info);
              break;
            // Sender = convert or swap button: same action.
            case "convert-btn":
            case "swap-btn":
              // Set result and symbol field with animation.
              animatedFade(resultField, data.result);
              animatedFade(symbolField, data.symbol);
              break;
            default:
              /* Any other sender id (should not happen):
                 throw error. */
              throw new Error("Unknown response data!");
          }
        })
        // Error catching.
        .catch((error) => {
          console.log(error);
        });
    });
}

/* Steps to do with HTML elements after unit system
   selection response. */
function setElements(infoElement, menuObject, data) {
  // Refresh system info box with animation.
  animatedFade(infoElement, data.info);
  // Reset unit menu.
  menuObject.destroy();
  menuObject.init();
  // Populate unit menu.
  menuObject.setChoices(data.list, "value", "label", false);
  // Enable select menu if disabled.
  menuObject.enable();
}

/* Rudimentary fade-out fade-in animation
   with text change. Coupled with CSS
   opacity transition. */
function animatedFade(element, newText) {
  element.style.opacity = "0";
  setTimeout(() => {
    element.textContent = newText;
    element.style.opacity = "1";
  }, 600);
}

/* Validate calculation buttons:
   Display error with animation
   if unit selection is incomplete
   or unit value is invalid.
   String variables in HTML file so jinja2
   can insert proper translation. */
function validateConvBtn(id, value) {
  if (valueBox.value == "") {
    animatedFade(resultField, errorText);
    animatedFade(symbolField, missingValue);
  } else if (inputUnitMenu.getValue(true) == "") {
    animatedFade(resultField, errorText);
    animatedFade(symbolField, missingInput);
  } else if (outputUnitMenu.getValue(true) == "") {
    animatedFade(resultField, errorText);
    animatedFade(symbolField, missingOutput);
  } else {
    submitValue(id, value);
  }
}

// Input value field: submit if enter pressed.
valueBox.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    convertButton.click();
  }
});
