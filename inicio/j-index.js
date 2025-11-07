const selectCidade = document.getElementById("cidade");
const selectHospital = document.getElementById("hospital");
const selectEspecialista = document.getElementById("especialidade");

fetch("../cidades.json")
    .then(response => {
        if (!response.ok) {
            throw new Error("Erro ao carregar especialistas: " + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        const cidades = data.cidade;
        cidades.forEach(cidade => {
            const option = document.createElement("option");
            option.value = cidade;
            option.textContent = cidade;
            selectCidade.appendChild(option);
        });
    })
    .catch(err => console.error(err));

selectCidade.addEventListener("change", (event) => {
    const cidadeSelecionada = event.target.value;

    fetch("../hospitais.json")
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao carregar hospital: " + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Conteúdo do JSON recebido:", data);

            const hospitais = data.hospital;

            selectHospital.innerHTML = '<option value="">Escolha a especialidade</option>';

            hospitais.forEach(item => {
                const option = document.createElement("option");
                option.value = item;
                option.textContent = item;
                selectHospital.appendChild(option);
            });
        })
        .catch(err => console.error(err));
});

selectHospital.addEventListener("change", (event) => {
    fetch("../especialista.json")
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao carregar hospital: " + response.statusText);
            }
            return response.json();
        })
        .then(data => {

            const especialistas = data.especialista;
            console.log(especialistas)

            selectEspecialista.innerHTML = '<option value="">Escolha a especialidade</option>';
            especialistas.forEach(item => {
                const option = document.createElement("option");
                option.value = item;
                option.textContent = item;
                selectEspecialista.appendChild(option);
            });
        })
        .catch(err => console.error(err));
});

selectEspecialista.addEventListener("change", (event) => {
    const clicaBotao = document.getElementById("botao");
    clicaBotao.addEventListener("click", (event) => {
        event.preventDefault();

        const cidade = selectCidade.value;
        const hospital = selectHospital.value;
        const especialista = selectEspecialista.value;

        sessionStorage.setItem("agendamento", JSON.stringify({ cidade, hospital, especialista }));
        console.log("Agendamento salvo:", { cidade, hospital, especialista });
        window.location.href = "h-marcar_consulta.html";
    });
});
