

document.getElementById("compress_btn").addEventListener("click", function() {
    // Disabling the button
    const button = document.getElementById("compress_btn");
    button.disabled = true;

    img_size = document.getElementById("img_size_2");
    const a = document.createElement("a");
    a.id = "download_img";

    const compress_img = document.createElement("img");
    compress_img.id = "compress_img";
    compress_img.alt = "Ваше изображение";

    const loader = document.createElement("div")
    loader.className = "loader";
    loader.id = "loader";
    

    a.appendChild(compress_img);

    const data = {
        name: (document.getElementById("img_name").innerHTML).toString(),
        perc_of_comp: document.getElementById("slider").value
    };
    
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(data)
    };

    if (document.getElementById("img_to_compress") == null){
        alert('Please select an image.');
    }else{
        document.getElementById("image-preview").appendChild(loader);
        fetch('/compress', options)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to download the image');
            }
        })
        .then(dict => {
            // Add Image
            document.getElementById("image-preview").removeChild(loader);
            document.getElementById("image-preview").appendChild(a);
            createTable();


            const img = document.getElementById("compress_img");
            img.src = dict["path"];

            document.getElementById("img_size_2").innerHTML = dict["file_size"] + " Mb"

            // Add download options
            download_image = document.getElementById("download_img");
            download_image.href = dict["path"];;
            download_image.download = "Compress Image.jpg";
        })
        .catch(error => {
            console.error(error);
            alert('An error occurred while downloading the image');
        });
    }
});