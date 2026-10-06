const photoInput = document.getElementById("photo");
const preview = document.getElementById("preview");


// PHOTO PREVIEW

photoInput.addEventListener("change", function () {

    const file = this.files[0];

    if (file) {

        preview.src = URL.createObjectURL(file);

        preview.style.display = "block";
    }
});


// BODY ANALYSIS

function analyzeBody() {

    const file = photoInput.files[0];

    if (!file) {

        alert("Please upload your full-body photo.");

        return;
    }

    document.getElementById("analysisResult").innerHTML = `
        <h3>🤖 FitAI Analysis</h3>

        <p>Person detected successfully.</p>

        <p>
            Estimated Height:
            <strong>165 cm</strong>
        </p>

        <p>
            Estimated Body Profile:
            <strong>Medium</strong>
        </p>

        <p>
            Suggested Size:
            <strong>M</strong>
        </p>

        <small>
            Note: These are prototype estimates.
        </small>
    `;
}


// OUTFIT RECOMMENDATION

function recommendOutfit() {

    const occasion =
        document.getElementById("occasion").value;

    const outfit =
        document.getElementById("outfit").value;

    const color =
        document.getElementById("color").value;

    const budget =
        document.getElementById("budget").value;


    let size = "M";

    let message = "";


    if (occasion === "party") {

        message =
            "✨ A stylish party outfit is recommended.";

    }

    else if (occasion === "office") {

        message =
            "💼 A professional outfit is recommended.";

    }

    else if (occasion === "college") {

        message =
            "🎓 A comfortable college outfit is recommended.";

    }

    else if (occasion === "traditional") {

        message =
            "🌸 A traditional outfit is recommended.";

    }

    else {

        message =
            "😊 A comfortable casual outfit is recommended.";

    }


    document.getElementById(
        "recommendation"
    ).style.display = "block";


    document.getElementById(
        "resultOccasion"
    ).innerText = occasion;


    document.getElementById(
        "resultOutfit"
    ).innerText = outfit;


    document.getElementById(
        "resultColor"
    ).innerText = color;


    document.getElementById(
        "resultBudget"
    ).innerText = "₹" + budget;


    document.getElementById(
        "resultSize"
    ).innerText = size;


    document.getElementById(
        "resultMessage"
    ).innerText = message;
}
