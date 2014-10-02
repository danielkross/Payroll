function show() {
    document.addEventListener('DOMContentLoaded', function() {
            if ("{{ opt }}" == 'customers') {
                customersOpt.style.display = 'block';
            }
            if ("{{ opt }}" == 'suppliers') {
                suppliersOpt.style.display = 'block';
            }
        }, false);
}

function showForm(elementName) {
    var element = document.getElementById(elementName);
    if (element.style.display == 'none') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
    }
}