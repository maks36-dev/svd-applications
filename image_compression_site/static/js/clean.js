document.getElementById("clear").addEventListener("click", function() {
    if (document.getElementById("img_to_compress") == null){
        alert('There is no image.');
    } else{
        // clearing dropzone
        dropzone.removeChild(document.getElementById("img_to_compress"));
        dropzone.innerHTML = "Перетащите сюда изображение";

        // enabling the button
        const button = document.getElementById("compress_btn");
        button.disabled = false;

        // clearing output zone
        document.getElementById("image-preview").innerHTML = "";

        // clearing info table in dropzone
        document.getElementById("img_size_1").innerHTML = "";
        document.getElementById("img_name").innerHTML = "";
    }
});