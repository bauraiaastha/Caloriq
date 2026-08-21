const foodImage = document.getElementById("food-image");
const scannerBox = document.querySelector(".scanner-box");

let selectedFile = null;


foodImage.addEventListener("change", function () {

    selectedFile = foodImage.files[0];

    if (!selectedFile) {
        return;
    }


    // Create image URL
    const imageURL = URL.createObjectURL(selectedFile);


    // Create image preview
    const preview = document.createElement("img");

    preview.src = imageURL;

    preview.classList.add("food-preview");


    // Remove old preview if there is one
    const oldPreview =
        document.querySelector(".food-preview");

    if (oldPreview) {
        oldPreview.remove();
    }


    // Add new preview
    scannerBox.prepend(preview);


    // Create Analyze button
    createAnalyzeButton();

});


function createAnalyzeButton() {

    // Prevent duplicate buttons
    const existingButton =
        document.querySelector(".analyze-button");

    if (existingButton) {
        existingButton.remove();
    }


    const analyzeButton =
        document.createElement("button");

    analyzeButton.type = "button";

    analyzeButton.classList.add("analyze-button");

    analyzeButton.textContent =
        "Analyze My Meal →";


    // Add button to scanner
    scannerBox.appendChild(analyzeButton);


    // Button click
    analyzeButton.addEventListener(
        "click",
        analyzeMeal
    );

}


function analyzeMeal() {

    const analyzeButton =
        document.querySelector(".analyze-button");


    analyzeButton.textContent =
        "Analyzing your meal...";


    analyzeButton.disabled = true;


    // Simulate AI processing
    setTimeout(function () {

        analyzeButton.textContent =
            "Analysis complete ✓";

        showDemoResult();

    }, 1800);

}


function showDemoResult() {

    // Remove an existing result
    const oldResult =
        document.querySelector(".demo-result");

    if (oldResult) {
        oldResult.remove();
    }


    const result =
        document.createElement("div");

    result.classList.add("demo-result");


    result.innerHTML = `

        <div class="result-line"></div>


        <!-- =========================
             FOOD IDENTIFICATION
             ========================= -->

        <div class="result-heading">

            <span class="result-label">
                WE FOUND YOUR MEAL
            </span>

            <h3>
                Indian Thali
            </h3>

        </div>


        <!-- =========================
             NUTRITION
             ========================= -->

        <div class="nutrition-section">

            <div class="calorie-main">

                <strong>
                    620
                </strong>

                <span>
                    kcal
                </span>

            </div>


            <div class="nutrition-grid">

                <div class="nutrition-item">

                    <strong>
                        24g
                    </strong>

                    <span>
                        Protein
                    </span>

                </div>


                <div class="nutrition-item">

                    <strong>
                        78g
                    </strong>

                    <span>
                        Carbs
                    </span>

                </div>


                <div class="nutrition-item">

                    <strong>
                        22g
                    </strong>

                    <span>
                        Fat
                    </span>

                </div>

            </div>

        </div>


        <!-- =========================
             FOOD STORY
             ========================= -->

        <div class="food-story">

            <div class="story-icon">
                ✦
            </div>

            <div>

                <span class="result-label">
                    A LITTLE FOOD STORY
                </span>

                <h4>
                    More than just a meal.
                </h4>

                <p>

                    Indian thalis bring together
                    different flavours, textures and
                    regional traditions on one plate.
                    The combination varies beautifully
                    from one part of India to another.

                </p>

            </div>

        </div>


        <!-- =========================
             BETTER ALTERNATIVE
             ========================= -->

        <div class="alternative">

            <div class="alternative-heading">

                <span>
                    🌿
                </span>

                <div>

                    <span class="result-label">
                        A LIGHTER CHOICE?
                    </span>

                    <h4>
                        Try a balanced thali
                    </h4>

                </div>

            </div>


            <div class="alternative-info">

                <div>

                    <strong>
                        ~480 kcal
                    </strong>

                    <span>
                        approximately 140 kcal less
                    </span>

                </div>


                <span class="alternative-arrow">
                    →
                </span>

            </div>

        </div>


        <p class="demo-note">

            ✦ AI-powered food analysis coming next

        </p>

    `;


    scannerBox.appendChild(result);

}