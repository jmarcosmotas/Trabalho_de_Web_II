document.addEventListener("DOMContentLoaded", () => {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    const linksDiv = document.querySelector(".links");
    if(usuario){
        const primeiroNome = usuario.nome.split(" ")[0];
        linksDiv.style.display = "none";
        console.log("Nome do usuário:", usuario.nome); 
        document.getElementById("oculto").innerHTML = `Olá <strong>${primeiroNome}</strong>,<br> seja bem-vindo`;

    }
});