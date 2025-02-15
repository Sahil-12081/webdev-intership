document.addEventListener('DOMContentLoaded', function() {
    const temperatureInput = document.getElementById('temperature');
    const typeSelect = document.getElementById('type');
    const convertBtn = document.getElementById('convertBtn');
    const resultDisplay = document.getElementById('result');

    function validateInput(value) {
        return !isNaN(value) && value !== '';
    }

    function convertTemperature() {
        const temperature = parseFloat(temperatureInput.value);
        const type = typeSelect.value;

        if (!validateInput(temperature)) {
            resultDisplay.textContent = 'Please enter a valid number';
            return;
        }

        let result;
        if (type === 'fahrenheit') {
            // Convert Fahrenheit to Celsius
            result = ((temperature - 32) * 5/9).toFixed(4);
            resultDisplay.textContent = `${result} °C`;
        } else {
            // Convert Celsius to Fahrenheit
            result = ((temperature * 9/5) + 32).toFixed(4);
            resultDisplay.textContent = `${result} °F`;
        }
    }

    // Event listeners
    convertBtn.addEventListener('click', convertTemperature);

    // Allow Enter key to trigger conversion
    temperatureInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            convertTemperature();
        }
    });

    // Clear invalid input
    temperatureInput.addEventListener('input', function() {
        if (this.value && !validateInput(this.value)) {
            resultDisplay.textContent = 'Please enter a valid number';
        } else {
            resultDisplay.textContent = '--';
        }
    });
});
