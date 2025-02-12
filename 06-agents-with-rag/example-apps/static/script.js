async function generateRecipe() {
    const dishName = document.getElementById('dishName').value;
    const dietaryRestrictions = Array.from(document.querySelectorAll('.dietary-restriction.selected'))
        .map(el => el.textContent.trim());
    const spiceLevel = document.getElementById('spiceLevel').value;

    // Clear previous results
    clearResults();
    
    // Show loading state
    document.getElementById('loadingIndicator').style.display = 'block';

    try {
        const response = await fetch('/generate_recipe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                dish_name: dishName,
                dietary_restrictions: dietaryRestrictions,
                spice_level: parseInt(spiceLevel)
            })
        });

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        // Create a div for streaming output
        const streamOutput = document.getElementById('streamOutput') || createStreamOutput();
        
        while (true) {
            const {value, done} = await reader.read();
            if (done) break;
            
            const text = decoder.decode(value);
            const messages = text.split('\n\n');
            
            for (const message of messages) {
                if (message.startsWith('data: ')) {
                    const data = JSON.parse(message.slice(6));
                    
                    if (data.type === 'stream') {
                        // Update streaming output
                        streamOutput.innerHTML += `<div>${data.data}</div>`;
                        streamOutput.scrollTop = streamOutput.scrollHeight;
                    } else {
                        // Final result
                        updateUI(data);
                    }
                }
            }
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('error').textContent = 'An error occurred while generating the recipe.';
    } finally {
        document.getElementById('loadingIndicator').style.display = 'none';
    }
}

function createStreamOutput() {
    const streamOutput = document.createElement('div');
    streamOutput.id = 'streamOutput';
    streamOutput.style.cssText = `
        max-height: 200px;
        overflow-y: auto;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-family: monospace;
        background-color: #f5f5f5;
    `;
    document.querySelector('.recipe-output').prepend(streamOutput);
    return streamOutput;
}

function clearResults() {
    const streamOutput = document.getElementById('streamOutput');
    if (streamOutput) streamOutput.innerHTML = '';
    // Clear other result elements as needed
}