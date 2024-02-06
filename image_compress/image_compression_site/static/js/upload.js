dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    console.log("!")
    const file = e.dataTransfer.files[0];

    if (file && file.type.startsWith('image/')) {
        upload_image(file);
        
    } else {
        alert('Please select an image.');
    }
});

// Processing a click to select a file through a dialog box
dropzone.addEventListener('click', () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.style.display = 'none';
    console.log("!!")
    input.addEventListener('change', (e) => {
        const file = e.target.files[0];

        if (file && file.type.startsWith('image/')) {
            upload_image(file);
        } else {
            alert('Please select an image.');
        }
    });

    document.body.appendChild(input);
    input.click();
    document.body.removeChild(input);
});