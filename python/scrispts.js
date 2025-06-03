document.getElementById('contact-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const nombre = document.getElementById('nombre').value;
  alert(`Gracias por tu mensaje, ${nombre}. ¡Te responderé pronto!`);
  this.reset();
});