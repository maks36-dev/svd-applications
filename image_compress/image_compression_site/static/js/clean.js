document.getElementById("clear").addEventListener("click", function() {
    if (document.getElementById("img_to_compress") == null){
        alert('There is no image.');
    } else{
        dropzone.removeChild(document.getElementById("img_to_compress"));

        dropzone.innerHTML = "Перетащите сюда изображение";

        // document.getElementById("compress_img").src = "";
        // document.getElementById("download_img").href = "";
        // document.getElementById("download_img").download = "";

        const button = document.getElementById("compress_btn");
        button.disabled = false;

        document.getElementById("image-preview").innerHTML = "";

        // document.getElementById("img_size_2").innerHTML = "";
        document.getElementById("img_size_1").innerHTML = "";
        document.getElementById("img_name").innerHTML = "";
    }
});