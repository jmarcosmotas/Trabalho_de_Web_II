
const cpf = document.getElementById("cpf");
        cpf.addEventListener("input", () => {
            let value = cpf.value.replace(/\D/g, "");
            value = value.replace(/(\d{3})(\d)/, "$1.$2");
            value = value.replace(/(\d{3})(\d)/, "$1.$2");
            value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
            cpf.value = value;
});