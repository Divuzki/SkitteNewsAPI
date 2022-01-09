var navBtn = document.querySelectorAll(".btn-toggle-nav")
var sidebar = document.querySelector(".nav-sidebar")
var sidebarUl = document.getElementsByTagName("ul")[1]

function showSideBar() {
    sidebar.classList.add("show")
    navBtn[0].classList.add("hide")
    navBtn[1].classList.add("show")
    sidebarUl.classList.add("show")
}

function closeSideBar() {
    sidebar.classList.remove("show")
    navBtn[0].classList.remove("hide")
    navBtn[1].classList.remove("show")
    sidebarUl.classList.remove("show")
}