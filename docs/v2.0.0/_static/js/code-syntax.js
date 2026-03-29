(function () {
  document.addEventListener("DOMContentLoaded", function () {
    function addColor(target, color) {
      $(target).css({
        color: color
      })
    }

    $("em.sig-param .default_value .pre").each(function () {
      var color = "var(--code-keyword)";
      try {
        switch (typeof eval(this.innerText)) {
          case "string":
            color = "var(--code-string)";
            break;
          case "number":
            color = "var(--code-number)";
            break;

        }
      } catch (e) {
      }

      addColor(this, color)
    })

    $("em.sig-param").each(function () {
      $(this).find(".n > .pre").each(function (index) {
        var color = "var(--code-class)";
        if (index === 0)
          color = "var(--code-params)"

        addColor(this, color)
      })

    })

    $("dt.sig.py").addClass("notranslate")
  })
})()