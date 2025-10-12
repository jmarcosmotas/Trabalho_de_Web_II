const params = new URLSearchParams(window.location.search);
const origem = params.get('origem');

if (origem === 'modificaPagina') {
    document.getElementById("mudaTexto").textContent = "Consulta Agendada";

    const botao = document.getElementById('botao-confirmar');
    if (botao) botao.remove();
}

const botaoConfirmar = document.getElementById('botao-confirmar');
const modal = document.getElementById('modal');
const modalOk = document.getElementById('modal-ok');

botaoConfirmar.addEventListener('click', function () {
    modal.style.display = 'flex';
});

modalOk.addEventListener('click', function () {
    modal.style.display = 'none';
    window.location.href = "index.html";
});