window.addEventListener('message', function(message){
    if(message.data.type=='preview.compiled') {
        console.log("Acertô, miseravi")
    }
})