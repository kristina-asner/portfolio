
const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particlesArray;

const symbols = [
    'Python', 'C++', 'C#', 'SQL', 
    'GIT', 'OOP', '97.13', 
    '{ }', '</>', '[]', '&&', 
    '0', '1'
];

let mouse = { x: null, y: null, radius: 150 };

window.addEventListener('mousemove', function(event) {
    mouse.x = event.x;
    mouse.y = event.y;
});

class Particle {
    constructor(x, y, directionX, directionY, fontSize, text) {
        this.x = x; this.y = y;
        this.directionX = directionX; this.directionY = directionY;
        this.fontSize = fontSize; this.text = text;
        this.baseColor = 'rgba(255, 255, 255, 0.08)';
        this.color = this.baseColor;
        this.fontWeight = (Math.random() > 0.5) ? 'normal' : 'bold';
    }
    
    draw() {
        ctx.font = `${this.fontWeight} ${this.fontSize}px Montserrat, monospace`;
        ctx.fillStyle = this.color;
        ctx.fillText(this.text, this.x, this.y);
    }
    
    update() {
        if (this.x > canvas.width + 50) this.x = -50;
        if (this.x < -50) this.x = canvas.width + 50;
        if (this.y > canvas.height + 50) this.y = -50;
        if (this.y < -50) this.y = canvas.height + 50;

        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx*dx + dy*dy);
        
        if (distance < mouse.radius){
             this.color = '#cc4100';
             this.x += this.directionX * 2; this.y += this.directionY * 2;
        } else { this.color = this.baseColor; }
        
        this.x += this.directionX; this.y += this.directionY;
        this.draw();
    }
}

function init() {
    particlesArray = [];
    let numberOfParticles = (canvas.height * canvas.width) / 20000;
    for (let i = 0; i < numberOfParticles; i++) {
        let fontSize = (Math.random() * 14) + 10;
        let x = Math.random() * canvas.width;
        let y = Math.random() * canvas.height;
        let directionX = (Math.random() * 0.6) - 0.3; 
        let directionY = (Math.random() * 0.6) - 0.3; 
        let text = symbols[Math.floor(Math.random() * symbols.length)];
        particlesArray.push(new Particle(x, y, directionX, directionY, fontSize, text));
    }
}

function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0,0,innerWidth, innerHeight);
    for (let i = 0; i < particlesArray.length; i++) { particlesArray[i].update(); }
}

init(); animate();
window.addEventListener('resize', function(){
    canvas.width = innerWidth; canvas.height = innerHeight; init();
});



function toggleTerminal() {
    const terminal = document.getElementById('terminal-wrapper');
    terminal.classList.toggle('closed');
}

function addMessageToChat(text, sender) {
    const chat = document.getElementById('chat-display');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('msg', sender);
    msgDiv.innerHTML = sender === 'user' ? `> ${text}` : text;
    chat.appendChild(msgDiv);
    chat.scrollTop = chat.scrollHeight; 
}




document.addEventListener("DOMContentLoaded", () => {
    fetchDailyChallenge();
});

async function fetchDailyChallenge() {
    try {
        const response = await fetch('https://kristina-portfolio-b3zs.onrender.com/api/daily-challenge');
        if (!response.ok) throw new Error("Server Error");
        
        const data = await response.json();
        
        const diffBadge = document.querySelector('.difficulty');
        diffBadge.textContent = data.difficulty;
        
        diffBadge.className = 'badge difficulty'; 
        if (data.difficulty === 'Easy') diffBadge.style.background = 'rgba(0, 255, 0, 0.2)';
        if (data.difficulty === 'Medium') diffBadge.style.background = 'rgba(255, 165, 0, 0.2)';
        if (data.difficulty === 'Hard') diffBadge.style.background = 'rgba(255, 0, 0, 0.2)';

        document.getElementById('lc-title').textContent = data.title;
        document.getElementById('lc-desc').textContent = data.description;
        document.getElementById('lc-link').href = data.link;
        
        window.currentProblemTitle = data.title;
        
    } catch (error) {
        console.error("Error connecting to server:", error);
        document.getElementById('lc-title').textContent = "Server Offline";
        document.getElementById('lc-desc').textContent = "Please run 'python app.py' in the backend folder.";
    }
}

async function getAIHint() {
    const hintBox = document.getElementById('ai-hint-box');
    hintBox.classList.remove('hidden');
    hintBox.classList.add('visible');
    hintBox.innerHTML = "<span class='typing-cursor'>Requesting hint from Python Server...</span>";

    try {
        const response = await fetch('https://kristina-portfolio-b3zs.onrender.com/api/hint', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: window.currentProblemTitle })
        });
        const data = await response.json();
        
        setTimeout(() => {
            hintBox.innerHTML = `> <strong>AI Hint:</strong> ${data.hint}`;
        }, 1000); 
        
    } catch (error) {
        hintBox.innerHTML = "> Error: Could not reach the server.";
    }
}

async function handleKeyPress(event) {
    if (event.key === 'Enter') {
        const input = document.getElementById('user-input');
        const text = input.value;
        if (!text) return;

        addMessageToChat(text, 'user');
        input.value = '';

        const loadingId = "loading-" + Date.now();
        const chat = document.getElementById('chat-display');
        const loadingDiv = document.createElement('div');
        loadingDiv.id = loadingId;
        loadingDiv.classList.add('msg', 'bot');
        loadingDiv.innerHTML = "<span class='typing-cursor'>...</span>";
        chat.appendChild(loadingDiv);
        chat.scrollTop = chat.scrollHeight;

        try {
            const response = await fetch('https://kristina-portfolio-b3zs.onrender.com/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });
            const data = await response.json();
            
            document.getElementById(loadingId).remove();
            addMessageToChat(data.response, 'bot');
            
        } catch (error) {
            document.getElementById(loadingId).remove();
            addMessageToChat("Error: Server not responding.", 'system');
        }
    }
}