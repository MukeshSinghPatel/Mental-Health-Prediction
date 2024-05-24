document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictionForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Check if all form fields are filled (basic validation)
        let formValid = true;
        const inputs = form.querySelectorAll("input[required]");
        inputs.forEach(input => {
            if (!input.checked && input.type === "radio" && !form.querySelector(`input[name=${input.name}]:checked`)) {
                formValid = false;
            }
            if (input.type === "text" && input.value.trim() === "") {
                formValid = false;
            }
        });

        if (formValid) {
            alert("You have selected all options successfully");

            // Simulate form submission and prediction result
            setTimeout(() => {
                // This is where you would normally handle the form submission
                // For demonstration, we're just showing another alert
                const predictionResult = document.getElementById("predictionResult");
                predictionResult.innerHTML = "<h3>Predicted Value: Example Prediction</h3>";
                alert("Prediction Complete. Please Click 'OK' Button for result.\n Result is shown under Form.");

                // Optionally, you can then actually submit the form to the server
                form.submit();
            }, 1000);
        } else {
            alert("Please fill out all required fields");
        }
    });
});
