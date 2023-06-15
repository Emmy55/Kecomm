const search = document.getElementById("search")
const myElement = document.getElementById("nav input");



function handleClick(element) {
   // Listen to clicks on the specified element
   element.addEventListener("click", function (event) {
      search.style.display = 'none'
      search.style.position = 'absolute'
      // Do something when the element is clicked
   });

   // Listen to clicks on the rest of the page 
//    document.addEventListener("click", function (event) {
//       // Check if the clicked element is not the specified element or its descendant
//       if (!element.contains(event.target)) {
//          search.style.display = 'block'
//          search.style.top = '7px'
//          search.style.position = 'absolute'
//          search.style.left = '-59px'

//          // Do something when clicked outside of the element
//       }
//    });
}

// Call the function with the specified element
handleClick(myElement);