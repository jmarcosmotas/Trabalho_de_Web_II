const selectCidade = document.getElementById("cidade");
const selectHospital = document.getElementById("hospital");
const selectEspecialista = document.getElementById("especialidade");
const clicaBotao = document.getElementById("botao");

fetch("http://127.0.0.1:5000/api/informacoes?informacoes=cidade")
    .then(response => response.json())
    .then(data => {
        data.cidade.forEach((nome, index) => {
            console.log(data);
            const option = document.createElement("option");
            option.value = data.id[index];
            option.textContent = nome;
            selectCidade.appendChild(option);
        });
    })
    .catch(err => console.error(err));

selectCidade.addEventListener("change", () => {
    const cidadeId = selectCidade.value;

    fetch(`http://127.0.0.1:5000/api/informacoes?informacoes=hospital&cidade_id=${cidadeId}`)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            selectHospital.innerHTML = '<option value="">Escolha o hospital</option>';
            data.hospital.forEach((nome, index) => {
                const option = document.createElement("option");
                option.value = data.id[index];
                option.textContent = nome;
                selectHospital.appendChild(option);
            });
        })

        .catch(err => console.error(err));
});

selectHospital.addEventListener("change", () => {
    const hospitalId = selectHospital.value;

    fetch(`http://127.0.0.1:5000/api/informacoes?informacoes=especialidade&hospital_id=${hospitalId}`)
        .then(res => res.json())
        .then(data => {
            selectEspecialista.innerHTML = '<option value="">Escolha a especialidade</option>';
            console.log(data);
            data.especialidade.forEach((item, index) => {
                const option = document.createElement("option");
                option.value = data.id[index];
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
   
    const agendamento = JSON.parse(sessionStorage.getItem("agendamento"));
    alert(`Agendamento armazenado:\nCidade: ${agendamento.cidade}\nHospital: ${agendamento.hospital}\nEspecialista: ${agendamento.especialista}`);

    window.location.href = "/marca-consulta";
});
