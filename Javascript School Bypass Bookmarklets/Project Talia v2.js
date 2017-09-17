javascript:

var a = window.location.href;

if (a.indexOf("/r/") > -1){
  var b = "http://taliaalghul.comeze.com/index.php?https://www.reddit.com";
  var c = a.substring(29, a.length + 1);
  window.open(b + c,);
}