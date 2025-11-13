function alteraSenha(){
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    console.log(dadosUsuario);

    fetch("/altera-senha", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "h-login.html";
        } else {
            throw new Error('Erro na requisição: ' + response.status);
        }
    })
    .catch(err => {
        console.error(err);
    });
}

function verificaEmail(event){
    event.preventDefault();
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    console.log(dadosUsuario);

    fetch("/verifica-email",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "h-altera-cadastro.html";
        } else {
            throw new Error('Erro na requisição: ' + response.status);
        }
    })
    .catch(err => {
        console.error(err);
        document.getElementById("erro").innerText = "E-mail não possui cadastro";
    });
}

function cadastro(event){
    event.preventDefault();
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    console.log(dadosUsuario);

    fetch("/cadastra",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "h-login.html";
        } else {
            throw new Error('Erro na requisição: ' + response.status);
        }
    })
    .catch(err => {
        console.error(err);
        document.getElementById("erro").innerText = "Ocorreu um erro no cadastro";
    });
}

function login(event){
    event.preventDefault();
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    console.log(dadosUsuario);
    if dadosUsuario.

    fetch("../autentica.json")
    // fetch("../autentica.json", {
    //     method: "POST",
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify(dadosUsuario)
    // })
    .then(response => {
        
        if (!response.ok) {
            throw new Error('Erro na requisição: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // alert("Dados recebidos do JSON: " + JSON.stringify(data));
        localStorage.setItem("usuario", JSON.stringify(data));
        window.location.href = "../inicio/h-index.html";
    })
    .catch(err => {
        console.error(err);
        document.getElementById("erro").innerText = "E-mail ou Senha Invalido";
    });
}

function alteraCadastro(){
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    console.log(dadosUsuario);

    fetch("/altera-cadastro", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "../inicio/h-index.html";
        } else {
            throw new Error('Erro na requisição: ' + response.status);
        }
    })
    .catch(err => {
        console.error(err);
    });
}