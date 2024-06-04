document.addEventListener("DOMContentLoaded", function() {
    // Find the container element by its ID
    const gameContainer = document.getElementById('game-container');
    
    if (!gameContainer) {
        console.error("Game container not found!");
        return;
    }

    // Get the unzipped location URL from the data attribute
    const gameUrl = gameContainer.getAttribute('game-url');

    // Check if the game URL is present
    if (!gameUrl) {
        console.error("Game URL not found in game-url attribute!");
        return;
    }

    // Load the main game script
    const script = document.createElement('script');
    script.src = gameUrl + '/index.js';
    script.type = 'module';
    script.onload = () => {
        import(gameUrl + '/index.js').then((module) => {
            const project = module.default;
            gameContainer.appendChild(project.view);
        }).catch((error) => {
            console.error("Error loading game script:", error);
        });
    };

    document.body.appendChild(script);
});