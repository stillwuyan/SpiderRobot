(() => {
  function list_movies(movies) {
    let list = document.getElementById('movie_list')
    for (var i = 0; i < movies.length; i++) {
      let item = document.createElement('li')
      let link = document.createElement('a')
      link.setAttribute('href', 'javascript:void(0)')
      link.addEventListener('click', query_subtitle)
      link.innerText = movies[i]
      item.appendChild(link)
      list.appendChild(item)
    }
  }

  function query_subtitle(event) {
    let request = new XMLHttpRequest()
    request.onload = () => {
      // request.readyState will be 4
      if (request.status == 200) {
        document.innerText = 'Hello world'
        alert(event)
      }
    }
    let name = event.target.innerText
    request.open('GET', `/query?movie=${name}`, true)
    request.send()
    return false
  }

  window.onload = () => {
    // TODO: use fetch to replace ajax
    let request = new XMLHttpRequest()
    request.onload = () => {
      // this.readyState will be 4
      if (request.status == 200) {
        list_movies(JSON.parse(request.responseText))
      }
    }
    request.open('GET', '/movies', true)
    request.send()
  }
})()