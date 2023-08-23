function handleSearch() {
    var categorySelect = document.getElementById("categorySelect");
    var selectedCategoryId = categorySelect.value;
    
    var inputText = document.querySelector(".header-search .input");
    var searchText = inputText.value.toLowerCase();
    
    var items = document.querySelectorAll(".product-item");
    
    items.forEach(function(item) {
        var categoryId = item.getAttribute("data-category");
        var itemName = item.getAttribute("data-name").toLowerCase();
        
        var categoryMatch = (selectedCategoryId === "0" || categoryId === selectedCategoryId);
        var textMatch = itemName.includes(searchText);
        
        if (categoryMatch && textMatch) {
            item.style.display = "block";
        } else {
            item.style.display = "none";
        }
    });
}
