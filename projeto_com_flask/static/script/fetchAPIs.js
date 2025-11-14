function cadastro(event) {
    event.preventDefault();
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    const erroDiv = document.getElementById("erro");

    if (dadosUsuario.senha !== dadosUsuario.confirmaSenha) {
        erroDiv.innerText = "As senhas não coincidem!";
        return;
    }
    dadosUsuario.senha = CryptoJS.SHA256(dadosUsuario.senha).toString();
    delete dadosUsuario.confirmaSenha;
    fetch("http://127.0.0.1:5000/api/cadastra", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
        .then(response => {
            if (response.ok) {
                window.location.href = "/login";
            } else {              
                return response.json().then(erroJson => {
                    document.getElementById("erro").innerText = erroJson.error;
                    console.log("Mensagem do servidor:", erroJson.error);
                });
            }
        })
        .catch(err => {
            console.error("Erro no fetch:", err);
        });
}

window.addEventListener("DOMContentLoaded", () => {
    const cpfSalvo = localStorage.getItem("cpf");

    const campoCpf = document.getElementById("cpf");
    const lembrarCheck = document.getElementById("lembrar");

    if (cpfSalvo && campoCpf && lembrarCheck) {
        campoCpf.value = cpfSalvo;
        lembrarCheck.checked = true;
    }
});

function login(event) {
    event.preventDefault();
    const form = document.getElementById("caixa-formulario");
    const dadosUsuario = Object.fromEntries(new FormData(form));
    const lembrar = document.getElementById("lembrar")?.checked;
    const erroDiv = document.getElementById("erro");

    dadosUsuario.senha = CryptoJS.SHA256(dadosUsuario.senha).toString();

    fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
    })
        .then(async response => {
            const data = await response.json();

            if (response.ok) {
                localStorage.setItem("usuario", JSON.stringify(data));

                if (lembrar) {
                    localStorage.setItem("cpf", dadosUsuario.cpf)
                } else { 
                    localStorage.removeItem("cpf");
                }
                window.location.href = "/"; 
            } else {
                document.getElementById("erro").innerText = data.error || "Erro desconhecido.";
                console.log("Mensagem do servidor:", data.error);
            }
        })
        .catch(err => {
            console.error("Erro de rede:", err);
            document.getElementById("erro").innerText = "Falha na conexão com o servidor.";
        });
}

function alteraSenha() {
    window.location.href = "/login"
//     const form = document.getElementById("caixa-formulario");
//     const dadosUsuario = Object.fromEntries(new FormData(form));
//     console.log(dadosUsuario);

//     fetch("/altera-senha", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(dadosUsuario)
//     })
//         .then(response => {
//             if (response.ok) {
//                 window.location.href = "/login";
//             } else {
//                 throw new Error('Erro na requisição: ' + response.status);
//             }
//         })
//         .catch(err => {
//             console.error(err);
//         });
}

function verificaEmail(event) {
     window.location.href = "/altera-senha"
    // event.preventDefault();
    // const form = document.getElementById("caixa-formulario");
    // const dadosUsuario = Object.fromEntries(new FormData(form));

    // fetch("/verifica-email", {
    //     method: "POST",
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify(dadosUsuario)
    // })
    //     .then(response => {
    //         if (response.ok) {
    //             window.location.href = "{/altera-cadastro";
    //         } else {
    //             throw new Error('Erro na requisição: ' + response.status);
    //         }
    //     })
    //     .catch(err => {
    //         console.error(err);
    //         document.getElementById("erro").innerText = err.message;
    //     });
}


// function alteraCadastro() {
//     window.location.href = "/home"
//     const form = document.getElementById("caixa-formulario");
//     const dadosUsuario = Object.fromEntries(new FormData(form));
//     console.log(dadosUsuario);

//     fetch("/altera-cadastro", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(dadosUsuario)
//     })
//         .then(response => {
//             if (response.ok) {
//                 window.location.href = "/}";
//             } else {
//                 throw new Error('Erro na requisição: ' + response.status);
//             }
//         })
//         .catch(err => {
//             console.error(err);
//         });
// }

function alteraCadastro() {
    const form = document.getElementById("caixa-formulario");
    const senha = document.getElementById("senha").value.trim();
    const confirmaSenha = document.getElementById("confirmaSenha").value.trim();

    // Verifica se os campos estão preenchidos
    if (!senha || !confirmaSenha) {
        alert("Por favor, preencha todos os campos!");
        return; // Para a execução
    }

    // Verifica se as senhas são iguais
    if (senha !== confirmaSenha) {
        alert("As senhas não coincidem!");
        return; // Para a execução
    }

    // Se chegou aqui, os campos estão corretos -> muda de página
    window.location.href = "/home";
}

const form  = document.getElementById("caixa-formulario");
if (form) {
    form.addEventListener("submit", login)
}