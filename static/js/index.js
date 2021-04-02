let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}

function main() {
var myHeaders = new Headers();

var myInit = { method: 'GET',
               headers: myHeaders,
               mode: 'cors',
               cache: 'default' };

fetch('http://localhost:5000/test',myInit)
.then(function(response) {
  return response.blob();
})
.then(function(myBlob) {
    alert('coucou')
 
});
}
main();