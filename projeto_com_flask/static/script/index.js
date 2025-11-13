const selectCidade = document.getElementById("cidade");
const selectHospital = document.getElementById("hospital");
const selectEspecialista = document.getElementById("especialidade");
const clicaBotao = document.getElementById("botao");

fetch("http://127.0.0.1:5000/api/informacoes?informacoes=cidade")
    .then(response => response.json())
    .then(data => {
        data.cidade.forEach(cidade => {
            const option = document.createElement("option");
            option.value = cidade;
            option.textContent = cidade;
            selectCidade.appendChild(option);
        });
    })
    .catch(err => console.error(err));

selectCidade.addEventListener("change", () => {
    fetch("http://127.0.0.1:5000/api/informacoes?informacoes=hospital")
        .then(res => res.json())
        .then(data => {
            selectHospital.innerHTML = '<option value="">Escolha o hospital</option>';
            data.hospital.forEach(hospital => {
                const option = document.createElement("option");
                option.value = hospital;
                option.textContent = hospital;
                selectHospital.appendChild(option);
            });
        })
        .catch(err => console.error(err));
});

selectHospital.addEventListener("change", () => {
    fetch("http://127.0.0.1:5000/api/informacoes?informacoes=especialidade")
        .then(res => res.json())
        .then(data => {
            selectEspecialista.innerHTML = '<option value="">Escolha a especialidade</option>';
            data.especialista.forEach(item => {
                const option = document.createElement("option");
                option.value = item;
                option.textContent = item;
                selectEspecialista.appendChild(option);
            });
        })
        .catch(err => console.error(err));
});

clicaBotao.addEventListener("click", (event) => {
    event.preventDefault();

    const cidade = selectCidade.value;
    const hospital = selectHospital.value;
    const especialista = selectEspecialista.value;

    if (!cidade || !hospital || !especialista) {
        alert("Selecione todos os campos antes de continuar!");
        return;
    }

    sessionStorage.setItem("agendamento", JSON.stringify({ cidade, hospital, especialista }));

    window.location.href = "/marca-consulta";
});
