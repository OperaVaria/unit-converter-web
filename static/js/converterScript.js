// Additional JavaScript for converter functionality.

// Declare constant variables:
const inputSystemMenu = document.getElementById("input-system-menu");
const outputSystemMenu = document.getElementById("output-system-menu");
const inputUnitMenu = document.getElementById("input-unit-menu");
const outputUnitMenu = document.getElementById("output-unit-menu");
const inputSystemInfo = document.getElementById("input-system-info");
const outputSystemInfo = document.getElementById("output-system-info");
const inputUnitInfo = document.getElementById("input-unit-info");
const outputUnitInfo = document.getElementById("output-unit-info");
const valueBox = document.getElementById("input-value-box");
const resultField = document.getElementById("result-field");
const symbolField = document.getElementById("symbol-field");

// Tasks on load: corrects soft reloading imperfections.
window.addEventListener("load", windowLoad);
function windowLoad() {
  // Disable unit menus.
  inputUnitMenu.disabled = true;
  outputUnitMenu.disabled = true;
  // (Re)select placeholder items.
  inputSystemMenu.selectedIndex = "0";
  outputSystemMenu.selectedIndex = "0";
  inputUnitMenu.selectedIndex = "0";
  outputUnitMenu.selectedIndex = "0";
  // Reset input value box to placeholder.
  valueBox.value = "";
}

// Long fetch function:
function submitValue(id, value) {
  /* Request content setup.
     Different structure for converter and swap
     button request. Swap button request has units
     swapped */
  if (id === "convert-btn") {
    var subData = {
      sender: id,
      inputValue: valueBox.value,
      inputUnit: inputUnitMenu.value,
      outputUnit: outputUnitMenu.value,
    };
  } else if (id === "swap-btn") {
    var subData = {
      sender: id,
      inputValue: valueBox.value,
      inputUnit: outputUnitMenu.value,
      outputUnit: inputUnitMenu.value,
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
              // Set input unit info box.
              inputUnitInfo.textContent = data.info;
              break;
            case "output-unit-menu":
              // Set output unit info box.
              outputUnitInfo.textContent = data.info;
              break;
            // Sender = convert or swap button: same action.
            case "convert-btn":
            case "swap-btn":
              // Display result.
              resultField.textContent = data.result;
              // Display output unit symbol.
              symbolField.textContent = data.symbol;
              break;
            default:
              /* Any other sender id (should not happen):
                 throw error. */
              throw new Error("Unknown response data!");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    });
}

/* Steps to do with HTML elements after unit system
   selection response */
function setElements(infoElement, MenuElement, data) {
  // Set system info box.
  infoElement.textContent = data.info;
  /* Reset unit menu (remove all elements
     besides placeholder) */
  while (MenuElement.options.length > 1) {
    MenuElement.remove(1);
  }
  // Populate unit menu.
  Object.entries(data.list).forEach(([key, value]) => {
    let newOption = new Option(value, key);
    MenuElement.add(newOption);
  });
  // Set default option to placeholder.
  MenuElement.selectedIndex = 0;
  // Enable select menu if disabled.
  MenuElement.disabled = false;
}

/* Validate calculation buttons:
   Display error if unit selection is incomplete
   or unit value is invalid. */
function validateConvBtn(id, value) {
  if (valueBox.value == "") {
    resultField.textContent = "Hiba!";
    symbolField.textContent = "Hiányzó vagy rossz érték!";
  } else if (inputUnitMenu.value == "") {
    resultField.textContent = "Hiba!";
    symbolField.textContent = "Hiányzó bemeneti mértékegység!";
  } else if (outputUnitMenu.value == "") {
    resultField.textContent = "Hiba!";
    symbolField.textContent = "Hiányzó kimeneti mértékegység!";
  } else {
    submitValue(id, value);
  }
}
