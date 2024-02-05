const dropzone = document.getElementById('dropzone');

const slider = document.getElementById("slider");
const currentValue = document.querySelector(".current-value"); 

slider.addEventListener("input", function() {
    const sliderValue = slider.value;
    currentValue.textContent = sliderValue + "%";
});

// Canceling default actions for dragover and dragleave events
dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.style.border = '2px dashed #666';
});

dropzone.addEventListener('dragleave', () => {
    dropzone.style.border = '2px dashed #ccc';
});

