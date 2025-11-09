const botaoConfirmar = document.getElementById('botao-confirmar');
const popUp = document.getElementById('pop-up');
const popUpOk = document.getElementById('pop-up-ok');
const popUpTitulo = document.getElementById('pop-up-titulo');
const popUpMensagem = document.getElementById('pop-up-mensagem');


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

        popUpTitulo.innerHTML = "Sucesso!";
        popUpMensagem.innerHTML = "Consulta confirmada com sucesso!";
        popUp.style.display = 'flex';
      })
      .catch(err => {
        console.error(err);
        popUpTitulo.innerHTML = "Erro!";
        popUpMensagem.innerHTML = "Não foi possível confirmar a consulta.";
        popUp.style.display = 'flex';
      });
  });

  popUpOk.addEventListener('click', function () {
    popUp.style.display = 'none';
    window.location.href = "h-index.html";
  });
}








