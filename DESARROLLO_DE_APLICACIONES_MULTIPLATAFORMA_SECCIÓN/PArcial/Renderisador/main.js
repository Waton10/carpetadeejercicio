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

        resizedImage.src = canvas.toDataURL('image/jpeg');
      };
    };

    reader.readAsDataURL(imageFile);
  } else {
    alert('Por favor, seleccione una imagen y proporcione dimensiones válidas.');
  }
}
