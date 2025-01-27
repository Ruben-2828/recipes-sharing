let ingredientCount = 1;

function addIngredient() {
    ingredientCount++;
    const container = document.getElementById('ingredients-container');
    const newIngredient = document.createElement('div');
    newIngredient.className = 'ingredient-entry';
    
    newIngredient.innerHTML = `
        <div class="form-group">
            <label for="ingredient-name-${ingredientCount}">Ingredient</label>
            <input type="text" id="ingredient-name-${ingredientCount}" name="ingredient_name[]" required>
        </div>
        <div class="form-group">
            <label for="ingredient-quantity-${ingredientCount}">Quantity</label>
            <input type="text" id="ingredient-quantity-${ingredientCount}" name="ingredient_quantity[]" required>
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
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', updateRemoveButtons); 