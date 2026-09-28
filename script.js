const diceFaces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
const diceElement = document.getElementById('dice');
const buttonElement = document.getElementById('roll-btn');

buttonElement.addEventListener('click', () => {
    // Add spin animation
    diceElement.classList.add('roll-animation');
    
    // Disable button during spin
    buttonElement.disabled = true;

    setTimeout(() => {
        // Generate random number between 0 and 5
        const randomIndex = Math.floor(Math.random() * 6);
        
        // Update dice face text
        diceElement.textContent = diceFaces[randomIndex];
        
        // Reset animation and button
        diceElement.classList.remove('roll-animation');
        buttonElement.disabled = false;
    }, 200);
});
