!(function () {
  "use strict";
  !(function () {
    if (
      "requestAnimationFrame" in window &&
      !/Mobile|Android/.test(navigator.userAgent)
    ) {
      var e = document.querySelectorAll("[data-bss-parallax]");
      if (e.length) {
        var t,
          n = [];
        window.addEventListener("scroll", a),
          window.addEventListener("resize", a),
          a();
      }
    }
    function a() {
      n.length = 0;
      for (var a = 0; a < e.length; a++) {
        var i = e[a].getBoundingClientRect(),
          o =
            parseFloat(e[a].getAttribute("data-bss-parallax-speed"), 10) || 0.5;
        i.bottom > 0 &&
          i.top < window.innerHeight &&
          n.push({ speed: o, node: e[a] });
      }
      cancelAnimationFrame(t), n.length && (t = requestAnimationFrame(r));
    }
    function r() {
      for (var e = 0; e < n.length; e++) {
        var t = n[e].node,
          a = n[e].speed;
        t.style.transform = "translate3d(0, " + -window.scrollY * a + "px, 0)";
      }
    }
  })();
})();
