const fetch = require('node-fetch');

var myInit = { method: 'POST',
                headers: { "Content-Type": "application/x-www-form-urlencoded"},
                mode: 'cors',
                cache: 'default',
                isBase64Encoded: false
};

fetch('https://c90tfg0wpf.execute-api.us-east-1.amazonaws.com/getMovies', myInit)
        .then(res =>  res.json())
        .then(data => listMovies(data))
        .catch(error => console.log('error', error));



function listMovies(movies){
    this.cardMovies = document.getElementById('div-total'); //.querySelector('card-c');
    this.cardMovies.innerHTML = '';

    for(var i = 0; i < movies.length; i++){

        //MODAL
        let tituloModal = document.createElement('p');
        tituloModal.setAttribute('class', 'modal-title');
        tituloModal.appendChild(document.createTextNode(movies[i].title));
        console.log(movies[i].title)

        let botaoX = document.createElement('span');
        botaoX.appendChild(document.createTextNode('X'));

        let botaoModal = document.createElement('button');
        botaoModal.setAttribute('type', 'button');
        botaoModal.setAttribute('class', 'close');
        botaoModal.setAttribute('data-dismiss', 'modal');
        botaoModal.appendChild(botaoX);

        let criarDivModal = document.createElement('div');
        criarDivModal.setAttribute('class', 'modal-header');
        criarDivModal.appendChild(tituloModal);
        criarDivModal.appendChild(botaoModal);

        //CRIAR MODAL DIV


        let imagemModal = document.createElement('img');
        imagemModal.setAttribute('id', 'card-image');
        imagemModal.setAttribute('class', 'd-none d-md-block');
        imagemModal.setAttribute('onerror', "this.src='ERROR.png'");
        imagemModal.setAttribute('src', movies[i].imageM);

        let estreiaM = document.createElement('p');
        estreiaM.setAttribute('id', 'modal-p');
        estreiaM.setAttribute('margin-top', '20px');
        estreiaM.appendChild(document.createTextNode('Estreia: ' + movies[i].date));

        let criarDivRowOne = document.createElement('div');
        criarDivRowOne.setAttribute('id', 'div-row-one');
        criarDivRowOne.appendChild(imagemModal);
        criarDivRowOne.appendChild(estreiaM);




        let linhaH = document.createElement('hr');
        linhaH.setAttribute('size', '10px');

        let infoSinopse = document.createElement('p');
        infoSinopse.setAttribute('class', 'parag');
        infoSinopse.appendChild(document.createTextNode('Sinopse: ' + movies[i].sinopse));

        let infoCategoria = document.createElement('p');
        infoCategoria.setAttribute('class', 'parag');
        infoCategoria.appendChild(document.createTextNode('Categoria: ' + movies[i].category));

        let infoElenco = document.createElement('p');
        infoElenco.setAttribute('class', 'parag');
        infoElenco.appendChild(document.createTextNode('Elenco: ' + movies[i].actors));

        let infoDirecao = document.createElement('p');
        infoDirecao.setAttribute('class', 'parag');
        infoDirecao.appendChild(document.createTextNode('Direção: ' + movies[i].director));
        
        let infoPO = document.createElement('p');
        infoPO.setAttribute('class', 'parag');
        infoPO.appendChild(document.createTextNode('País de Origem: ' + movies[i].countryOfOrigin));

        let infoClassif = document.createElement('p');
        infoClassif.setAttribute('class', 'parag');
        infoClassif.appendChild(document.createTextNode('Classificação: ' + movies[i].classification));


        let criarDivRowTwo = document.createElement('div');
        criarDivRowTwo.setAttribute('id', 'div-row-two');
        criarDivRowTwo.appendChild(infoSinopse);
        criarDivRowTwo.appendChild(infoCategoria);
        criarDivRowTwo.appendChild(infoElenco);
        criarDivRowTwo.appendChild(infoDirecao);
        criarDivRowTwo.appendChild(infoPO);
        criarDivRowTwo.appendChild(infoClassif);
        criarDivRowTwo.appendChild(linhaH);




        let criarDivRow = document.createElement('div');
        criarDivRow.setAttribute('class', 'row');
        criarDivRow.appendChild(criarDivRowOne);
        criarDivRow.appendChild(criarDivRowTwo);
        
        let criarDivContainer = document.createElement('div');
        criarDivContainer.setAttribute('class', 'container-fluid');
        criarDivContainer.appendChild(criarDivRow);

        let criarDivModalBody = document.createElement('div');
        criarDivModalBody.setAttribute('class', 'modal-body');
        criarDivModalBody.appendChild(criarDivContainer);

        let criarDivModalContent = document.createElement('div');
        criarDivModalContent.setAttribute('class', 'modal-content');
        criarDivModalContent.appendChild(criarDivModal);
        criarDivModalContent.appendChild(criarDivModalBody);

        let criarDivModalDialog = document.createElement('div');
        criarDivModalDialog.setAttribute('class', 'modal-dialog modal-lg');
        criarDivModalDialog.appendChild(criarDivModalContent);

        var idAuxModal = 'siteModal' + i;
        let criarDivModalModal = document.createElement('div');
        criarDivModalModal.setAttribute('class', 'modal');
        criarDivModalModal.setAttribute('aria-labelledby', 'siteModalAria');
        criarDivModalModal.setAttribute('aria-hidden', 'true');
        criarDivModalModal.setAttribute('id', idAuxModal);
        criarDivModalModal.setAttribute('tabindex', '-1');
        criarDivModalModal.setAttribute('role', 'dialog');
        criarDivModalModal.appendChild(criarDivModalDialog);




        let imagemR = document.createElement('img');
        imagemR.setAttribute('src', 'https://img.icons8.com/color/30/000000/prize.png');

        let ranking = document.createElement('p');
        ranking.setAttribute('id', 'id-ranking');
        ranking.appendChild(document.createTextNode((i + 1) + 'º Lugar'));
        ranking.appendChild(imagemR);




        let img = document.createElement('img');
        img.setAttribute('id', 'card-image');
        //img.setAttribute('class', 'd-none d-md-block');
        img.setAttribute('onerror', "this.src='ERROR.png'");
        img.setAttribute('src', movies[i].imageM);


        //Próxima DIV
        let tituloCard = document.createElement('p');
        tituloCard.setAttribute('class', 'card-title');
        var cartaz = '';
        if(movies[i].emCartaz == 'yes'){
            cartaz = 'Em Cartaz';
        } else{
            cartaz = 'Em Breve';
        }
        tituloCard.appendChild(document.createTextNode(cartaz));

        let imagensP = document.createElement('img');
        imagensP.setAttribute('id', 'card-iconP');
        imagensP.setAttribute('src', 'https://img.icons8.com/dusk/64/000000/thumb-up.png');

        let imagensN = document.createElement('img');
        imagensN.setAttribute('id', 'card-iconN');
        imagensN.setAttribute('src', 'https://img.icons8.com/dusk/64/000000/thumbs-down.png');

        let avaliacoes = document.createElement('p');
        avaliacoes.setAttribute('id', 'card-avaliacao');
        avaliacoes.appendChild(document.createTextNode(movies[i].positive));
        avaliacoes.appendChild(imagensP);
        avaliacoes.appendChild(document.createTextNode(movies[i].negative));
        avaliacoes.appendChild(imagensN);
        
        var idAuxDT = '#siteModal' + i;
        let linkModal = document.createElement('a');
        linkModal.setAttribute('href', '#');
        linkModal.setAttribute('data-toggle', 'modal');
        linkModal.setAttribute('data-target', idAuxDT);
        linkModal.appendChild(document.createTextNode('Ver mais...'));

        let verModal = document.createElement('p');
        verModal.setAttribute('id', 'card-link');
        verModal.appendChild(linkModal);

        let criarDivInfo = document.createElement('div');
        criarDivInfo.setAttribute('id', 'card-body');
        criarDivInfo.appendChild(tituloCard);
        criarDivInfo.appendChild(avaliacoes);
        criarDivInfo.appendChild(verModal);


        let criarCard = document.createElement('div');
        criarCard.setAttribute('class', 'card card-c');
        criarCard.appendChild(ranking);
        criarCard.appendChild(img);
        criarCard.appendChild(criarDivInfo);
        criarCard.appendChild(criarDivModalModal);


        this.cardMovies.appendChild(criarCard);
        
    }

}


