(() => {
  function handle_response(responseText) {
    let response = JSON.parse(responseText)
    switch (response.type) {
    case 'folder':
      list_movies(response.path, response.data)
      break
    case 'subtitles':
      list_subtitles(response.data)
      break
    case 'message':
      document.getElementsByTagName('body')[0].innerHTML = responseText
      break
    default:
      console.log('unknown response data type: ${response.type}')
    }
  }

  function list_subtitles(items) {
    let subject = document.getElementById('subject')
    subject.innerText = 'Subtitle list'
    let list = document.getElementById('movie_list')
    list.innerHTML = ''
    for (let i = 0; i < items.length; i++) {
      let item = document.createElement('li')
      let link = document.createElement('a')
      link.setAttribute('href', items[i].download_url[0])
      link.innerText = items[i].title + ' <' + items[i].lang + '> <' +
                       items[i].type + '> [rate: ' + items[i].rate + 
                       '] [download: ' + items[i].download_number + ']'
      item.appendChild(link)
      list.appendChild(item)
    }
  }

  function list_movies(path, movies) {
    let subject = document.getElementById('subject')
    subject.innerText = path.slice(path.lastIndexOf('/'))
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
    request.open('GET', '/home', true)
    request.send()
  }
})()