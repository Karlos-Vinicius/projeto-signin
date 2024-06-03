function equalsPasswords() {
    let password = document.getElementById("ipassword").value;
    let cpassword = document.getElementById("icpassword").value;

    // Testes 
    console.log(password, cpassword);
    console.log(password == cpassword);

    let submit = document.getElementById("submit");

    if (!(password =! cpassword)) {
        submit.setAttribute("disabled", "");
    } else {
        submit.removeAttribute("disabled");
    }
}