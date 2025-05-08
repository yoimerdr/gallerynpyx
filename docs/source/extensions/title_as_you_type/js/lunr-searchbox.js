/*jslint browser: true*/
/*global $, lunr, Search, DOCUMENTATION_OPTIONS*/

(function () {
  "use strict";

  $.fn.textWidth = function (text, font) {
    if (!$.fn.textWidth.fakeEl) $.fn.textWidth.fakeEl = $('<span>').hide().appendTo(document.body);
    $.fn.textWidth.fakeEl.text(text || this.val() || this.text()).css('font', font || this.css('font'));
    return $.fn.textWidth.fakeEl.width();
  };

  var searchModule = (function ($, lunr, DOCUMENTATION_OPTIONS) {
    "use strict";

    var store = LunrDataSearch.data,
      index = null;

    var relativeUrl = LunrDataSearch.relativeUrl;
    var maxResults = LunrDataSearch.maxResults || 7;
    var withWildcard = LunrDataSearch.withWildcard;


    lunr.tokenizer.seperator = lunr.tokenizer.separator = new RegExp(LunrDataSearch.tokenizerSeparator, 'g');

    index = lunr(function () {
      this.ref('id');
      this.field('title');
      this.metadataWhitelist = []
      store.forEach(function (item, index) {
        this.add({
          id: index,
          title: item.title,
        })
      }, this)
    });

    var searchResults = $('#ls_search-results'), searchField = $('#ls_search-field'),
      resetButton = $("#search-reset-button");

    resetButton.click(function () {
      searchResults.empty();
      resetButton.hide();
    })

    function hideResults() {
      window.setTimeout(function () {
        searchResults.hide();
      }, 100);
    }

    function showResults() {
      if (searchResults.find('.search-result').length > 0)
        searchResults.show();
    }

    searchField.keyup(onKeyUp)
      .keydown(onNavigate)
      .focusout(hideResults)
      .focusin(showResults)

    function onKeyUp(event) {
      var keycode = event.keyCode || event.which,
        query = searchField.val(),
        i = 0,
        results = null;

      // ignore enter, down and up
      if (keycode === 13 || keycode === 40 || keycode === 38)
        return;

      // ignore empty query
      if (!query) {
        resetButton.hide();
        searchResults.empty()
          .hide();
        return;
      }

      if (withWildcard && query[query.length - 1] !== '*')
        query += "*";

      resetButton.show();

      results = index.search(query);
      searchResults.empty()
        .show();

      if (results.length === 0)
        return searchResults.append($('<li class="search-result"><a class="search-result-ref" href="#">No results found</a></li>'));

      for (i = 0; i < Math.min(results.length, maxResults); i += 1)
        searchResults.append(createResultElement(store[results[i].ref]));

      // set the width of the dropdown so that it contains all of the
      // list elements
      searchResults.width(Math.max(
        searchField.outerWidth(),
        Math.max.apply(null, searchResults.children().map(function (i, o) {
          return $(o).textWidth();
        })) + 20
      ));

    }  // end onKeyUp
    function selectFirstResult(source) {
      source.find('.search-result-ref')
        .first()
        .addClass('selected')
    }

    function selectLastResult(source) {
      source.find('.search-result-ref')
        .last()
        .addClass('selected')
    }

    function onNavigate(ev) {

      var keycode = ev.keyCode || ev.which;

      if (keycode !== 40 && keycode !== 38)
        return;

      var active = searchResults.find('.search-result-ref.selected')
        .first();

      // down key, next result
      if (keycode === 40) {
        // no element selected
        if (!active.length)
          return selectFirstResult(searchResults);

        var next = active.parent()
          .next();

        // next on last
        if (!next.length) {
          if (LunrDataSearch.navigationMode === "infinite") {
            active.removeClass('selected')
            selectFirstResult(searchResults)
          }

          return;
        }

        // next result
        active.removeClass('selected');
        return selectFirstResult(next);
      }

      // up key, prev result
      // no result selected
      if (!active.length)
        return selectLastResult(searchResults)

      var prev = active.parent()
        .prev();

      // prev on first
      if (!prev.length) {
        if (LunrDataSearch.navigationMode === "infinite") {
          active.removeClass('selected')
          selectLastResult(searchResults)
        }

        return;
      }

      // prev result
      active.removeClass('selected');
      selectFirstResult(prev);
    }  // end handleKeyboardNavigation

    function buildHref(match) {
      var baseUrl = relativeUrl || DOCUMENTATION_OPTIONS.URL_ROOT || ""
      return baseUrl + match.root + DOCUMENTATION_OPTIONS.FILE_SUFFIX + '#' + match.anchor;
    } // end buildHref

    function createResultElement(s) {
      return $('<li class="search-result">')
        .append($('<a class="search-result-ref">')
          .attr('href', buildHref(s))
          .attr('title', s.title)
          .text(s.label || s.title)
          .click(function () {
            searchField.val("")
            searchResults.empty()
          })
          .mouseenter(function () {
            searchResults.find('.search-result-ref')
              .removeClass('selected');
            $(this).addClass('selected');
          })
          .mouseleave(function () {
            $(this).removeClass('selected');
          })
        );
    } // end createResultElement
  });

  window.onload = function () {
    searchModule($, lunr, DOCUMENTATION_OPTIONS);
  };

}());
