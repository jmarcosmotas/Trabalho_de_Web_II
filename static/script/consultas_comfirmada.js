const botaoCancelar = document.getElementById("botao-cancelar");

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

const popUp = document.getElementById('pop-up');
const popUpOk = document.getElementById('pop-up-ok');
const popUpTitulo = document.getElementById('pop-up-titulo');
const popUpMensagem = document.getElementById('pop-up-mensagem');

const usuario = JSON.parse(localStorage.getItem("usuario") || '{}');
console.log(usuario)
function preencherCampos(data) {
    nome.value = usuario.nome || '';
    dataNascimento.value = usuario.data || '';
    telefone.value = usuario.telefone || '';
    cpf.value = data.cpf || '';
    crm.value = data.crm || '';
    horario.value = data.horario || '';
    dataConsulta.value = data.data || '';
    medico.value = data.medico || '';
    endereco.value = data.endereco || '';
    especialidade.value = data.especialidade || '';
    hospital.value = data.hospital || '';
    cidade.value = data.cidade || '';
}

function mostrarPopUp(titulo, mensagem) {
    popUpTitulo.textContent = titulo;
    popUpMensagem.textContent = mensagem;
    popUp.style.display = "flex";
}

if (!usuario || !usuario.nome) {
    window.location.href = "/login";
} else {
    fetch("http://127.0.0.1:5000/api/consultas-comfirmadas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cpf: usuario.cpf })
    })
        .then(res => res.json().then(data => ({ ok: res.ok, data })))
        .then(({ ok, data }) => {
            if (ok && data.status === "ok") {
                preencherCampos(data);
            } else {
                mostrarPopUp("Aviso!", data.error || "Nenhuma consulta encontrada.");
            }
        })
        .catch(err => {
            console.error("Erro ao buscar dados:", err);
            mostrarPopUp("Erro!", "Falha na comunicação com o servidor.");
        });

    let popUpCancelamentoAtivo = false; // flag para identificar o pop-up de cancelamento

    botaoCancelar.addEventListener("click", () => {
        popUpCancelamentoAtivo = true; // ativa a flag
        mostrarPopUp("Cancelar Consulta", "Tem certeza que deseja cancelar a consulta?");

        popUpOk.onclick = () => {
            popUp.style.display = "none";
            popUpCancelamentoAtivo = false; // desativa a flag

            fetch("http://127.0.0.1:5000/api/cancelar-consulta", {
                method: "DELETE",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ cpf: usuario.cpf })
            })
                .then(res => res.json())
                .then(data => {
                    if (data.status === "ok") {
                        window.location.href = "/";
                    } else {
                        mostrarPopUp("Aviso!", data.error || "Não foi possível cancelar a consulta.");
                    }
                })
                .catch(err => {
                    console.error("Erro ao cancelar consulta:", err);
                    mostrarPopUp("Erro!", "Falha na comunicação com o servidor.");
                });
        };
    });

    popUp.addEventListener("click", (e) => {
        if (e.target === popUp && popUpCancelamentoAtivo) {
            popUp.style.display = "none";
            popUpCancelamentoAtivo = false; 
        }
    });
}

if (popUpOk) {
    popUpOk.addEventListener("click", () => {
        popUp.style.display = "none";
        window.location.href = "/";
    });
}


