const url = window.location.href
const quizBox = document.getElementById('quiz-box') 
const scoreBox = document.getElementById('score-box') 
const resultBox = document.getElementById('result-box') 

// for time function
// const activateTimer = (time) => {
//     console.log(time)
// }


$.ajax({
    type:'GET',
    url : `${url}data`,
    success:function(respons){
        const data = respons.data
        data.forEach(el => {

            for(const [question , answers] of Object.entries(el)){
                quizBox.innerHTML += `
                   <hr>
                   <div class='mb-2' >
                      <b>${question}</b>
                   </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                     <div>
                     <input type="radio" class='ans' id='${question}-${answer}' name="${question}" value='${answer}' >
                     <label for="${question}">${answer}</label> 
                     </div>
                    `
                })
            }
            
        });
        // for the time function
        // activateTimer(respons.time)
    }, 
    error:function(error){
        console.log(error)
    }, 
})


//======== 

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData =() =>{
    const element = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value 
    element.forEach(el => {
            if(el.checked){
                 data[el.name] = el.value
                
            }else{
                if(!data[el.name]){
                    data[el.name] = null
                }
            }
    })

    $.ajax({
        type: 'POST',
        url : `${url}save/`,
        data:data,
        success:function(respons){
            const results = respons.results
           
            quizForm.classList.add('not-visible')
            scoreBox.innerHTML = `${respons.passed ? 'congratulations !': 'Ups... :('} Your result is ${respons.score.toFixed(2)}%`


            results.forEach(res => {
                const resDiv = document.createElement('div')
                for (const [question,resp] of Object.entries(res)){
                     resDiv.innerHTML += question
                     const cls = ['container','p-3','text-light' ,'h6']
                     resDiv.classList.add(...cls)
                     if (resp == 'not answerd') {
                        resDiv.innerHTML += '- not answerd'
                        resDiv.classList.add('bg-danger')  
                     }else{
                        const answer = resp['answred']
                        const correct = resp['correct_answer']
                            if (answer == correct) {
                                resDiv.classList.add('bg-success')
                                resDiv.innerHTML += `answerd : ${answer}`
                                
                            }else{
                                resDiv.classList.add('bg-danger')
                                resDiv.innerHTML += `| correct answer : ${correct}`
                                resDiv.innerHTML += `| answered : ${answer}`
                            }
                     }
                }
                // const body = document.getElementsByTagName('BODY')[0] 
                resultBox.append(resDiv)
            })
        },
        error:function(error){
            console.log(error)
        },
    })
}

quizForm.addEventListener('submit', (e)=>{
    e.preventDefault()
    sendData()
})