/*function movies(dados){
    console.log(dados);
    document.querySelector('#id-ranking').innerHTML = '1º Lugar <img src="https://img.icons8.com/color/30/000000/prize.png"/>';
    document.querySelector('.card-title').innerHTML = dados[0].title;
    document.getElementById('card-image').src.innerHTML = 'filme2.jpg';
    document.querySelector('#card-avaliacao').innerHTML = '40% <img id="card-iconP" src="https://img.icons8.com/dusk/64/000000/thumb-up.png"/> 60% <img id="card-iconN"  src="https://img.icons8.com/dusk/64/000000/thumbs-down.png"/>';
    
    document.querySelector('.modal-title').innerHTML = " obj.title";
    document.getElementById('modal-image').src.innerHTML = 'filme2.jpg';
    document.querySelector('#modal-p').innerHTML = '2020-03-28';
    var informacoes = document.querySelectorAll('.parag');
    for(var i=0; i<informacoes.length; i++){
        informacoes[i].innerHTML = 'AQUI é uma sinopse.';
    }
}*/

/*
function alterarCard(){
    document.querySelector('#id-ranking').innerHTML = '1º Lugar <img src="https://img.icons8.com/color/30/000000/prize.png"/>';
    document.querySelector('.card-title').innerHTML = "obj.title";
    document.getElementById('card-image').src.innerHTML = 'filme2.jpg';
    document.querySelector('#card-avaliacao').innerHTML = '40% <img id="card-iconP" src="https://img.icons8.com/dusk/64/000000/thumb-up.png"/> 60% <img id="card-iconN"  src="https://img.icons8.com/dusk/64/000000/thumbs-down.png"/>';
    console.log("AQUI FOI");
}

function alterarModal(){
    document.querySelector('.modal-title').innerHTML = " obj.title";
    document.getElementById('modal-image').src.innerHTML = 'filme2.jpg';
    document.querySelector('#modal-p').innerHTML = '2020-03-28';
    var informacoes = document.querySelectorAll('.parag');
    for(var i=0; i<informacoes.length; i++){
        informacoes[i].innerHTML = 'AQUI é uma sinopse.';
    }
}*/