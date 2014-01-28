var bluey=function(e) {
    this.classList.toggle('blue');

var elts = document.querySelectorAll('li');
for (var i=0;i<elts.length;i++) {
    elts[i].addEventListener('click',bluey);

}
