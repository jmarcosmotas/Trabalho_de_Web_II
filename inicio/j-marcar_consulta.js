const nomeMedico = document.getElementById("nome-medico")
const espMedico = document.getElementById("esp-medico")
const crmMedico = document.getElementById("crm-medico")
const textoMedico = document.getElementById("texto-medico")
const endMedico = document.getElementById("end-Medico")

const ths = document.querySelectorAll("thead th");
const mesAno = document.getElementById("mes-ano");

function requisicao() {
    fetch("../medico.json")
        .then(response => response.json())
        .then(data => {
            nomeMedico.innerHTML = `DR. ${data.medico}`;
            espMedico.innerHTML = `<strong>Especialidade: </strong>`;
            crmMedico.innerHTML = `CRM: ${data.CRM}`;
            textoMedico.innerHTML = `${data.texto}`;
            endMedico.innerHTML = `<strong>Endereço da Consulta:</strong> ${data.endereco}`;

            const horariosPorDia = [
                ["Dom", ...(data.dom || [])],
                ["Seg", ...(data.seg || [])],
                ["Ter", ...(data.ter || [])],
                ["Qua", ...(data.qua || [])],
                ["Qui", ...(data.qui || [])],
                ["Sex", ...(data.sex || [])],
                ["Sáb", ...(data.sab || [])]
            ];

            preencherTabela(horariosPorDia, data.medico, data.CRM, data.endereco);
        })
        .catch(err => console.error(err));
}

function preencherTabela(horariosPorDia, nomeMed, crmMed, endMed) {
    const ths = document.querySelectorAll("thead th");
    const mesAno = document.getElementById("mes-ano");

    const agora = new Date();
    let dataAtual = new Date();

    const mesAtual = dataAtual.toLocaleString("pt-BR", { month: "long" });
    const anoAtual = dataAtual.getFullYear();
    mesAno.textContent = `${mesAtual[0].toUpperCase() + mesAtual.slice(1)} ${anoAtual}`;

    ths.forEach(th => {
        const div = th.querySelector("div");
        div.innerHTML = "";

        const diaSemana = dataAtual.getDay();
        const [nomeDia, ...horarios] = horariosPorDia[diaSemana];

        div.innerHTML = `<span class="dia">${nomeDia}, ${dataAtual.getDate()}/${dataAtual.getMonth() + 1}</span>`;

        const horariosDiv = document.createElement("div");
        horariosDiv.classList.add("horarios");

        if (horarios.length === 0) {
            const msg = document.createElement("p");
            msg.textContent = "-";
            msg.style.cssText = "color:#999;font-style:italic";
            horariosDiv.appendChild(msg);
        } else {
            horarios.forEach(hora => {
                const [h, m] = hora.split(":").map(Number);
                const dataHora = new Date(dataAtual.getFullYear(), dataAtual.getMonth(), dataAtual.getDate(), h, m);

                const botao = document.createElement("button");
                botao.textContent = hora;

                if (dataHora < agora) {
                    botao.disabled = true;
                    botao.classList.add("passado");
                } else {
                    botao.dataset.dia = dataAtual.getDate();
                    botao.dataset.mes = dataAtual.getMonth() + 1;
                    botao.dataset.ano = anoAtual;
                    botao.dataset.horario = hora;

                    botao.addEventListener("click", (e) => {
                        const usuario = localStorage.getItem("usuario");
                        if (usuario) {
                            const diaSelecionado = e.target.dataset.dia;
                            const mesSelecionado = e.target.dataset.mes;
                            const anoSelecionado = e.target.dataset.ano;
                            const horarioSelecionado = e.target.dataset.horario;
                            const infoConsulta = {
                                medico: nomeMed,
                                crm: crmMed,
                                endereco: endMed,
                                data: diaSelecionado + "/" + mesSelecionado + "/" + anoSelecionado,
                                horario: horarioSelecionado
                            };
                            alert(JSON.stringify(infoConsulta));
                            localStorage.setItem("infoConsulta", JSON.stringify(infoConsulta));
                            window.location.href = "h-confirmacao.html";
                        }else{
                            window.location.href = "h-login.html";
                        }

                    });
                }

                horariosDiv.appendChild(botao);
            });
        }

        div.appendChild(horariosDiv);
        dataAtual.setDate(dataAtual.getDate() + 1);
    });
}



requisicao();
