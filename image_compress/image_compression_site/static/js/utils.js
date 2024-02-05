function createTable() {
    var table = document.createElement("table");
    var row = document.createElement("tr");
    var th = document.createElement("th");
    th.textContent = "Размер: ";

    var td = document.createElement("td");
    td.id = "img_size_2";
  
    row.appendChild(th);
    row.appendChild(td);

    table.appendChild(row);
  
    var container = document.getElementById("image-preview");
  
    container.appendChild(table);
}

async function fetchData(formData) {
    try {
    const response = await fetch("/upload", {
                                    method: 'POST',
                                    body: formData,
                                });
    if (!response.ok) {
        throw new Error('Ошибка HTTP: ' + response.status);
    }
        const data = await response.json();
        return data["file_size"];
    } catch (error) {
        console.error('Произошла ошибка:', error);
    }
}

async function upload_image(file){
    const reader = new FileReader();

    const formData = new FormData();
    formData.append('file', file);
    var size_of_img = await fetchData(formData);
    // res = fetch('/upload', {
    //     method: 'POST',
    //     body: formData,
    // }).then(response => response.json())
    document.getElementById("img_size_1").innerHTML = size_of_img + " Mb"
    reader.onload = (e) => {
        const img = new Image();
        img.src = e.target.result;
        img.style.maxWidth = '100%';
        img.id = "img_to_compress"

        dropzone.innerHTML = '';
        dropzone.appendChild(img);
    };
    document.getElementById("img_name").innerHTML = file.name;

    reader.readAsDataURL(file);
}