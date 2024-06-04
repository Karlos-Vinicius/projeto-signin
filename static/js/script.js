function equalsPasswords() {
    let password = document.getElementById("ipassword").value;
    let cpassword = document.getElementById("icpassword").value;

    let submit = document.getElementById("submit");

    if (password == cpassword) {
        submit.removeAttribute("disabled");
    } else {
        submit.setAttribute("disabled", "");
    }
}