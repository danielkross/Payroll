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

function yo() {
    alert("siemanko");
}