let imageInput = document.getElementById('imageInput');
let widthInput = document.getElementById('widthInput');
let heightInput = document.getElementById('heightInput');
let resizedImage = document.getElementById('resizedImage');

function resizeImage() {
  let imageFile = imageInput.files[0];
  let width = parseInt(widthInput.value);
  let height = parseInt(heightInput.value);

  if (imageFile && !isNaN(width) && !isNaN(height)) {
    let reader = new FileReader();

    reader.onload = function (e) {
      let img = new Image();
      img.src = e.target.result;

      img.onload = function () {
        let canvas = document.createElement('canvas');
        canvas.width = width;
        canvas.height = height;

        let ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0, width, height);

        let resizedDataUrl = canvas.toDataURL('image/jpeg');
        resizedImage.src = resizedDataUrl;
        resizedImage.style.display = 'block';
      };
    };

    reader.readAsDataURL(imageFile);
  } else {
    alert('Por favor, seleccione una imagen y proporcione dimensiones válidas.');
  }
}

function saveImage() {
  let dataUrl = resizedImage.src;
  if (dataUrl) {
    // Crear un enlace temporal
    let link = document.createElement('a');
    link.href = dataUrl;
    link.download = 'resized_image.jpg';
    
    // Simular un clic en el enlace para descargar la imagen
    link.click();
  } else {
    alert('Primero redimensiona una imagen antes de guardarla.');
  }
}
