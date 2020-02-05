
var index = Math.floor(Math.random() * 5);
var images = [];
var path="../../../media/ads/ad";
for (var i=1; i<6; i++)
{
  images.push(path + i + ".jpg")
}
var time = 4500;
function change(){
    document.adsSlider.src = images[index];
    if(index < images.length - 1)
      index++;
    else
      index = 0;
    setTimeout("change()", time);
}
window.onload = change;
