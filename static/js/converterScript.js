// Additional JavaScript for converter functionality.

// Declare constant variables:
const inputSystemMenu = document.getElementById("input_system_menu");
const outputSystemMenu = document.getElementById("output_system_menu");
const inputUnitMenu = document.getElementById("input_unit_menu");
const outputUnitMenu = document.getElementById("output_unit_menu");
const inputSystemInfo = document.getElementById("input_system_info");
const outputSystemInfo = document.getElementById("output_system_info");
const inputUnitInfo = document.getElementById("input_unit_info");
const outputUnitInfo = document.getElementById("output_unit_info");
const valueBox = document.getElementById("input_value_box");
const resultField = document.getElementById("result_field");
const symbolField = document.getElementById("symbol_field");

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

// Fetch function:
function submitValue(id, value) {

    /* Request content setup.
       Different structure for converter button request. */
    if (id === "convert_btn") {
        var sub_data = {
            sender: id,
            input_value: valueBox.value,
            input_unit: inputUnitMenu.value, 
            output_unit: outputUnitMenu.value
        }
    } else {
        var sub_data = {
            sender: id,
            value: value
        }
    }

    // Create and send request json.
    fetch(`${window.origin}/fetch-traffic`, {
        method: "POST",
        body: JSON.stringify(sub_data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

    // Response handling based upon sender.
    .then(function (response) {
        response.json().then(function (data) {
            switch(data.req_sender) {
                case "input_system_menu":
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
                case "output_system_menu":
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
                case "input_unit_menu":
                    // Set input unit info box.
                    inputUnitInfo.textContent = data.info;
                    break;
                case "output_unit_menu":
                    // Set output unit info box.
                    outputUnitInfo.textContent = data.info;
                    break;
                case "convert_btn":
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

/* Validate calculation button:
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