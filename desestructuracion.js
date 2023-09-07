const eventos = [
    {
      titulo: 'Evento 1',
      fecha: '2023-09-10',
      hora: '14:00',
      descripcion: 'Descripción del evento 1'
    },
    {
      titulo: 'Evento 2',
      fecha: '2023-09-15',
      hora: '16:30',
      descripcion: 'Descripción del evento 2'
    },
    {
      titulo: 'Evento 3',
      fecha: '2023-09-20',
      hora: '10:00',
      descripcion: 'Descripción del evento 3'
    }
  ];
  for (const evento of eventos) {
    const { titulo, fecha, hora, descripcion } = evento;
    console.log(`Título: ${titulo}`);
    console.log(`Fecha: ${fecha}`);
    console.log(`Hora: ${hora}`);
    console.log(`Descripción: ${descripcion}`);
    console.log('---');
  }
  function mostrarCampos({ titulo, fecha, hora, descripcion }) {
    console.log(`Título: ${titulo}`);
    console.log(`Fecha: ${fecha}`);
    console.log(`Hora: ${hora}`);
    console.log(`Descripción: ${descripcion}`);
  }
  
  const eventoEjemplo = {
    titulo: 'Evento de Ejemplo',
    fecha: '2023-09-25',
    hora: '19:00',
    descripcion: 'Descripción del evento de ejemplo'
  };
  
  mostrarCampos(eventoEjemplo);
  const [, segundoEvento, ...restoEventos] = eventos;

  const { titulo: tituloAnterior, fecha: fechaAnterior, hora: horaAnterior, descripcion: descripcionAnterior } = eventos[0];
  const { titulo: tituloActual, fecha: fechaActual, hora: horaActual, descripcion: descripcionActual } = segundoEvento;
  
  console.log('Datos del evento anterior:');
  console.log(`Título: ${tituloAnterior}`);
  console.log(`Fecha: ${fechaAnterior}`);
  console.log(`Hora: ${horaAnterior}`);
  console.log(`Descripción: ${descripcionAnterior}`);
  console.log('---');
  console.log('Datos del segundo evento:');
  console.log(`Título: ${tituloActual}`);
  console.log(`Fecha: ${fechaActual}`);
  console.log(`Hora: ${horaActual}`);
  console.log(`Descripción: ${descripcionActual}`);
  console.log('---');
      