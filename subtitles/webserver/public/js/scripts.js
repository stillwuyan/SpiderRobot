function list_movies(movies) {
  var list = document.getElementById("movie_list")
  for (var i = 0; i < movies.length; i++) {
    child = document.createElement("li")
    child.innerHTML = movies[i]
    list.appendChild(child)
  }
}

window.onload = function () {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      list_movies(JSON.parse(this.responseText))
    }
  }
  request.open("GET", "/movies", true)
  request.send()
}