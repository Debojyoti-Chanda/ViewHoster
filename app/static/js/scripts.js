// Ensure the DOM is fully loaded before attaching event listeners
document.addEventListener("DOMContentLoaded", () => {
    const screenshotList = document.querySelector("ul"); // Parent element

    // Use event delegation to listen for clicks on buttons
    screenshotList.addEventListener("click", (event) => {
        const target = event.target;

        // Check if the clicked element is an "Extract Text" button
        if (target.classList.contains("extract-btn")) {
            const filename = target.getAttribute("data-filename");
            extractText(filename);
        }
    });
});

// Function to call the extract text API and display the result
function extractText(filename) {
    fetch(`/extract_text/${filename}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                alert(`Error extracting text: ${data.error}`);
            } else {
                displayExtractedTextModal(filename, data.text);
            }
        })
        .catch(error => {
            console.error("Error fetching extracted text:", error);
            alert("Failed to extract text. Please try again.");
        });
}

// Function to display the extracted text in a modal
function displayExtractedTextModal(filename, text) {
    const textModal = document.createElement("div");
    textModal.style.position = "fixed";
    textModal.style.top = "50%";
    textModal.style.left = "50%";
    textModal.style.transform = "translate(-50%, -50%)";
    textModal.style.padding = "20px";
    textModal.style.backgroundColor = "white";
    textModal.style.border = "1px solid #ccc";
    textModal.style.boxShadow = "0 4px 8px rgba(0,0,0,0.2)";
    textModal.style.zIndex = "1000";

    textModal.innerHTML = `
        <h3>Extracted Text for ${filename}</h3>
        <pre>${text}</pre>
        <button onclick="document.body.removeChild(this.parentNode)">Close</button>
    `;

    // Append the modal to the document body
    document.body.appendChild(textModal);
}

