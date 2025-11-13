const botaoConfirmar = document.getElementById('botao-confirmar');
const popUp = document.getElementById('pop-up');
const popUpOk = document.getElementById('pop-up-ok');
const popUpTitulo = document.getElementById('pop-up-titulo');
const popUpMensagem = document.getElementById('pop-up-mensagem');

const nome = document.getElementById("nome-pessoa");
const cpf = document.getElementById("cpf");
const dataNascimento = document.getElementById("data-nascimento");
const telefone = document.getElementById("telefone");

const medico = document.getElementById("nome-medico");
const crm = document.getElementById("crm");
const horario = document.getElementById("horario");
const dataConsulta = document.getElementById("data");
const endereco = document.getElementById("endereco");

const hospital = document.getElementById("hospital");
const cidade = document.getElementById("cidade");
const especialidade = document.getElementById("especialista");

const usuario = JSON.parse(localStorage.getItem("usuario") || '{}');
const infoConsulta = JSON.parse(localStorage.getItem("infoConsulta") || '{}');
const agendamento = JSON.parse(sessionStorage.getItem("agendamento") || '{}');

const params = new URLSearchParams(window.location.search);
const origem = params.get('origem');

function preencherCampos() {
  nome.value = usuario?.nome || '';
  cpf.value = usuario?.cpf || '';
  dataNascimento.value = usuario?.data || '';
  telefone.value = usuario?.telefone || '';

  medico.value = infoConsulta?.medico || '';
  crm.value = infoConsulta?.crm || '';
  horario.value = infoConsulta?.horario || '';
  dataConsulta.value = infoConsulta?.data || '';
  endereco.value = infoConsulta?.endereco || '';

  hospital.value = agendamento?.hospital || '';
  cidade.value = agendamento?.cidade || '';
  especialidade.value = agendamento?.especialista || '';
}

  preencherCampos();

  if (botaoConfirmar) {
    botaoConfirmar.addEventListener('click', function () {
      if (!usuario || !infoConsulta || !agendamento) return;

      const dadosUsuario = {
        hospital: agendamento.hospital,
        cidade: agendamento.cidade,
        especialidade: agendamento.especialista,
        cpf: usuario.cpf,
        crm: infoConsulta.crm,
        medico: infoConsulta.medico,
        horario: infoConsulta.horario,
        data: infoConsulta.data,
        endereco: infoConsulta.endereco
      };

      fetch("http://127.0.0.1:5000/api/confirma-consulta", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosUsuario)
      })
        .then(response => response.json().then(data => ({ ok: response.ok, data })))
        .then(({ ok, data }) => {
          popUpTitulo.innerHTML = ok ? "Sucesso!" : "Erro!";
          popUpMensagem.innerHTML = ok ? "Consulta confirmada com sucesso!" : (data.error || "Não foi possível confirmar a consulta.");
          popUp.style.display = 'flex';
        })
        .catch(err => {
          console.error("Erro de rede:", err);
          popUpTitulo.innerHTML = "Erro!";
          popUpMensagem.innerHTML = "Falha na comunicação com o servidor.";
          popUp.style.display = 'flex';
        });
    });
  }

  if (popUpOk) {
    popUpOk.addEventListener('click', function () {
      popUp.style.display = 'none';
      window.location.href = "/";
    });
  }

