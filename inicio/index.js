const nomesDias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];

const horariosPorDia = [
    ["Domingo", "08:00", "09:00", "10:00", "11:00"],
    ["Segunda", "09:00", "10:00", "14:00"],
    ["Terça", "08:00", "09:00", "11:00", "15:00"],
    ["Quarta"],
    ["Quinta", "08:00", "14:00"],
    ["Sexta", "08:00", "09:00", "10:00"],
    ["Sábado"]
];

const ths = document.querySelectorAll("thead th");
const mesAno = document.getElementById("mes-ano");

let data = new Date();
const mesAtual = data.toLocaleString("pt-BR", { month: "long" });
const anoAtual = data.getFullYear();
mesAno.textContent = `${mesAtual.charAt(0).toUpperCase() + mesAtual.slice(1)} ${anoAtual}`;

const agora = new Date();

ths.forEach((th, index) => {
    const div = th.querySelector("div");
    div.innerHTML = "";

    const diaSemana = data.getDay();
    const dia = data.getDate();
    const mes = data.getMonth() + 1;

    let diaHorario = horariosPorDia[diaSemana];
    const nomeDia = diaHorario[0];
    const horarios = diaHorario.slice(1);

    const titulo = document.createElement("span");
    titulo.classList.add("dia");
    titulo.textContent = `${nomeDia}, ${dia}/${mes}`;
    div.appendChild(titulo);

    const horariosDiv = document.createElement("div");
    horariosDiv.classList.add("horarios");

    if (horarios.length === 0) {
        const msg = document.createElement("p");
        msg.textContent = "-";
        msg.style.color = "#999";
        msg.style.fontStyle = "italic";
        horariosDiv.appendChild(msg);
    } else {
        horarios.forEach(hora => {
            const [h, m] = hora.split(":").map(Number);
            const dataHora = new Date(data.getFullYear(), data.getMonth(), data.getDate(), h, m);

            const botao = document.createElement("button");
            botao.textContent = hora;

            if (dataHora < agora) {
                botao.disabled = true;
                botao.classList.add("passado");
            } else {
                botao.onclick = () => {
                    const dataSelecionada = `${dia}/${mes}/${anoAtual}`;
                    const url = `marcar.html?dia=${dataSelecionada}&horario=${hora}`;
                    window.location.href = url;
                };
            }
            horariosDiv.appendChild(botao);
        });
    }

    div.appendChild(horariosDiv);
    data.setDate(data.getDate() + 1);
});