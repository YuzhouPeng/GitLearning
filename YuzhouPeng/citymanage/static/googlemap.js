window.onload = function initMap() {
    var canvas = document.getElementById("map");
    var options = {
        center: new google.maps.LatLng(53.343507, -6.253920),
        zoom: 10
    };
    var map = new google.maps.Map(canvas, options);
}

document.write('<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCqWiyZjXWgHExWGy92GcFSWSS7F2EEm8U&language=en"></script>')
