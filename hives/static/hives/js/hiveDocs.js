function show_images(image_pk, button_pk, button2_pk) {
    let images = document.getElementById(image_pk);
    images.classList.add("show-images");
    let but = document.getElementById(button_pk);
    but.classList.remove("showbutton");
    but.classList.add("hidebutton");
    let but2 = document.getElementById(button2_pk);
    but2.classList.remove("hidebutton");
    but2.classList.add("showbutton");
}

function hide_images(image_id, button_pk, button2_pk) {
    let images = document.getElementById(image_id);
    images.classList.remove("show-images");
    images.classList.add("hide-images");
    let but = document.getElementById(button_pk);
    but.classList.remove("hidebutton");
    but.classList.add("showbutton");
    let but2 = document.getElementById(button2_pk);
    but2.classList.remove("showbutton");
    but2.classList.add("hidebutton");
}
