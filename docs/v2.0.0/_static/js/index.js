(function () {
  document.addEventListener("DOMContentLoaded", function () {
    $("a.reference.external").each(function () {
      $(this).attr("target", "_blank")
    })
    document.querySelectorAll("a.reference.internal.image-reference").forEach(el => el.setAttribute("data-fancybox", 'gallery'))
    Fancybox.bind('[data-fancybox="gallery"]', {
      Thumbs: {
        showOnStart: false,
      },
      Images: {
        Panzoom: {
          maxScale: 1.5,
          click: "iterateZoom"
        },
      },
      Toolbar: {
        display: {
          left: ["infobar"],
          middle: [],
          right: ["iterateZoom", "slideshow", "download", "thumbs", "close"]
        }
      },
      contentClick: "iterateZoom"
    })
  })
})()