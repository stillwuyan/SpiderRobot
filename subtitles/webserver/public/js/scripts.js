(() => {
  function handle_response(responseText) {
    let response = JSON.parse(responseText)
    switch (response.type) {
    case 'folder':
      list_movies(response.data)
      break
    case 'file':
      document.getElementsByTagName('body')[0].innerHTML = responseText
      break
    case 'message':
      document.getElementsByTagName('body')[0].innerHTML = responseText
      break
    default:
      console.log('unknown response data type: ${response.type}')
    }
  }

  function list_movies(movies) {
    let list = document.getElementById('movie_list')
    list.innerHTML = ''
    for (let i = 0; i < movies.length; i++) {
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
        handle_response(request.responseText)
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
        handle_response(request.responseText)
      }
    }
    request.open('GET', '/movies', true)
    request.send()
  }
})()