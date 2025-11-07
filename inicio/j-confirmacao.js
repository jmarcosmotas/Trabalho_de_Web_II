const botaoConfirmar = document.getElementById('botao-confirmar');
const modal = document.getElementById('modal');
const modalOk = document.getElementById('modal-ok');
const modalTitulo = document.getElementById('modal-titulo');
const modalMensagem = document.getElementById('modal-mensagem');


const params = new URLSearchParams(window.location.search);
const origem = params.get('origem');

if (origem === 'modificaPagina') {
  document.getElementById("mudaTexto").textContent = "Consulta Agendada";
  const botao = document.getElementById('botao-confirmar');
  if (botao) botao.remove();
} else {
  const usuario = JSON.parse(localStorage.getItem("usuario"));
  const infoConsulta = JSON.parse(localStorage.getItem("infoConsulta"));
  const agendamento = JSON.parse(sessionStorage.getItem("agendamento"));
  if (usuario) {
    document.getElementById("nome-pessoa").value = usuario.nome;
    document.getElementById("cpf").value = usuario.cpf;
    document.getElementById("data-nascimento").value = usuario.data;
    document.getElementById("telefone").value = usuario.telefone;
  }

  if (infoConsulta) {
    document.getElementById("nome-medico").value = infoConsulta.medico;
    document.getElementById("crm").value = infoConsulta.crm;
    document.getElementById("horario").value = infoConsulta.horario;
    document.getElementById("data").value = infoConsulta.data
    document.getElementById("endereco").value = infoConsulta.endereco
  }

  if (agendamento) {
    document.getElementById("hospital").value = agendamento.hospital;
    document.getElementById("cidade").value = agendamento.cidade;
    document.getElementById("especialista").value = agendamento.especialista;
  }
  botaoConfirmar.addEventListener('click', function () {
    const dadosUsuario = {
      hospital: agendamento.hospital,
      cidade: agendamento.cidade,
      especialidade: agendamento.especialista,
      cpf: usuario.cpf,
      crm: infoConsulta.crm,
      horario: infoConsulta.horario,
      data: infoConsulta.data,
      endereco: infoConsulta.endereco
    };

    fetch("../autent.json", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dadosUsuario)
    })
      .then(response => {
        if (!response.ok) throw new Error("Erro na requisição");
        modalTitulo.innerHTML = "Sucesso!";
        modalMensagem.innerHTML = "Consulta confirmada com sucesso!";
        modal.style.display = 'flex';
      })
      .catch(err => {
        console.error(err);
        modalTitulo.innerHTML = "Erro!";
        modalMensagem.innerHTML = "Não foi possível confirmar a consulta.";
        modal.style.display = 'flex';
      });
  });

  modalOk.addEventListener('click', function () {
    modal.style.display = 'none';
    window.location.href = "h-index.html";
  });
}














// document.addEventListener("DOMContentLoaded", function () {
//     const params = new URLSearchParams(window.location.search);
//     const origem = params.get("origem");

//     if (origem === "modificaPagina") {
//         document.getElementById("mudaTexto").textContent = "Consulta Agendada";

//         const botao = document.getElementById("botao-confirmar");
//         if (botao) botao.remove();
//     }

//     const pacienteLogado = JSON.parse(localStorage.getItem("pacienteLogado"));

//     if (pacienteLogado) {
//         const nome = document.getElementById("nome");
//         const cpf = document.getElementById("cpf");
//         const dataNascimento = document.getElementById("dataNascimento");
//         const telefone = document.getElementById("telefone");

//         if (nome) nome.value = pacienteLogado.nome || "";
//         if (cpf) cpf.value = pacienteLogado.cpf || "";
//         if (dataNascimento) dataNascimento.value = pacienteLogado.dataNascimento || "";
//         if (telefone) telefone.value = pacienteLogado.telefone || "";
//     } else {
//         console.warn("Nenhum paciente logado encontrado no localStorage.");
//     }

//     const botaoConfirmar = document.getElementById("botao-confirmar");
//     const modal = document.getElementById("modal");
//     const modalOk = document.getElementById("modal-ok");

//     if (botaoConfirmar && modal) {
//         botaoConfirmar.addEventListener("click", function () {
//             modal.style.display = "flex";
//         });
//     }

//     if (modalOk && modal) {
//         modalOk.addEventListener("click", function () {
//             modal.style.display = "none";
//             window.location.href = "index.html";
//         });
//     }
// });
