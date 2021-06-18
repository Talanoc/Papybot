let nb = 0;

let soumettre = async function () {

  let myInit = {
    method: 'GET',
    headers: new Headers(),
    mode: 'cors',
    cache: 'default'
  };
  
  let question = document.getElementById('user_question').value;
  console.log(question);
  let response = await fetch(`https://talanoc-papybot.herokuapp.com/question/${question}`, myInit);
  console.log(response);
  let data = await response.json();
  
  console.table(data);

  if (data.address != null ) {

      let map_id = `map_${nb}`;
      let response_box = document.getElementById("response_box");
      let content =
        `
        <div class="container mt-3">
            <div class="media border p-3">
            <img id="intero" src="static/img/interrogation.gif">
                <div class="media-body"> 
                    <h4>Votre demande : ${data.user_question_sw[1]}</h3>
                </div>
            </div>
        </div>
        <div class="container mt-3">
            <div class="media border p-3">
                <img src="static/img/vieux-sage.jpg" alt="papybot" class="mr-3 mt-3 rounded-circle" style="width: 40px;" />
                <div class="media-body">
                    <div id="ville">
                      La ville de ${data.wiki.wiki_title} est très jolie. J'y suis passé il y a fort longtemps.<br>
                      Adresse : ${data.address}<br>
                    </div>
                    <div id="response"  >
                        <div class="map" id="${map_id}"></div>
                        <div class="wiki" id="wiki_text">${data.wiki.wiki_text}</div>
                    </div>
                </div>
            </div>
        </div>
        
        `;
      response_box.innerHTML = content + response_box.innerHTML;
      new google.maps.Map(document.getElementById(map_id),
      {
        center: { lat:data.lat , lng: data.lon },zoom: 16
      });
      } 
  else {
      let response_box = document.getElementById("response_box");
      let content = 
        `
        <div class="container mt-3">
            <div class="media border p-3">
            <img id="erreur" src="static/img/boussole.gif">
                <div class="media-body"> 
                    <h4>J'ai un petit problème avec ta question.il faut reformuler la question </h4>
                </div>
            </div>
        </div> `
          ;
      response_box.innerHTML = content + response_box.innerHTML;
    }
nb += 1;
}