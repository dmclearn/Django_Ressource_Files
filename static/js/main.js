var burger = document.getElementById("burger")
var links = document.getElementById("nav-items")

burger.addEventListener('click',
    ()=>{
        links.classList.toggle('is-active')
        burger.classList.toggle('is-active')
    }
)

console.log(burger)
console.log(links)