document.addEventListener("DOMContentLoaded", () => {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    const linksDiv = document.getElementById("links-login");
    const oculto = document.getElementById("oculto");
    const botaoSair = document.getElementById("botao-sair");

    const popUp = document.getElementById('pop-up');
    const popUpOk = document.getElementById('pop-up-ok');
    const popUpTitulo = document.getElementById('pop-up-titulo');
    const popUpMensagem = document.getElementById('pop-up-mensagem');


    if (usuario && usuario.nome) {
        const primeiroNome = usuario.nome.split(" ")[0];
        linksDiv.style.display = "none";
        botaoSair.style.display = "inline-block";
        oculto.innerHTML = `Olá <strong>${primeiroNome}</strong>,<br> seja bem-vindo`;
    } else {
        linksDiv.style.display = "flex";
        botaoSair.style.display = "none";
        oculto.innerHTML = "";
    }

    window.realizarLogout = function () {
        localStorage.removeItem("usuario");
        sessionStorage.removeItem("agendamento");
        localStorage.removeItem("infoConsulta");
        popUpTitulo.innerHTML = "Sessão Encerrada!";
        popUpMensagem.innerHTML = "Você foi deslogado com sucesso.";
        popUp.style.display = "flex";
    }

    if (popUpOk) {
        popUpOk.addEventListener("click", () => {
            popUp.style.display = "none";
            window.location.href = "/";
        });
    }
});
