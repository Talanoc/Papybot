

let soumettre=function (){
  var myHeaders = new Headers();

  var myInit = { method: 'GET',
                 headers: myHeaders,
                 mode: 'cors',
                 cache: 'default' };
  
  
  let question=document.getElementById('user_question').value

  fetch(`http://localhost:5000/question/${question}`,myInit)
  
    .then(response => response.json())   
    
    .then(data => {
    console.table(data)
  });
                                  
}
