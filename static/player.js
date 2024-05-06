document.getElementById('prev').onclick = prevMovie;
document.getElementById('next').onclick = nextMovie;
document.getElementById('video-player').addEventListener('error', e => {
  document.getElementById('movie-index').innerHTML = 'no more video';
}, true);


function prevMovie() { 
    const player = document.getElementById('video-player');
    const videoSource = document.getElementById('video-src');
    
    player.pause();
    player.currentTime = 0;
    const src = videoSource.getAttribute('src');
    const srcAsList = src.split('/');
    const len = srcAsList.length;
    const idx = parseInt(srcAsList[len - 1]) - 1;
    srcAsList[len - 1] = idx;
    const newSrc = srcAsList.join('/');
    videoSource.setAttribute('src', newSrc);
    document.getElementById('movie-index').innerHTML = idx + 1;
    player.load();
    player.play();
}


function nextMovie() {
    const player = document.getElementById('video-player');
    const videoSource = document.getElementById('video-src');
    
    player.pause();
    player.currentTime = 0;
    const src = videoSource.getAttribute('src');
    const srcAsList = src.split('/');
    const len = srcAsList.length;
    const idx = parseInt(srcAsList[len - 1]) + 1;
    srcAsList[len - 1] = idx;
    const newSrc = srcAsList.join('/');
    videoSource.setAttribute('src', newSrc);
    document.getElementById('movie-index').innerHTML = idx + 1;
    player.load();
    player.play();
 }