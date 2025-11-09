document.addEventListener("DOMContentLoaded", () => {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    const linksDiv = document.getElementById("links-login");
    const oculto = document.getElementById("oculto");
    const botaoSair = document.getElementById("botao-sair");

    const popUp = document.getElementById('pop-up');
    const popUpOk = document.getElementById('pop-up-ok');
    const popUpTitulo = document.getElementById('pop-up-titulo');
    const popUpMensagem = document.getElementById('pop-up-mensagem');

    // Mostra ou esconde elementos dependendo se o usuário está logado
    if (usuario && usuario.nome) {
        const primeiroNome = usuario.nome.split(" ")[0];
        linksDiv.style.display = "none";          // Esconde login/cadastro
        botaoSair.style.display = "inline-block"; // Mostra botão Sair
        oculto.innerHTML = `Olá <strong>${primeiroNome}</strong>,<br> seja bem-vindo`;
    } else {
        linksDiv.style.display = "flex";  // Mostra login/cadastro
        botaoSair.style.display = "none"; // Esconde botão Sair
        oculto.innerHTML = "";
    }

    // Função de logout, chamada apenas ao clicar no botão
    window.realizarLogout = function() {
        localStorage.removeItem("usuario");
        popUpTitulo.innerHTML = "Sessão Encerrada!";
        popUpMensagem.innerHTML = "Você foi deslogado com sucesso.";
        popUp.style.display = "flex";
    }

    // Fechar pop-up e redirecionar para login
    if (popUpOk) {
        popUpOk.addEventListener("click", () => {
            popUp.style.display = "none";
            window.location.href = "../Login/h-login.html";
        });
    }
});
