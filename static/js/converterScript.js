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
       button request. */
    if (id === "convert-btn" || id === "swap-btn") {
        var subData = {
            sender: id,
            inputValue: valueBox.value,
            inputUnit: inputUnitMenu.value,
            outputUnit: outputUnitMenu.value
        }
    } else {
        var subData = {
            sender: id,
            value: value
        }
    }

    // Create and send request json.
    fetch(`${window.origin}/fetch-traffic`, {
        method: "POST",
        body: JSON.stringify(subData),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

    // Response handling based upon sender.
    .then(function (response) {
        response.json().then(function (data) {
            switch(data.reqSender) {
                case "input-system-menu":
                    // Set input system info box.
                    inputSystemInfo.textContent = data.info;
                    // Reset input unit menu.
                    removeAll(inputUnitMenu);
                    // Populate input unit menu.
                    Object.entries(data.list).forEach(([key, value]) => {
                        let newOption = new Option(value, key)
                        inputUnitMenu.add(newOption)
                    });
                    // Set default option to placeholder.
                    inputUnitMenu.selectedIndex = 0;
                    // Enable select menu if disabled.
                    inputUnitMenu.disabled = false;
                    break;
                case "output-system-menu":
                    // Set output system info box.
                    outputSystemInfo.textContent = data.info;
                    // Reset output unit menu.
                    removeAll(outputUnitMenu);
                    // Populate output unit menu.
                    Object.entries(data.list).forEach(([key, value]) => {
                        let newOption = new Option(value, key);
                        outputUnitMenu.add(newOption);
                    });
                    // Set default option to placeholder.
                    outputUnitMenu.selectedIndex = 0;
                    // Enable select menu if disabled.
                    outputUnitMenu.disabled = false;
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
                    console.log("Unknown response data!");
                }
            })
    })
}

// Remove all elements, except placeholder, from select menu.
function removeAll(selectMenu) {
    while (selectMenu.options.length > 1) {
        selectMenu.remove(1);
    }
}

/* function menuSetup(menuObj) {
    console.log(menuObj)
    // Set input system info box.
    inputSystemInfo.textContent = data.info;
    // Reset input unit menu.
    removeAll(inputUnitMenu);
    // Populate input unit menu.
    Object.entries(data.list).forEach(([key, value]) => {
        let newOption = new Option(value, key)
        inputUnitMenu.add(newOption)
    });
    // Set default option to placeholder.
    inputUnitMenu.selectedIndex = 0;
    // Enable select menu if disabled.
    inputUnitMenu.disabled = false;
} */


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
