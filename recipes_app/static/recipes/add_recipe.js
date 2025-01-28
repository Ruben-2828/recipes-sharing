function addIngredient() {
    const container = document.getElementById('ingredients-container');
    const newIngredient = document.createElement('div');
    newIngredient.className = 'ingredient-entry';

    newIngredient.innerHTML = `
        <div class="form-group">
            <label for="id_ingredient-X-name">Ingredient</label>
            <input type="text" id="id_ingredient-X-name" name="ingredient-X-name" required>
        </div>
        <div class="form-group">
            <label for="id_ingredient-X-quantity">Quantity</label>
            <input type="text" id="id_ingredient-X-quantity" name="ingredient-X-quantity" required>
        </div>
        <button type="button" class="btn btn-remove" onclick="removeIngredient(this)">
            Remove
        </button>
    `;

    container.appendChild(newIngredient);
    updateRemoveButtons();
}

function removeIngredient(button) {
    const ingredientEntry = button.parentElement;
    ingredientEntry.remove();
    updateRemoveButtons();
}

function updateRemoveButtons() {
    const ingredients = document.querySelectorAll('.ingredient-entry');
    const removeButtons = document.querySelectorAll('.btn-remove');

    removeButtons.forEach(button => {
        button.disabled = ingredients.length === 1;
    });

    // Update total forms count in management form
    const totalFormsInput = document.querySelector('[name="ingredient-TOTAL_FORMS"]');
    if (totalFormsInput) {
        totalFormsInput.value = ingredients.length;
    }

    // Update ids and names of remaining ingredients
    ingredients.forEach((ingredient, index) => {
        const nameInput = ingredient.querySelector('input[id*="-name"]');
        const quantityInput = ingredient.querySelector('input[id*="-quantity"]');
        const nameLabel = ingredient.querySelector('label[for*="-name"]');
        const quantityLabel = ingredient.querySelector('label[for*="-quantity"]');

        // Update name input
        nameInput.id = `id_ingredient-${index}-name`;
        nameInput.name = `ingredient-${index}-name`;
        nameLabel.setAttribute('for', `id_ingredient-${index}-name`);

        // Update quantity input  
        quantityInput.id = `id_ingredient-${index}-quantity`;
        quantityInput.name = `ingredient-${index}-quantity`;
        quantityLabel.setAttribute('for', `id_ingredient-${index}-quantity`);
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', updateRemoveButtons); 