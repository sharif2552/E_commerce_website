document.addEventListener("DOMContentLoaded", function() {
   
    function handleCategoryFilter(categoryId) {
        const checkbox = document.getElementById(`category-${categoryId}`);
        const isChecked = checkbox.checked;

        // Get the current URL
        let url = new URL(window.location.href);

        // Update the 'category' parameter in the URL
        if (isChecked) {
            url.searchParams.set('category', categoryId);
        } else {
            url.searchParams.delete('category');
        }

        // Redirect to the updated URL
        window.location.href = url.toString();
    }

    function handleSearch() {
        var categorySelect = document.getElementById("categorySelect");
        var selectedCategoryId = categorySelect.value;
        
        var searchInput = document.getElementById("searchInput");
        var searchText = searchInput.value.toLowerCase();
        
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

    var filterForm = document.getElementById("filterForm");
    var filterUrl = filterForm.getAttribute("data-filter-url");

    filterForm.addEventListener("submit", function(event) {
        event.preventDefault();

        // Call the search filtering function
        handleSearch();

        // Get the selected category from the dropdown
        var categorySelect = document.getElementById("categorySelect");
        var selectedCategoryId = categorySelect.value;

        // Check if the current URL is the homepage
        var url = new URL(window.location.href);
        if (url.pathname === '/') {
            // Redirect to the filter_products page
            window.location.href = filterUrl + '?category=' + selectedCategoryId;
        } else {
            // Handle form submission as usual
            handleCategoryFilter(selectedCategoryId);
        }
    });

    // Add other functions here

});
