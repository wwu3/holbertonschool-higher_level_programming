$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    console.log(data);
    $.each(data.results, function (index, element) {
      $('ul#list_movies').append(`<li>${element.title}</li>`);
    });
  });
});
