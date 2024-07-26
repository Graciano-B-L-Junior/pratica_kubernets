// public/script.js
console.log('Hello from the front-end!');
fetch('http://localhost:3000')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    document.querySelector("h1").innerText = data.quote
    document.querySelector("h2").innerText = data.source
  })
  .catch(error => {
    console.error('Erro:', error);
  });
