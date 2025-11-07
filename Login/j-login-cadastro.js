document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("caixa-formulario");

    if (window.location.pathname.includes("login.html")) {
        const cpfInput = document.getElementById("cpf");
        const senhaInput = document.getElementById("senha");
        const lembrarChk = document.getElementById("lembrar");

        const cpfSalvo = localStorage.getItem("cpfUsuario");
        if (cpfSalvo) {
            cpfInput.value = cpfSalvo;
            lembrarChk.checked = true;
        }

        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const cpf = cpfInput.value.trim();
            const senha = senhaInput.value;

            const pacientes = JSON.parse(localStorage.getItem("pacientes")) || [];
            const paciente = pacientes.find(
                (p) => p.cpf === cpf && p.senha === senha
            );

            if (paciente) {
                alert("Login bem-sucedido!");

                if (lembrarChk.checked) {
                    localStorage.setItem("cpfUsuario", cpf);
                } else {
                    localStorage.removeItem("cpfUsuario");
                }

                localStorage.setItem("pacienteLogado", JSON.stringify(paciente));
                window.location.href = "../inicio/h-index.html"; 
            } else {
                alert("CPF ou senha inválidos. Verifique e tente novamente!");
            }
        });
    }

    else if (window.location.pathname.includes("h-cadastro.html")) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const nome = document.getElementById("nome").value.trim();
            const cpf = document.getElementById("cpf").value.trim();
            const email = document.getElementById("email").value.trim();
            const telefone = document.getElementById("telefone").value.trim();
            const dataNascimento = document.getElementById("dataNascimento").value.trim();
            const endereco = document.getElementById("endereco").value.trim();
            const senha = document.getElementById("senha").value.trim();
            const confirmaSenha = document.getElementById("confirmaSenha").value.trim();

            if (senha !== confirmaSenha) {
                alert("É necessário que as senhas coincidam, tente novamente!");
                return;
            }

            const pacientes = JSON.parse(localStorage.getItem("pacientes")) || [];

            const pacientes_presentes = pacientes.some((p) => p.cpf === cpf);
            if (pacientes_presentes) {
                alert("Já existe um cadastro com esse CPF!");
                return;
            }
            const novoPaciente = {
                nome,
                cpf,
                email,
                telefone,
                dataNascimento,
                endereco,
                senha,
            };

            pacientes.push(novoPaciente);
            localStorage.setItem("pacientes", JSON.stringify(pacientes));

            alert("Cadastro realizado com sucesso!");
            window.location.href = "h-login.html";
        });
    }
});
