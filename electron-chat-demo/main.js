const fs = require('fs');
const path = require('path');
const SAVE_PATH = path.join(__dirname, 'save.json');

class Card {
    constructor(text, response,time) {
        this.text = text;
        this.response = response;
        this.time = time;
    }
    tosave(){
        return {
            text: this.text,
            response: this.response,
            time: this.time
        };
    }
    static fromsave(data){
        return new Card(data?.text||"", data?.response||"", data?.time||Date.now());
    }
}
class Discussion {
    constructor() {
        this.cards = [];
    }   
    addCard(card) {
        this.cards.push(card);
    }
      tosave() { return JSON.stringify(this.cards, null, 2); }
}
function loadDiscussion(filename) {
    const discussion = new Discussion();
     if (!fs.existsSync(filename)) {
      fs.writeFileSync(filename, "[]", "utf8");
      return discussion;
    }
    const data = fs.readFileSync(filename, 'utf8');
    const cardsData = JSON.parse(data);
    cardsData.forEach(cardData => {
        const card = Card.fromsave(cardData);
        discussion.addCard(card);
    });
    return discussion;
}
let discussion = loadDiscussion(SAVE_PATH)||new Discussion();
let xx=`
<nav><h1>Welcome to AI Model</h1></nav>
<div id="cards">`;
if(discussion.cards.length==0){
    discussion.addCard(new Card("Bienvenue dans l'analyseur de sentiments !", "", Date.now()));
}
for(let card of discussion.cards){
    xx+=`
    <div class="card">
        <div class="card-body d-flex justify-content-end user-msg">${(card.text)}</div>
        <div class="card-footer bot-msg">${(card.response)}</div>
    </div>
    `;
}
xx+=`<textarea class="form-control" id="text" rows="3" placeholder="Enter your text here"></textarea>
<button class="btn btn-primary" id="sendBtn"><i class="bi bi-send"></i></button>
</div>`;
document.body.innerHTML=xx;
document.getElementById('sendBtn').addEventListener('click', generateResponse);
function generateResponse(){
    let cardsDiv = document.getElementById('cards');
    const userInput = document.getElementById('text');
    const text = userInput.value;
    const card = new Card(text, `this is a response for "${text}"`, Date.now());
    discussion.addCard(card);
    fs.writeFileSync(SAVE_PATH, discussion.tosave());
    cardsDiv.insertAdjacentHTML('beforeend', `
    <div class="card">
        <div class="card-body d-flex justify-content-end user-msg">${card.text}</div>
        <div class="card-footer bot-msg">${card.response}</div>
    </div>
    `);
    userInput.value = '';
}


