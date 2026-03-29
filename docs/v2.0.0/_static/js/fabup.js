(function () {
  document.addEventListener("DOMContentLoaded", function () {
    function checkFabUpPosition() {
      var fabUp = $("#fab-up")
      window.scrollY < window.innerHeight ? fabUp.hide() : fabUp.show()
    }

    $("<button>")
      .attr("id", "fab-up")
      .attr("class", "fab-up")
      .append(
        $("<i>")
          .attr("class", "fa fa-arrow-up")
      )
      .click(function () {
        window.scrollTo({
          top: 0,
          behavior: "smooth"
        })
      })
      .appendTo(document.body)

    $("i[data-toggle='wy-nav-top']")
      .first()
      .click(function () {
        $("#fab-up")
          .toggle()
        checkFabUpPosition()
      })

    checkFabUpPosition()
    document.addEventListener("scroll", checkFabUpPosition)
  })
})()