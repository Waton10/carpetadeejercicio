const addProductForm = document.querySelector("#add-product-form");
const productNameInput = document.querySelector("#product-name");
const productPriceInput = document.querySelector("#product-price");
const productQuantityInput = document.querySelector("#product-quantity");

addProductForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const productName = productNameInput.value;
    const productPrice = parseFloat(productPriceInput.value);
    const productQuantity = parseInt(productQuantityInput.value);

    if (productName && !isNaN(productPrice) && !isNaN(productQuantity)) {
        // Agregar el nuevo producto a la lista
        const newProduct = {
            id: productors.length + 1,
            name: productName,
            price: productPrice,
            cantidad: productQuantity
        };
        productors.push(newProduct);

        // Limpiar los campos del formulario
        productNameInput.value = "";
        productPriceInput.value = "";
        productQuantityInput.value = "";

        // Actualizar la tabla
        filasTabla();
    }
});
function filasTabla() {
    // Resto del código

    // Agregar un evento de clic para cada botón "Eliminar"
    const removeButtons = contentFilas.querySelectorAll(".remove-button");
    removeButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            // Eliminar el producto de la lista
            productors.splice(index, 1);
            // Actualizar la tabla
            filasTabla();
        });
    });
}
function filasTabla() {
    // Resto del código

    // Calcular el total de precios multiplicado por la cantidad
    const totalPriceElement = document.querySelector("#total-amount");
    let totalPrice = 0;

    productors.forEach((item) => {
        const rowPrice = item.price * item.cantidad;
        totalPrice += rowPrice;
    });

    totalPriceElement.textContent = totalPrice.toFixed(2);
}

// Llama a filasTabla() para mostrar el total inicial
filasTabla();
