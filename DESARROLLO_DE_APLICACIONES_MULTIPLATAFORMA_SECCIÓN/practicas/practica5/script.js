function calcularEstadisticas() {
    const dataInput = document.getElementById('dataInput').value;
    const datos = dataInput.split(',').map(Number);

    const media = calcularMedia(datos);
    const varianza = calcularVarianza(datos);
    const moda = calcularModa(datos);
    const mediana = calcularMediana(datos);
    const desviacion = calcularDesviacion(datos);

    document.getElementById('mediaResult').textContent = media;
    document.getElementById('varianzaResult').textContent = varianza;
    document.getElementById('modaResult').textContent = moda;
    document.getElementById('medianaResult').textContent = mediana;
    document.getElementById('desviacionResult').textContent = desviacion;
}

function calcularMedia(datos) {
    const sum = datos.reduce((acc, val) => acc + val, 0);
    return sum / datos.length;
}

function calcularVarianza(datos) {
    const media = calcularMedia(datos);
    const sumSquaredDiff = datos.reduce((acc, val) => acc + (val - media) ** 2, 0);
    return sumSquaredDiff / datos.length;
}

function calcularModa(datos) {
    const counts = {};
    datos.forEach(num => {
        counts[num] = (counts[num] || 0) + 1;
    });

    let moda = [];
    let maxCount = 0;
    for (const num in counts) {
        if (counts[num] > maxCount) {
            moda = [num];
            maxCount = counts[num];
        } else if (counts[num] === maxCount) {
            moda.push(num);
        }
    }

    return moda.join(', ');
}

function calcularMediana(datos) {
    datos.sort((a, b) => a - b);
    const middle = Math.floor(datos.length / 2);
    if (datos.length % 2 === 0) {
        return (datos[middle - 1] + datos[middle]) / 2;
    } else {
        return datos[middle];
    }
}

function calcularDesviacion(datos) {
    const media = calcularMedia(datos);
    const sumSquaredDiff = datos.reduce((acc, val) => acc + (val - media) ** 2, 0);
    return Math.sqrt(sumSquaredDiff / datos.length);
}
