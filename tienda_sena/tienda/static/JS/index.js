// Iniciar Sesion

const btn_iniciar_sesion=
document.querySelector("#btn_iniciar_sesion");

const btn_cerrar_modal=
document.querySelector("#cerrar_modal")

const modal=
document.querySelector("#modal")

btn_iniciar_sesion.addEventListener("click",(event)=>{
    event.preventDefault();
    modal.showModal();
})


// modal Registrarse

const btn_registrarse=
document.querySelector("#btn_registrarse");

const modal2=
document.querySelector("#modal2")


btn_registrarse.addEventListener("click",(event)=>{
    event.preventDefault();
    modal2.showModal();
});
