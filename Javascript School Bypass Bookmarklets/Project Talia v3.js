javascript: 
var a = prompt("Project Talia v3 by T. Activated - Enter Website To Visit");

if (a.length == 0){
  alert("Nothing Was Entered Numb Nuts!");
  exit();
}

if (a.indexOf("www.") == -1 && a.indexOf("http") == -1){
  a = "www." + a;
}

if (a.indexOf(".com") == -1 && a.indexOf(".org") == -1 && a.indexOf(".net") == -1){
  a = a + ".com"
}

if (a.length > 0){
  window.open("http://taliaalghul.comeze.com/index.php?" + a)
}
