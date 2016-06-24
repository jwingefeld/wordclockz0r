function switchto(num) {
  $('#segments').animate( { scrollLeft: 900*num }, 300);
  if (num==2) {
    $('.progress:nth-of-type(3)').addClass("done");
  }
  console.log($("input[name='font']:checked"))

}
function submitform() {
  $("#message").html("This be takin some tiemz and i am le-tired.")
  filelink = "<a href=\"../openscad/lasercut.zip\">aaa</a>";
  window.setTimeout('$("#message").html("Here is your file: <br /><a href=../openscad/lasercut.zip><input type=button class=button value=lasercut.zip /></a>");',3000);

}
function checkfields() {
//  if $('#')
  //alert($(""));
}
window.setInterval("less.watch();",1000);
