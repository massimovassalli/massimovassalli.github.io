/**
 * n4m-nav.js — shared header and footer for the N4M static pages.
 *
 * Usage: set window.N4M_PAGE to one of 'home', 'about', 'venue', 'contacts'
 * BEFORE loading this script, then place <div id="n4m-header"> and
 * <div id="n4m-footer"> as placeholders in the page.
 *
 * To update the current-edition button or add a new edition to the dropdown,
 * edit only this file.
 */
(function () {
  var p = window.N4M_PAGE || '';

  function cls(page) {
    return 'nav-link px-2 ' + (p === page ? 'text-secondary' : 'text-white');
  }

  var headerHTML =
    '<header class="p-3 bg-dark text-white">' +
    '<div class="container">' +
    '<div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">' +
    '<a href="index.html" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">' +
    '<img src="img/n4m.svg" height="25"></a>' +
    '<ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">' +
    '<li><a href="index.html" class="' + cls('home') + '">Home</a></li>' +
    '<li><a href="about.html" class="' + cls('about') + '">About</a></li>' +
    '<li><a href="venue.html" class="' + cls('venue') + '">Venue</a></li>' +
    '<li><a href="contacts.html" class="' + cls('contacts') + '">Contact us</a></li>' +
    '<li><a href="2027/index.html" class="nav-link px-2 text-white btn btn-success">2027</a></li>' +
    '<li class="nav-item dropdown">' +
    '<a class="nav-link text-white dropdown-toggle" href="#" id="n4m-dropdown"' +
    ' data-bs-toggle="dropdown" aria-expanded="false">Editions</a>' +
    '<ul class="dropdown-menu" aria-labelledby="n4m-dropdown">' +
    '<li><a class="dropdown-item" href="2024/index.html" target="_blank">2024</a></li>' +
    '<li><a class="dropdown-item" href="2022.html" target="_blank">2022</a></li>' +
    '<li><a class="dropdown-item" href="2020/index.html" target="_blank">2020</a></li>' +
    '<li><a class="dropdown-item" href="2019/index.html" target="_blank">2019</a></li>' +
    '<li><a class="dropdown-item" href="2018/index.html" target="_blank">2018</a></li>' +
    '<li><a class="dropdown-item" href="2017/index.html" target="_blank">2017</a></li>' +
    '<li><a class="dropdown-item" href="2016/index.html" target="_blank">2016</a></li>' +
    '</ul></li>' +
    '</ul>' +
    '</div></div></header>';

  var footerHTML =
    '<footer class="footer mt-auto py-3 bg-light">' +
    '<div class="container">' +
    '<div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">' +
    '<div class="text-end w-100">' +
    '<a href="http://www.empa.ch" target="_blank" class="button"><img src="img/empa.png" height="40"></a>' +
    ' <a href="http://glasgow.thecemi.org" target="_blank" class="button"><img src="img/cemi-logo.svg" height="40"></a>' +
    '</div></div></div></footer>';

  var h = document.getElementById('n4m-header');
  if (h) h.outerHTML = headerHTML;

  var f = document.getElementById('n4m-footer');
  if (f) f.outerHTML = footerHTML;
}());
