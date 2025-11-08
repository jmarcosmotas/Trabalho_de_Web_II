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
            window.location.href="/login";
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
            window.location.href="{/altera-cadastro";
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

    fetch("http://127.0.0.1:5000/api/cadastra",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (response.ok) {
            window.location.href="/login"
        } else {
            throw new Error('Erro na requisição: ' + response.status);
        }
    })
    .catch(err => {
        console.error(err);
        document.getElementById("erro").innerText = "Ocorreu um erro no cadastro";
    });

}

function login(event) {
    event.preventDefault();
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    console.log(dadosUsuario);

    fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na requisição: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        localStorage.setItem("usuario", JSON.stringify(data));
         window.location.href = "/";
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
            window.location.href = "/}";
        } else {
            throw new Error('Erro na requisição: ' + response.status);
        }
    })
    .catch(err => {
        console.error(err);
    });
}