

document.getElementsByTagName('select')[0].onchange = function() {
    var index = this.selectedIndex;
    if(index == 0) {
        document.getElementsByClassName('player-label')[0].textContent = 'Player 1';
        document.getElementsByClassName('player-label')[1].textContent = 'Player 2';
        document.getElementsByClassName('player')[0].getElementsByTagName('img')[0].src = 'static/img/image1.png';
        document.getElementsByClassName('player')[1].getElementsByTagName('img')[0].src = 'static/img/image2.png';
    } else if(index == 1) {
        document.getElementsByClassName('player-label')[0].textContent = 'Player';
        document.getElementsByClassName('player-label')[1].textContent = 'Bot';
        document.getElementsByClassName('player')[0].getElementsByTagName('img')[0].src = 'static/img/image1.png';
        document.getElementsByClassName('player')[1].getElementsByTagName('img')[0].src = 'static/img/bot.png';
    } else if(index == 2){
        document.getElementsByClassName('player-label')[0].textContent = 'Bot 1';
        document.getElementsByClassName('player-label')[1].textContent = 'Bot 2';
        document.getElementsByClassName('player')[0].getElementsByTagName('img')[0].src = 'static/img/bot.png';
        document.getElementsByClassName('player')[1].getElementsByTagName('img')[0].src = 'static/img/bot.png';
    }
}