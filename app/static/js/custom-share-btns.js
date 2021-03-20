function fbShare(winWidth, winHeight) {
    var title = document.getElementsByTagName('h1').item(0).innerHTML
    var descr = document.getElementsByTagName('h2').item(0).innerHTML
    var image = document.getElementsByTagName('header').item(0).style.backgroundImage.slice(5,-2)
    var winTop = (screen.height / 2) - (winHeight / 2);
    var winLeft = (screen.width / 2) - (winWidth / 2);
    window.open(`http://www.facebook.com/sharer.php?s=100&p[title]=${title}&p[summary]=${descr}&p[url]=${window.location.href}&p[images][0]=${image}`, 'sharer', `top=${winTop},left=${winLeft},toolbar=0,status=0,width=${winWidth},height=${winHeight}`);
}


function twitterShare(winWidth, winHeight) {
    var title = document.getElementsByTagName('h1').item(0).innerHTML
    var descr = document.getElementsByTagName('h2').item(0).innerHTML
    var winTop = (screen.height / 2) - (winHeight / 2);
    var winLeft = (screen.width / 2) - (winWidth / 2);
    window.open(`https://twitter.com/share?url=${window.location.href}&text=Recomendo o post "${title}: ${descr}" do Blog do André. Acesse no link: `, 'sharer' , `top=${winTop},left=${winLeft},toolbar=0,status=0,width=${winWidth},height=${winHeight}`);
}