document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search);
    const origem = params.get("origem");

    // ----- Verifica se veio da página de consultas marcadas -----
    if (origem === "modificaPagina") {
        document.getElementById("mudaTexto").textContent = "Consulta Agendada";

        const botao = document.getElementById("botao-confirmar");
        if (botao) botao.remove();
    }

    // ----- Recupera o paciente logado -----
    const pacienteLogado = JSON.parse(localStorage.getItem("pacienteLogado"));

    if (pacienteLogado) {
        // Preenche automaticamente os campos do paciente
        const nome = document.getElementById("nome");
        const cpf = document.getElementById("cpf");
        const dataNascimento = document.getElementById("dataNascimento");
        const telefone = document.getElementById("telefone");

        if (nome) nome.value = pacienteLogado.nome || "";
        if (cpf) cpf.value = pacienteLogado.cpf || "";
        if (dataNascimento) dataNascimento.value = pacienteLogado.dataNascimento || "";
        if (telefone) telefone.value = pacienteLogado.telefone || "";
    } else {
        console.warn("Nenhum paciente logado encontrado no localStorage.");
    }

    // ----- Lógica do modal -----
    const botaoConfirmar = document.getElementById("botao-confirmar");
    const modal = document.getElementById("modal");
    const modalOk = document.getElementById("modal-ok");

    // Exibe o modal ao confirmar
    if (botaoConfirmar && modal) {
        botaoConfirmar.addEventListener("click", function () {
            modal.style.display = "flex";
        });
    }

    // Fecha o modal e volta à página inicial
    if (modalOk && modal) {
        modalOk.addEventListener("click", function () {
            modal.style.display = "none";
            window.location.href = "index.html";
        });
    }
});
