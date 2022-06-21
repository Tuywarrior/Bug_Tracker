let addButton = document.querySelector('.add-button');
addButton.addEventListener('mouseenter', addLook);
addButton.addEventListener('mouseleave', removeLook)

function addLook(e) {
    e.target.textContent = "Raise a Bug";
    console.log(e.target.style.height);
}

function removeLook(e) {
    e.target.textContent = "+";
}
