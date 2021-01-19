/*
 {% if doc.image1 or doc.image2 %}
<input class="btn btn-secondary showbutton hive-doc-buttons" type="button" id="button{{doc.pk}}"
    onclick="show_images('image{{doc.pk}}', 'button{{doc.pk}}', 'buttonhide{{doc.pk}}')"
    value="Images"></input>
<input class="btn btn-secondary hidebutton hive-doc-buttons" type="button"
    id="buttonhide{{doc.pk}}"
    onclick="hide_images('image{{doc.pk}}', 'button{{doc.pk}}', 'buttonhide{{doc.pk}}')"
    value="Hide"></input>
{% endif %} 
*/

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

/*
<div class="hide-images" id="image{{doc.pk}}">
{% if doc.image1 %}
<a href="{{ doc.image1.url }}" target="_blank">
    <img class="imageondoc" src="{{ doc.image1.url }}"
        alt="Oops lost Image1! {{ doc.image1.name }}">
</a>
{% endif %}
{% if doc.image2 %}
<a href="{{ doc.image2.url }}" target="_blank">
    <img class="imageondoc" src="{{ doc.image2.url }}"
        alt="Oops lost Image2!  {{ doc.image2.name }}">
</a>
{% endif %}
</div></a>
*/