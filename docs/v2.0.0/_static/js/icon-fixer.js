(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var element = $(".wy-side-nav-search")
    var version = element.find(".version")

    if (version) {
      var icon = element.find(".icon.icon-home")

      $("<small>")
        .text(version.text())
        .appendTo(icon)

      element = $("nav.wy-nav-top")

      element.find("a")
        .last()
        .remove()

      element.append(icon.clone())
    }

    version.remove()
  })
})()