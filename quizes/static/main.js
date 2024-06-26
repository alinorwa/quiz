console.log('hello')
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href


modalBtns.forEach(modalBtn =>  modalBtn.addEventListener('click' , () => {

    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-name')
    const numQuestion = modalBtn.getAttribute('data-question')
    const difficluty = modalBtn.getAttribute('data-difficluty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')
    
    modalBody.innerHTML = `
        <div class='h5 mb-3'>Are you sure you want to begin <b>${name}</b>?</div>
        <div class='text-muted' >
          <ul>
             <li>difficluty : <b>${difficluty}</b></li>
             <li>number of question : <b>${numQuestion}</b></li>
             <li>score to pass : <b>${scoreToPass}</b> %</li>
             <li>time : <b>${time} min</b></li>
          </ul>
        </div>
    `
    startBtn.addEventListener('click' , ()=> {
        window.location.href = url + pk
    })
    
      
}))

