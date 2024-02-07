document.getElementById("compress_btn").addEventListener("click", function() {
    img_size = document.getElementById("img_size_2");

    // Disabling the button
    const button = document.getElementById("compress_btn");
    button.disabled = true;

    // link to show img
    const compress_img = document.createElement("img");
    compress_img.id = "compress_img";
    compress_img.alt = "Ваше изображение";

    // rotating animation
    const loader = document.createElement("div")
    loader.className = "loader";
    loader.id = "loader";
    
    // link to download img
    const a = document.createElement("a");
    a.id = "download_img";
    a.appendChild(compress_img);

    // data about name and percent of compress 
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
        document.getElementById("image-preview").appendChild(loader); // add loader

        fetch('/compress', options) // POST request for compressed image
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to download the image');
            }
        })
        .then(dict => {
            // add Image
            document.getElementById("image-preview").removeChild(loader);
            document.getElementById("image-preview").appendChild(a);
            const img = document.getElementById("compress_img");
            img.src = dict["path"];

            // add table inform
            createTable();
            document.getElementById("img_size_2").innerHTML = dict["file_size"] + " Mb"

            // add download options
            download_image = document.getElementById("download_img");
            download_image.href = dict["path"];
            download_image.download = "Compress Image.jpg";
        })
        .catch(error => {
            alert('An error occurred while downloading the image');
        });
    }
});