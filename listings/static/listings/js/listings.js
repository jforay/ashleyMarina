document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("tr.clickable-row").forEach(function (row) {
        row.addEventListener("click", function () {
        const url = row.dataset.href;
        if (url) window.open(url, "_blank"); // or: window.location.href = url;
        });
    });
});
