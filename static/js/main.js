// Toggle tema gelap/terang (disimpan di localStorage agar tidak reset saat pindah halaman)
(function () {
    const btn = document.getElementById("btnTema");
    function terapkan(terang) {
        document.body.classList.toggle("light", terang);
        btn.textContent = "tema: " + (terang ? "terang" : "gelap");
    }
    let terang = false;
    try { terang = localStorage.getItem("tema") === "terang"; } catch (e) {}
    terapkan(terang);

    btn.addEventListener("click", function () {
        const baru = !document.body.classList.contains("light");
        terapkan(baru);
        try { localStorage.setItem("tema", baru ? "terang" : "gelap"); } catch (e) {}
    });
})();
