
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
